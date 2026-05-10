# 2026 全球支付与跨境结汇服务指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，跨境支付已经变得极其透明和高效。
> - **合规第一**：对于出海项目，Stripe 和 PayPal 依然是门槛，但如果主体在香港或新加坡，可以解锁更多低成本结汇渠道。
> - **加密货币支付**：2026 年，接受 USDT/USDC 已成为独立开发者的标配，能有效解决高风险地区的支付成功率问题。
> - **费率权衡**：不要只看名义手续费，提现时的汇率损耗（Spread）往往才是大头。

---

## 💳 主流在线支付平台 (Mainstream Payment)

- [ ] [**Stripe**](https://stripe.com/) - **[行业标准]** 最强大的 API 和订阅管理（Billing）系统。支持全球 135+ 种货币。
- [ ] [**PayPal**](https://www.paypal.com/) - 个人用户信誉度最高，虽然费率偏高但转换率极佳。
- [ ] [**Lemonsqueezy**](https://www.lemonsqueezy.com/) - **[推荐]** 作为 Merchant of Record (MoR)，自动处理全球税务（VAT/Sales Tax），极其适合独立开发者。
- [ ] [**Paddle**](https://www.paddle.com/) - 另一款优秀的 MoR 服务，深度集成 SaaS 订阅逻辑。

---

## 🌍 跨境收款与结汇 (Cross-border Collections)

- [ ] [**Wise (原 TransferWise)**](https://wise.com/) - 提供多币种本地银行账户，汇率损耗极低，支持直接结汇至国内支付宝/银行卡。
- [ ] [**Payoneer (派安盈)**](https://www.payoneer.com/) - 适配各大主流电商平台与自由职业者平台。
- [ ] [**Airwallex (空中云汇)**](https://www.airwallex.com/) - 功能强大的全球收付款平台，尤其适合香港/新加坡主体。
- [ ] [**PingPong**](https://www.pingpongx.com/) - 针对中国卖家的跨境收款方案，费率极具竞争力。

---

## 🪙 加密货币支付网关 (Crypto Payments)

- [ ] [**BitPay**](https://bitpay.com/) - 支持将加密货币自动转换为法币存入银行账户。
- [ ] [**Coinbase Commerce**](https://commerce.coinbase.com/) - 简单好用的加密货币收款工具，无托管。
- [ ] [**Triple-A**](https://triple-a.io/) - 合规性极强的加密支付方案，支持结算为本地法币。
- [ ] [**Epusdt**](https://github.com/assimon/epusdt) - 针对个人开发者的开源 USDT 自动收款系统，无中间商。

---

## 💡 选型建议
1. **不想处理复杂的全球税务问题**：强烈建议选 **Lemonsqueezy**。
2. **需要极致的订阅管理与开发者体验**：选 **Stripe**。
3. **资金主要回流国内且金额较大**：配合使用 **Wise** 或 **Airwallex**。
4. **面向 Web3 玩家或高风险内容**：必须部署 **Epusdt** 或集成 **Coinbase Commerce**。
