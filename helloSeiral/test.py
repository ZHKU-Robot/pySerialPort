import pandas as pd
import numpy as np
import copy
# import 这里要改成Excel数据

# 资金分配
def fund_allocate(securities, portfolio_value, method, nowtime_str):
    if method == 'equal_weight':
        return pd.DataFrame(dict(symbol=securities, order_value=[portfolio_value / len(securities)] * len(securities)))
    # 查询流通股本,总股本#这里要用EXcel的数据
    q = query(
        valuation.symbol, valuation.circulating_cap, valuation.capitalization, valuation.market_cap,         valuation.current_market_cap
    ).filter(
        valuation.symbol.in_(securities)
    )
    capital_dfs = get_fundamentals(q, nowtime_str)
    capital_dfs = capital_dfs.rename(columns=dict(
        valuation_symbol='symbol',
        valuation_circulating_cap='circulating_cap',
        valuation_capitalization='capitalization',
        valuation_market_cap='market_cap',
        valuation_current_market_cap='current_market_cap',
    ))
    close_dict = history(securities, ['close'], 1, '1d')
    close_dfs = pd.DataFrame(dict(
        symbol=list(close_dict.keys()),
        close=[x['close'].iloc[-1] if not x.empty else np.nan for x in close_dict.values()],
    ))
    df = capital_dfs.merge(close_dfs, left_on='symbol', right_on='symbol', how='outer').dropna()
    # 不同方法分别处理
    if method == 'total_weight':
        df['order_value'] = df['capitalization'] / np.sum(df['capitalization']) * portfolio_value
    elif method == 'circulating_weight':
        df['order_value'] = df['circulating_cap'] / np.sum(df['circulating_cap']) * portfolio_value
    elif method == 'equal_number':
        df['order_value'] = 1 / len(df) * portfolio_value
    elif method == 'total_root':
        df['order_value'] = np.sqrt(df['market_cap']) / np.sqrt(df['market_cap']).sum() * portfolio_value
    elif method == 'circulating_root':
        df['order_value'] = np.sqrt(df['current_market_cap']) / np.sqrt(df['current_market_cap']).sum() * portfolio_value
    else:
        df['order_value'] = [portfolio_value / len(securities)] * len(securities)
    return df[['symbol', 'order_value']]


# 获取股票列表的总市值
def get_market_cap(securities, nowtime_str):
    if not securities:
        q = query(
            valuation.market_cap
        )
    else:
        q = query(
            valuation.market_cap
        ).filter(
            valuation.symbol.in_(securities)
        )
    market_df = get_fundamentals(q, nowtime_str)
    if market_df.empty:
        return 0
    return market_df['valuation_market_cap'].sum()

# 组内资金分配行业中性处理
def industry_neutral(securities, portfolio_value, nowtime_str, data=None, method='equal_weight', index_code='000300.SH',                      industryid='industryid2'):
    data_list = []
    # 默认沪深300，需要支持类型查找
    symbol_all = get_index_stocks(index_code, nowtime_str)
    benchmark_val = get_market_cap(symbol_all, nowtime_str)

    cache_dict = dict()
    industry_dict = dict()
    industry_weight = dict()
    for symbol in securities:
        industry = get_symbol_industry(symbol, nowtime_str)
        if industry is None:
            continue
        industry_id = getattr(industry, industryid)

        if not industry_id in industry_dict:
            industry_dict[industry_id] = [symbol]
        else:
            industry_dict[industry_id].append(symbol)

        if industry_id in cache_dict:
            industry_symbols_num, industry_val = cache_dict.get(industry_id)
        else:
            industry_symbols = get_industry_stocks(industry_id, nowtime_str)
            industry_symbols = list(set(industry_symbols).intersection(set(symbol_all)))
            # 计算个股所属行业在基准中的行业权重
            industry_symbols_num, industry_val = len(industry_symbols), get_market_cap(industry_symbols, nowtime_str)
            cache_dict[industry_id] = (industry_symbols_num, industry_val)
        industry_weight[industry_id] = industry_val / benchmark_val
        data_list.append((symbol, industry_weight[industry_id], 100 / industry_symbols_num, industry_symbols_num))

    # 当前默认分配方式，需要参数指定配合前端接口#这里就想改成等权分配，但是不会
    df_allocate = fund_allocate(securities, portfolio_value, method, nowtime_str)
    df_allocate['wi'] = df_allocate['order_value'] / portfolio_value
    df = pd.DataFrame(data_list, columns=['symbol', 'wbk', 'wi', 'nk'])
    df['wi'] = df_allocate['wi']
    df['r_weight'] = df_allocate['wi']

    values = df.values

    for value in values:
        for _, symbols in industry_dict.items():
            if len(symbols) > 1:
                symbol_list_tmp = filter(lambda x:x != value[0], symbols) if value[0] in symbols else []
                for symbol_t in symbol_list_tmp:
                    for value_t in values:
                        if value_t[0] == symbol_t:
                            value[4] = value[4] + value_t[2]
                            break
            else:
                continue

    df = pd.DataFrame(values, columns=['symbol', 'wbk', 'wi', 'nk', 'r_weight'])
    df['order_value'] = df['wbk'] * df['wi'] / df['r_weight'] * portfolio_value

    return df[['symbol', 'order_value']]


