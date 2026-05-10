# 量化金融工具与资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，量化交易的门槛已经下放到个人开发者。
> - **Python 为王**：虽然 Rust (Polars) 和 Julia 在性能上占优，但 Python 拥有最成熟的生态和 AI 集成能力。
> - **数据即资产**：优先使用 **AkShare** (国内) 和 **yfinance** (出海) 获取免费行情，把省下的钱花在算力和优质信号上。

---

## 🐍 Python 核心生态 (Python Quant Stack)

### 基础数值与高性能计算
- [ ] [**NumPy / SciPy**](https://numpy.org/) - 科学计算基石，提供高效数组运算与数学模型求解。
- [ ] [**Pandas**](https://pandas.pydata.org/) - 量化数据分析的“瑞士军刀”，处理时间序列的标准工具。
- [ ] [**Polars**](https://docs.pola.rs/) - **2026 推荐**。基于 Rust 的高性能 DataFrame，处理 TB 级数据比 Pandas 快 10-50 倍。
- [ ] [**ArcticDB**](https://github.com/man-group/ArcticDB) - Man Group 开源的 Tick 数据存储，高性能时间序列数据库。

### 金融定价与风险模型
- [ ] [**OpenBB SDK**](https://github.com/OpenBB-finance/OpenBB) - 开源金融终端，支持股票、期权、加密货币的一站式定价与分析。
- [ ] [**gs-quant**](https://github.com/goldmansachs/gs-quant) - 高盛开源的专业工具包，包含顶级投行的定价逻辑。
- [ ] [**FinancePy**](https://github.com/domokane/FinancePy) - 专注于衍生品定价，涵盖期权、债券与利率互换。

### 策略回测与实盘交易
- [ ] [**VectorBT**](https://vectorbt.dev/) - 基于向量化运算的极速回测库，支持复杂参数优化。
- [ ] [**Qlib**](https://github.com/microsoft/qlib) - 微软开源，集成 AI/ML 因子工程与全生命周期量化平台。
- [ ] [**Freqtrade**](https://github.com/freqtrade/freqtrade) - 2026 年最强加密货币开源交易机器人，支持回测与实盘部署。
- [ ] [**FinRL**](https://github.com/AI4Finance-LLC/FinRL-Library) - 专注于强化学习 (RL) 的交易策略框架。

---

## 📈 数据获取与分析 (Data & Analysis)

- [ ] [**AkShare**](https://github.com/jindaxiang/akshare) - **国内首选**。完全免费的 A 股、期货、宏观数据接口库。
- [ ] [**yfinance**](https://github.com/ranaroussi/yfinance) - **出海标配**。通过 Yahoo Finance 获取全球股票与加密货币数据。
- [ ] [**Pandas TA**](https://github.com/twopirllc/pandas-ta) - 集成 100+ 技术指标，与 Pandas 无缝配合。
- [ ] [**PyPortfolioOpt**](https://github.com/robertmartin8/PyPortfolioOpt) - 投资组合优化，支持马科维茨有效前沿与风险平价。

---

## 📊 可视化与工具 (Visualization & Utilities)

- [ ] [**Finplot**](https://github.com/highfestiva/finplot) - 高性能绘图，流畅缩放百万级 K 线数据。
- [ ] [**xlwings**](https://www.xlwings.org/) - 连接 Python 与 Excel 的桥梁，满足传统分析习惯。
- [ ] [**CCXT**](https://github.com/ccxt/ccxt) - **必选**。统一连接全球 100+ 加密货币交易所的 JavaScript/Python 库。

---

## 🎓 学习与前沿 (Learning)

- [ ] [**Python for Finance (Yves Hilpisch)**](https://github.com/yhilpisch/py4fi2nd) - 行业入门经典，含全套代码实现。
- [ ] [**Tidy Finance**](https://www.tidy-finance.org/) - 提供可复现的金融研究方法与代码示例。
- [ ] [**J.P. Morgan Python Training**](https://github.com/jpmorganchase/python-training) - 顶级投行内部培训级别的实战课程。

---

## 💡 选型建议
1. **初学者入门**：选 **Backtesting.py** (回测) + **yfinance** (数据)。
2. **构建 AI 交易系统**：选 **Qlib** (因子) + **FinRL** (模型)。
3. **高频加密货币套利**：选 **CCXT** + **Freqtrade**。
4. **处理海量 A 股行情**：选 **AkShare** + **Polars**。
