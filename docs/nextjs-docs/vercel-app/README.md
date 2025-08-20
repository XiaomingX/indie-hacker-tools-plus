# Next.js 项目快速初始化与 Vercel 部署指南

A quick start guide for initializing a Next.js project with TypeScript and deploying it to Vercel.

## 项目初始化 (Next.js + TypeScript)

通过以下命令快速创建一个基于 TypeScript 的 Next.js 新项目，无需手动配置环境：

```bash
# 使用 create-next-app 脚手架创建项目（指定 TypeScript）
npx create-next-app@latest my-next-app --typescript

# 进入项目根目录
cd my-next-app

# 启动本地开发服务器（默认端口：3000）
npm run dev
```

执行完成后，打开浏览器访问 `http://localhost:3000` 即可查看项目运行效果。


## 部署到 Vercel

Vercel 是 Next.js 官方推荐的部署平台，支持 GitHub 仓库自动关联与持续部署，步骤如下：

1. **推送代码到 GitHub 仓库**
   - 在 GitHub 新建一个**私有/公开仓库**（无需初始化 `README` 或 `.gitignore`）。
   - 在本地项目根目录执行 Git 命令，将代码推送到远程仓库：
     ```bash
     git init
     git add .
     git commit -m "Initial commit: Next.js TypeScript project"
     git branch -M main
     git remote add origin https://github.com/你的GitHub用户名/你的仓库名.git
     git push -u origin main
     ```

2. **在 Vercel 部署项目**
   - 访问 [Vercel 官网](https://vercel.com/) 并使用 GitHub 账号登录。
   - 点击页面右上角 **"New Project"**，选择你刚刚创建的 GitHub 仓库。
   - 保持默认部署配置（Vercel 会自动识别 Next.js 项目并配置构建命令），点击 **"Deploy"**。
   - 等待部署完成后，Vercel 会生成一个可访问的在线域名（如 `your-project.vercel.app`）。


## 关键词说明
- **技术栈**：Next.js, TypeScript, Vercel, GitHub
- **核心功能**：项目初始化、本地开发、快速部署、持续集成
- **适用场景**：前端项目快速启动、Next.js 应用原型开发与上线