# 简单长度划分,返回index_s,index_e
def length_split(length, group_num, num):
    if length == 0 or group_num == 0:
        return 0, 0

    return (num - 1) * int(length / group_num), num * int(length / group_num) if num != group_num else length

# 获取下一个需要调仓的日期
def get_next_date(current_date, context):
    current_date = pd.Timestamp(current_date).normalize()
    date_index = get_all_trade_days()
    trade_date = date_index[date_index.searchsorted(current_date, side='left') + context.cycle]
    return trade_date

def init(context):
    # 初始化参数
    context.cycle_flag = True
    # 下一个要交易的日期
    context.next_date = None
    context.cycle = 5       # 调仓周期
    context.num = 1          # 持仓组别
    context.group_num = 3    # 因子分组
    context.index_code = "000300.SH"    # 股票池#这里要改成Excel数据
    context.stock_benchmark = "000001.SH"   # 基准指数#这里也要改成Excel
    context.exclude_st = False                 #这里想改成True，停盘时不交易
    context.group_consider_industry = ""   # 持仓股行业覆盖
    context.fund_consider_industry = ""     # 按行业进行资金分配
    context.fund_allocate = "equal_weight"  # 资金分配
    context.clean_ty = "triple_deviation-standardize"   # 极值处理 + 标准化处理
    context.sys_query = query(factor.symbol, factor.vstd)  # 已选系统因子
    context.sys_sort = []                # 系统因子排序
    context.sys_factors = {'vstd': 1.00}   # 因子比率
    context.user_query = ""   # 用户因子筛选条件#这里想知道，如何改成只要两头，不要中间
    context.user_sort = []              # 用户因子排序
    context.user_factors = {}    # 用户因子比率
    context.stock_hold_count = 10                # 持仓数量#这里想改成按资金比例持仓
    context.trade_days = get_all_trade_days()
    context.buy_failed_symbols = dict()
    context.sell_failed_symbols = dict()
    context.empty_failed_symbols = list()
    # 1. 设置基准
    set_benchmark("000001.SH")                # 基准指数
    # 调用get_iwencai选股
    get_iwencai(context.index_code)

def handle_bar(context, bar_dict):
    try:
        # 2. 遇到调仓日进行调仓
        current_date = pd.Timestamp(get_datetime()).normalize()

        if context.cycle_flag or current_date == context.next_date:
            # 每次调仓之前上次买入失败的股票数据清除
            context.buy_failed_symbols = dict()
            context.sell_failed_symbols = dict()
            context.empty_failed_symbols = list()
            nowtime_str = get_last_datetime().strftime("%Y-%m-%d")
            context.securities = []
            # 3. 从股票池获取所有股票
            context.index_stocks = get_index_stocks(context.index_code, current_date.strftime("%Y%m%d"))
            if not context.index_stocks:
                context.index_stocks = context.iwencai_securities
            if not context.index_stocks:
                log.info('股票池设置有误，请重新设置')
            # 4. 排除ST股
            if context.exclude_st:
                context.index_stocks = [key for key in context.index_stocks if not bar_dict[key].is_st]
            # 5. 分组是否考虑行业
            if context.group_consider_industry:
                symbols_industry = dict()
                for symbol in context.index_stocks:
                    industry = get_symbol_industry(symbol, nowtime_str)
                    if industry is None:
                        continue
                    industry_id = getattr(industry, context.group_consider_industry)

                    if industry_id in symbols_industry:
                        symbols_industry[industry_id].append(symbol)
                    else:
                        symbols_industry[industry_id] = [symbol]
                for industry, symbols in symbols_industry.items():
                    # 根据因子筛选股票
                    securities_df = sfactor_stock_scanner(
                        symbols,
                        context.sys_query,
                        context.sys_sort,
                        context.sys_factors,
                        context.user_query,
                        context.user_sort,
                        context.user_factors,
                        nowtime_str,
                        context.clean_ty,
                    )
                    # 分组返回
                    if len(securities_df):
                        index_s, index_e = length_split(len(securities_df), context.group_num, context.num)
                        context.securities.extend(list(securities_df.iloc[index_s:index_e]['symbol']))
            else:
                # 6. 根据因子筛选股票 #这里想改成只要前十支股票
