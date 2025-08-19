# Next.js + TypeScript 项目快速搭建指南

## 什么是 Next.js？
Next.js 是一个基于 React 的前端框架，支持服务端渲染、静态站点生成等功能，非常适合构建高性能的现代 web 应用。本指南将帮助你快速创建一个带有 TypeScript 的 Next.js 项目。

## 准备工作
在开始之前，请确保你的电脑上已经安装了：
- Node.js（推荐 v18 及以上版本）
- npm（通常随 Node.js 一起安装）

你可以通过以下命令检查是否已安装：
```bash
node -v  # 查看 Node.js 版本
npm -v   # 查看 npm 版本
```

## 项目初始化步骤

### 1. 创建 Next.js 项目（带 TypeScript）
打开终端，运行以下命令创建一个新的 Next.js 项目，并自动配置 TypeScript：

```bash
npx create-next-app@latest my-next-app --typescript
```

执行命令后，系统会提示你进行一些配置选择（如是否使用 ESLint、Tailwind CSS 等），根据你的需求选择即可，新手建议直接按回车选择默认选项。

### 2. 进入项目目录
创建完成后，进入刚刚创建的项目文件夹：

```bash
cd my-next-app
```

### 3. 启动本地开发服务器
运行以下命令启动开发服务器：

```bash
npm run dev
```

启动成功后，你会看到类似以下的提示：
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

此时，打开浏览器访问 `http://localhost:3000` 就能看到你的 Next.js 应用了！

## 后续操作建议

- 编辑 `pages/index.tsx` 文件可以修改首页内容
- 查看 [Next.js 官方文档](https://nextjs.org/docs) 学习更多功能
- 需要部署时，可以考虑使用 Vercel（Next.js 官方推荐的部署平台）

## 技术关键词
Next.js, TypeScript, 前端框架, React, 项目搭建, 开发环境配置, 前端开发

通过以上步骤，你可以在几分钟内搭建好一个功能完善的 Next.js 开发环境，开始你的前端项目开发之旅！