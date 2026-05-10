# GitHub Actions 自动化工作流精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，GitHub Actions 已成为独立开发者的 **"数字员工"**。
> - **CI/CD 提速**：必须利用 `actions/cache` 缓存依赖，否则每次构建都是在浪费生命（和额度）。
> - **AI 评审**：集成 AI Code Reviewer，让大模型在你合并代码前先帮你把关，减少低级 Bug。
> - **本地调试**：使用 `nektos/act` 在本地运行 Actions，避免为了调试一个工作流而反复 Push 代码。

---

## 🏗️ 官方核心工具 (Core Actions)

- [ ] [**actions/checkout**](https://github.com/actions/checkout) - **[必备]** 拉取仓库代码到运行环境，几乎所有工作流的第一步。
- [ ] [**actions/setup-node**](https://github.com/actions/setup-node) - 配置 Node.js 环境，内置高效的 npm/yarn/pnpm 缓存支持。
- [ ] [**actions/cache**](https://github.com/actions/cache) - 缓存依赖和构建产物，极大缩短后续运行时间。
- [ ] [**actions/upload-artifact**](https://github.com/actions/upload-artifact) - 保存构建产物（如编译后的二进制文件、测试报告）。
- [ ] [**actions/github-script**](https://github.com/actions/github-script) - 在工作流中直接运行 JS 代码调用 GitHub API。

---

## 🚀 部署与发布 (Deployment & Release)

- [ ] [**softprops/action-gh-release**](https://github.com/softprops/action-gh-release) - 自动创建 GitHub Release 并上传附件。
- [ ] [**peaceiris/actions-gh-pages**](https://github.com/peaceiris/actions-gh-pages) - 快速部署静态网站（Next.js, Astro, Hugo）到 GitHub Pages。
- [ ] [**docker/build-push-action**](https://github.com/docker/build-push-action) - 构建并推送 Docker 镜像，支持多平台架构。
- [ ] [**appleboy/ssh-action**](https://github.com/appleboy/ssh-action) - 通过 SSH 远程执行命令，适合传统的 VPS 部署方案。

---

## 🛡️ 安全与质量审计 (Security & Quality)

- [ ] [**reviewdog/action-eslint**](https://github.com/reviewdog/action-eslint) - 在 PR 中直接标注 ESLint 错误，提升代码审核效率。
- [ ] [**aquasecurity/trivy-action**](https://github.com/aquasecurity/trivy-action) - 扫描镜像和文件中的漏洞，确保交付物安全。
- [ ] [**trufflesecurity/trufflehog**](https://github.com/trufflesecurity/trufflehog) - 扫描仓库中的敏感信息泄露（Key, Secret）。

---

## 🤖 2026 AI 增强插件 (AI Actions)

- [ ] [**actions/ai-code-reviewer**](https://github.com/actions/ai-code-reviewer) - 利用 LLM 自动评审代码变更，提供优化建议。
- [ ] [**coderabbitai/ai-pr-reviewer**](https://github.com/coderabbitai/ai-pr-reviewer) - 深度集成的 AI 评审员，擅长发现逻辑漏洞。

---

## 💡 选型建议
1. **前端项目 CI**：`checkout` -> `setup-node` (含缓存) -> `npm install` -> `npm test` -> `upload-artifact`。
2. **静态站点发布**：构建完成后配合 `peaceiris/actions-gh-pages`。
3. **本地调试 Actions**：安装命令行工具 `act`。
4. **自动化 Issue 管理**：使用 `actions/stale` 自动关闭不活跃的任务。
