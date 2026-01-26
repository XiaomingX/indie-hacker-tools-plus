# Awesome-Quant：精选量化金融工具与资源库
一个经过精心筛选的量化金融（Quantitative Finance）核心工具库、资源包与学习资料清单，聚焦**活跃维护、功能实用、社区成熟**的项目，按工具用途与编程语言分类，便于快速查找与使用。


## Python：量化金融第一生态
Python是量化领域的主流语言，生态完善且工具迭代迅速。以下按核心功能分类，标注「🔥 核心推荐」的工具为行业常用选型。


### 一、基础数值计算与数据结构
量化分析的底层工具，负责数据存储、数值运算与数学建模。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 numpy | [numpy.org](https://www.numpy.org) | Python科学计算基石，提供高效多维数组（ndarray）与向量运算，支撑所有量化库的数值计算 |
| 🔥 scipy | [scipy.org](https://www.scipy.org) | 基于NumPy的扩展，包含线性代数、积分、优化、信号处理等工具，常用于金融模型求解（如波动率计算） |
| 🔥 pandas | [pandas.pydata.org](https://pandas.pydata.org) | 量化数据分析「瑞士军刀」，提供DataFrame数据结构，支持时间序列处理、缺失值填充、分组统计等核心操作 |
| 🔥 polars | [docs.pola.rs](https://docs.pola.rs/) | 新一代高性能DataFrame库，基于Rust实现，速度远超pandas，适合TB级大规模金融数据处理 |
| sympy | [sympy.org](https://www.sympy.org/) | 符号数学库，可推导金融公式（如期权定价公式）、求解代数方程，无需手动计算解析解 |
| 🔥 pymc | [pymc.io](https://www.pymc.io) | 现代概率编程库（替代老旧的pymc3），基于PyTensor，用于贝叶斯建模（如风险因子的概率推断） |
| ArcticDB | [github.com/man-group/ArcticDB](https://github.com/man-group/ArcticDB) | 专用于时间序列与Tick数据的存储库，支持高并发读写，常被对冲基金用于行情数据落地 |
| modelx | [docs.modelx.io](https://docs.modelx.io/) | 将Excel表格逻辑转化为Python对象，适合习惯用Excel建模的分析师迁移至代码环境 |


### 二、金融工具定价与估值
专注于股票、债券、衍生品等金融资产的定价模型实现。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 OpenBB SDK | [github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | 替代原OpenBB Terminal的开发级工具，支持股票/期权/加密货币定价、风险分析与数据获取 |
| 🔥 FinancePy | [github.com/domokane/FinancePy](https://github.com/domokane/FinancePy) | 轻量化衍生品定价库，覆盖欧式/美式期权、债券、利率互换，文档详尽，适合新手学习 |
| 🔥 gs-quant | [github.com/goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | 高盛开源的专业工具包，支持固定收益、信贷、外汇等资产定价，内置成熟的风险模型 |
| vollib | [github.com/vollib/vollib](https://github.com/vollib/vollib) | 期权定价专用库，实现Black-Scholes、Binomial Tree等模型，可直接计算希腊字母（Delta/Gamma） |
| pysabr | [github.com/ynouri/pysabr](https://github.com/ynouri/pysabr) | 实现SABR波动率模型（用于利率衍生品定价），支持市场数据标定与风险参数计算 |
| rateslib | [github.com/attack68/rateslib](https://github.com/attack68/rateslib) | 固定收益领域专用，支持债券、债券期货、利率远期的定价与久期/凸性计算 |
| fypy | [github.com/jkirkby3/fypy](https://github.com/jkirkby3/fypy) | 覆盖常规与奇异期权（如障碍期权、亚洲期权），支持多种波动率模型的市场标定 |
| AbsBox | [github.com/yellowbean/AbsBox](https://github.com/yellowbean/AbsBox) | 专用于资产支持证券（ABS）、按揭支持证券（MBS）的现金流建模与估值 |


### 三、技术指标与因子分析
量化策略的核心组件，负责从行情数据中提取交易信号或风险因子。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 Pandas TA | [github.com/twopirllc/pandas-ta](https://github.com/twopirllc/pandas-ta) | 最活跃的技术指标库，支持115+指标（MA、RSI、MACD、布林带等），无缝集成pandas |
| 🔥 talib | [github.com/mrjbq7/ta-lib](https://github.com/mrjbq7/ta-lib) | 经典技术指标库的Python绑定，机构常用，支持批量计算与向量优化 |
| talipp | [github.com/nardew/talipp](https://github.com/nardew/talipp) | 增量式指标库，适合实时行情流（如Tick数据）中动态更新指标，低延迟 |
| 🔥 alphalens-reloaded | [github.com/stefan-jansen/alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded) | 因子绩效分析工具，可回测因子的收益率、IC值（信息系数）、换手率等关键指标 |
| Spectre | [github.com/Heerozh/spectre](https://github.com/Heerozh/spectre) | GPU加速的因子计算库，支持千万级股票池的因子批量生成，适合高频因子研究 |
| lppls | [github.com/Boulder-Investment-Technologies/lppls](https://github.com/Boulder-Investment-Technologies/lppls) | 实现LPPLS模型，用于识别资产价格的泡沫与崩盘信号（如加密货币、股票指数） |


### 四、策略回测与交易执行
从策略研发（回测）到实盘交易的全流程工具，核心关注「回测真实性」与「实盘兼容性」。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 VectorBT | [vectorbt.dev](https://vectorbt.dev) | 新一代回测库，基于NumPy/Pandas加速，支持参数优化、多策略对比，可对接实盘API |
| 🔥 Backtesting.py | [kernc.github.io/backtesting.py](https://kernc.github.io/backtesting.py/) | 轻量级回测工具，API简洁，自带可视化界面，适合快速验证技术分析策略（如均线交叉） |
| 🔥 Blankly | [github.com/Blankly-Finance/Blankly](https://github.com/Blankly-Finance/Blankly) | 全流程平台，支持回测、模拟交易、实盘部署（对接Binance、Coinbase等），适合加密货币策略 |
| 🔥 zipline-reloaded | [github.com/stefan-jansen/zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) | 经典Zipline的维护版本，兼容Quantopian的策略代码，支持A股/美股数据 |
| 🔥 freqtrade | [github.com/freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | 开源加密货币交易机器人，支持回测、实盘、止损止盈，社区插件丰富 |
| 🔥 Qlib | [github.com/microsoft/qlib](https://github.com/microsoft/qlib) | 微软开源的量化平台，集成数据获取、因子工程、模型训练（ML）、回测的全流程 |
| FinRL-Library | [github.com/AI4Finance-LLC/FinRL-Library](https://github.com/AI4Finance-LLC/FinRL-Library) | 基于强化学习（RL）的交易策略库，内置股票/加密货币环境，可快速训练RL智能体 |
| alpaca-trade-api | [github.com/alpacahq/alpaca-trade-api-python](https://github.com/alpacahq/alpaca-trade-api-python) | 对接Alpaca经纪商，支持美股实时行情获取与实盘交易，适合算法交易部署 |


### 五、投资组合优化与风险分析
专注于资产配置、风险度量与组合绩效评估。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 PyPortfolioOpt | [github.com/robertmartin8/PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | 最流行的组合优化库，支持有效前沿、最大夏普比、风险平价等经典模型 |
| 🔥 riskparity.py | [github.com/dppalomar/riskparity.py](https://github.com/dppalomar/riskparity.py) | 风险平价组合专用工具，基于TensorFlow加速，适合大类资产配置 |
| 🔥 pyfolio-reloaded | [github.com/stefan-jansen/pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) | 组合绩效分析工具，可计算最大回撤、夏普比、Calmar比率，生成专业绩效报告 |
| empyrical-reloaded | [github.com/stefan-jansen/empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded) | 金融绩效指标计算库，支持年化收益、波动率、下行风险等核心指标 |
| Riskfolio-Lib | [github.com/dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | 进阶组合优化工具，支持条件风险价值（CVaR）、熵池优化等高级模型 |
| Kelly-Criterion | [github.com/deltaray-io/kelly-criterion](https://github.com/deltaray-io/kelly-criterion) | 实现凯利准则，用于计算最优仓位大小（控制风险与收益的平衡） |


### 六、时间序列分析与预测
量化中用于价格预测、波动率建模的核心技术栈。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 statsmodels | [statsmodels.org](https://www.statsmodels.org) | 经典时间序列库，支持ARIMA、VAR、GARCH等模型，用于趋势预测与波动率建模 |
| 🔥 Facebook Prophet | [github.com/facebook/prophet](https://github.com/facebook/prophet) | 轻量级预测工具，自动处理节假日、多季节性，适合非专业人士快速生成价格预测 |
| 🔥 ARCH | [github.com/bashtage/arch](https://github.com/bashtage/arch) | 专注于异方差模型（如GARCH、EGARCH），用于股票/加密货币波动率预测 |
| pmdarima | [github.com/alkaline-ml/pmdarima](https://github.com/alkaline-ml/pmdarima) | 自动优化ARIMA模型参数（替代R的auto.arima），减少调参工作量 |
| functime | [github.com/functime-org/functime](https://github.com/functime-org/functime) | 基于Polars的大规模时间序列工具，支持千万级数据的特征提取与预测 |
| tsmoothie | [github.com/cerlymarco/tsmoothie](https://github.com/cerlymarco/tsmoothie) | 时间序列平滑与异常值检测，可识别行情中的突发波动（如闪崩） |


### 七、数据来源：行情与基本面数据
量化分析的「原料」，优先选择**免费、稳定、接口友好**的工具。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 yfinance | [github.com/ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) | 最流行的免费数据工具，抓取Yahoo Finance的股票/ETF/加密货币行情与基本面数据 |
| 🔥 akshare | [github.com/jindaxiang/akshare](https://github.com/jindaxiang/akshare) | 国内最好用的金融数据接口，支持A股、期货、基金、宏观数据，完全免费 |
| pandas-datareader | [github.com/pydata/pandas-datareader](https://github.com/pydata/pandas-datareader) | 对接FRED（宏观数据）、IEX Cloud（美股）等数据源，与pandas无缝集成 |
| tiingo | [github.com/hydrosquall/tiingo-python](https://github.com/hydrosquall/tiingo-python) | 专业数据源接口，提供高质量OHLCV数据与新闻，适合机构级研究（部分免费） |
| investpy | [github.com/alvarobartt/investpy](https://github.com/alvarobartt/investpy) | 抓取Investing.com的数据，支持全球股票、债券、商品，无需API密钥 |
| pytdx | [github.com/rainx/pytdx](https://github.com/rainx/pytdx) | 对接通达信行情接口，获取A股实时Tick数据与历史行情，适合国内实盘辅助 |


### 八、数据可视化与Excel集成
将量化结果转化为直观图表，或对接Excel生态（满足传统分析师需求）。

| 工具名称 | 链接 | 核心优势与用途 |
|----------|------|----------------|
| 🔥 mplfinance | [github.com/matplotlib/mplfinance](https://github.com/matplotlib/mplfinance) | 金融图表专用库，支持K线图、成交量、均线叠加，可生成专业交易图表 |
| 🔥 finplot | [github.com/highfestiva/finplot](https://github.com/highfestiva/finplot) | 高性能金融绘图工具，支持百万级数据的流畅缩放，适合高频行情可视化 |
| D-Tale | [github.com/man-group/dtale](https://github.com/man-group/dtale) | 交互式数据探索工具，可在浏览器中查看DataFrame、生成统计图表，支持数据清洗 |
| 🔥 xlwings | [xlwings.org](https://www.xlwings.org/) | 最成熟的Python-Excel桥梁，支持在Excel中调用Python函数，或用Python读写Excel |
| openpyxl | [openpyxl.readthedocs.io](https://openpyxl.readthedocs.io/) | 纯Python实现的Excel读写库，支持.xlsx/.xlsm格式，无需依赖Office |


## 其他主流语言工具
除Python外，R、Julia等语言在特定场景（如统计建模、高性能计算）中更具优势。


### R语言：统计建模与金融分析
R在统计推断与因子分析中应用广泛，适合学术研究与低频策略。

| 分类 | 工具名称 | 核心用途 |
|------|----------|----------|
| 数据结构 | 🔥 xts/zoo | 时间序列数据处理的核心库，支持不规则时间索引 |
| 数据结构 | 🔥 data.table | 高性能数据框，适合大规模金融数据的聚合与排序 |
| 金融建模 | 🔥 quantmod | 量化金融基础框架，支持数据获取、技术指标、绘图 |
| 衍生品定价 | RQuantLib | 对接QuantLib，实现期权、债券定价 |
| 回测 | 🔥 quantstrat | 专业回测框架，支持多资产、多策略组合 |
| 风险分析 | 🔥 PerformanceAnalytics | 组合绩效与风险指标计算（如夏普比、最大回撤） |
| 时间序列 | 🔥 rugarch/rmgarch | 单变量/多变量GARCH模型，用于波动率建模 |


### Julia语言：高性能量化计算
Julia兼顾Python的易用性与C++的速度，适合高频交易与复杂模型。

| 工具名称 | 核心用途 |
|----------|----------|
| 🔥 DataFrames.jl | 数据框处理，类似pandas |
| 🔥 TimeSeries.jl | 时间序列数据结构与操作 |
| QuantLib.jl | 衍生品定价与风险管理 |
| MarketTechnicals.jl | 技术指标计算（MA、RSI等） |
| Strategems.jl | 策略回测与交易系统开发 |
| YieldCurve.jl | 固定收益工具的收益率曲线建模 |


### 其他语言工具
| 语言 | 工具名称 | 核心用途 |
|------|----------|----------|
| Java | Strata | 机构级市场风险与分析库 |
| JavaScript | 🔥 ccxt | 对接100+加密货币交易所，支持实盘交易 |
| JavaScript | Ghostfolio | 个人资产追踪与投资分析工具 |
| Julia | Ito.jl | 随机微积分与量化金融建模 |


## 量化学习与实践资源
### 经典书籍与代码实现
- **《Python for Finance》（Yves Hilpisch）**：[py4fi2nd](https://github.com/yhilpisch/py4fi2nd) - 书中代码与Jupyter笔记本，涵盖衍生品定价、组合优化。
- **《金融机器学习进展》**：[mlfinlab](https://github.com/hudson-and-thames/mlfinlab) - 书中核心算法实现（如元标记、特征重要性）。
- **《资产管理的机器学习》**：[Machine-Learning-for-Asset-Managers](https://github.com/emoen/Machine-Learning-for-Asset-Managers) - 基于实时数据的代码示例。

### 实战项目与课程
- **J.P. Morgan Python培训**：[github.com/jpmorganchase/python-training](https://github.com/jpmorganchase/python-training) - 投行级Python量化实战课程。
- **量化金融证书（CQF）资料**：[JoaoJungblut/QuantFinanceTraining](https://github.com/JoaoJungblut/QuantFinanceTraining) - CQF课程代码整理，涵盖衍生品定价与风险。
- **Tidy Finance**：[tidy-finance.org](https://www.tidy-finance.org/) - 可复现的金融研究方法，提供Python/R代码。

### 学术与前沿资源
- **差分机器学习**：[differential-machine-learning/notebooks](https://github.com/differential-machine-learning/notebooks) - 金融风险建模的前沿方法实现。
- **粗糙Bergomi模型**：[ryanmccrickerd/rough_bergomi](https://github.com/ryanmccrickerd/rough_bergomi) - 波动率建模的学术热点代码。