#sfactor_stock_scanner
                securities_df = sfactor_stock_scanner(
                    context.index_stocks,
                    context.sys_query,
                    context.sys_sort,
                    context.sys_factors,
                    context.user_query,
                    context.user_sort,
                    context.user_factors,
                    nowtime_str,
                    context.clean_ty,
                )
                # 7. 分组返回
                if len(securities_df):
                    index_s, index_e = length_split(len(securities_df), context.group_num, context.num)
                    context.securities = list(securities_df.iloc[index_s:index_e]['symbol'])
            if not len(context.securities):
                log.info("因子回测在调仓日(" + nowtime_str + ")筛选后股票池为空.")
                context.next_date = get_next_date(current_date, context)
            #根据设置来限制买入股票数
            context.securities = context.securities[:context.stock_hold_count]
            #这是我自己加的,想替换上一条买入的指令
            #context.securities=order_percent(context,10,price=None)

            # 原有股票不在股票池中则卖空
            sell_symbols = set(context.portfolio.positions).difference(set(context.securities))

            for symbol in sell_symbols:
                if order_target_value(symbol, 0) is None:
                    context.empty_failed_symbols.append(symbol)

            reduce_stock_dict = dict()
            add_stock_dict = dict()
            # 获取每支股票下单量#想改成根据资金比例下单
            if context.fund_consider_industry:
                # 9. 组内资金分配考虑行业
                order_symbols_df = industry_neutral(context.securities, context.portfolio.portfolio_value, nowtime_str, bar_dict, context.fund_allocate, context.stock_benchmark,                   industryid=context.fund_consider_industry)
            else:
                # 8. 每组资金分配#每组资金分配10%
                order_symbols_df = fund_allocate(context.securities, context.portfolio.portfolio_value, context.fund_allocate, nowtime_str)
            order_symbols_df = order_symbols_df.dropna()

            for _, item in order_symbols_df.iterrows():
                symbol = item['symbol']
                # 先卖后买逻辑
                if symbol in context.portfolio.positions and context.portfolio.positions[symbol].amount > int(item['order_value']  / bar_dict[symbol].open / 100) * 100:
                    reduce_stock_dict[item['symbol']] = item['order_value']
                else:
                    add_stock_dict[item['symbol']] = item['order_value']

            for key, value in reduce_stock_dict.items():
                if order_target_value(key, value) is None:
                    context.sell_failed_symbols[key] = value
            for key, value in add_stock_dict.items():
                if order_target_value(key, value) is None:
                    context.buy_failed_symbols[key] = value
            context.next_date = get_next_date(current_date, context)
    except:
        pass
    finally:
        context.cycle_flag = False
        empty_symbols = copy.copy(context.empty_failed_symbols)
        sell_symbols = copy.copy(context.sell_failed_symbols)
        buy_symbols = copy.copy(context.buy_failed_symbols)

        for symbol in empty_symbols:
            if order_target_value(symbol, 0) is not None:
                context.empty_failed_symbols.remove(symbol)
        for symbol, value in sell_symbols.items():
            if order_target_value(symbol, value) is not None:
                del context.sell_failed_symbols[symbol]
        for symbol, value in buy_symbols.items():
            if order_target_value(symbol, value) is not None:
                del context.buy_failed_symbols[symbol]
