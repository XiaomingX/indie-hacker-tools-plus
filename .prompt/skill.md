# Skills: 创业导师工具箱

## skill: analyze_yc_logic
**Description**: 分析文章是否符合 YC 的核心价值观。
**Parameters**:
- focus_points: ["用户痛点是否真实", "是否过早扩张", "产品是否简单可行"]
**Operation**: 
- 检查文章是否在推崇“闭门造车”。如果是，标记为“高风险”。
- 评估文章是否强调了“与用户沟通”的重要性。

## skill: tech_stack_audit (AI Focus)
**Description**: 针对独立开发者文章，评估技术路径的现实性。
**Operation**:
- 识别文中提到的 AI 架构（如 RAG, Agentic Workflow）。
- 判断该方案对于“独立开发者”是否过重，建议更轻量级的替代方案。

## skill: iterative_update
**Description**: 根据当前科技时事（如 OpenAI 发布的最新 API 或市场趋势）更新旧文。
**Operation**:
- 识别文章中过时的技术名词或过时的市场假设。
- 自动生成补充段落，标记为 [2026 Update]。

## skill: style_polishing
**Description**: 调整文风为“启发式”而非“说教式”。
**Operation**:
- 将“你应该...”改为“在 YC，我们观察到最成功的创始人通常会...”。
- 增加反问句，引发读者思考。