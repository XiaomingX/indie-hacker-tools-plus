# FastAPI 最佳实践与资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，FastAPI 是 Python 后端的绝对统治者。
> - **异步优先**：确保你的数据库驱动和外部请求都是异步的 (async/await)，否则将无法发挥 FastAPI 的高并发优势。
> - **Pydantic V2**：充分利用 Pydantic V2 的性能提升和模型验证能力。
> - **依赖注入**：将业务逻辑从路由处理器中抽离，通过依赖注入实现可测试、可扩展的代码。

---

## 🏗️ 核心框架与基础 (Core)

- [ ] [**FastAPI**](https://github.com/tiangolo/fastapi) - 高性能 Python ASGI 框架，2026 年依然是首选。
- [ ] [**Starlette**](https://github.com/encode/starlette) - FastAPI 的底层，如果你需要极简、极高性能的异步服务，可直接使用。
- [ ] [**uv**](https://github.com/astral-sh/uv) - **2026 推荐**。用 uv 管理你的 Python 环境与依赖，速度比 pip/poetry 快一个量级。
- [ ] [**Uvicorn / Granian**](https://github.com/emmett-framework/granian) - 高性能 ASGI 服务器。Granian 是 2026 年更快的 Rust 替代方案。

---

## 🛠️ 管理后台 (Admin Panels)

- [ ] [**SQLAdmin**](https://github.com/aminalaee/sqladmin) - 基于 SQLAlchemy 的异步管理后台，功能成熟且活跃。
- [ ] [**FastAPI AMIS Admin**](https://github.com/amisadmin/fastapi_amis_admin) - 结合百度 AMIS 前端，通过 JSON 即可生成极其复杂的后台界面。
- [ ] [**Piccolo Admin**](https://github.com/piccolo-orm/piccolo_admin) - 轻量且现代化的数据库管理后台。

---

## 📂 数据库与 ORM (Databases & ORM)

- [ ] [**SQLAlchemy (2.0+)**](https://github.com/sqlalchemy/sqlalchemy) - 工业级标准，支持完整的异步操作。
- [ ] [**Tortoise ORM**](https://github.com/tortoise/tortoise-orm) - 语法类似 Django ORM 的异步 ORM，非常适合中小型项目。
- [ ] [**Prisma for Python**](https://github.com/RobertCraigie/prisma-client-py) - 强类型的 ORM 体验，生成代码非常优雅。
- [ ] [**Beanie**](https://github.com/roman-right/beanie) - 针对 MongoDB 的异步 ODM，完美适配 Pydantic。

---

## ⚡ 性能提升与扩展 (Performance & Extensions)

- [ ] [**FastAPI Cache**](https://github.com/long2ice/fastapi-cache) - 简单好用的函数级/装饰器级缓存，支持 Redis/Memcached。
- [ ] [**SlowAPI**](https://github.com/laurentS/slowapi) - 基于限流器，保护你的 API 免受滥用。
- [ ] [**FastAPI Events**](https://github.com/melvinkcx/fastapi-events) - 优雅地处理异步事件订阅与发布。
- [ ] [**Loguru**](https://github.com/Delgan/loguru) - 现代、易用的日志管理，替代 Python 标准库日志。

---

## 🚀 项目模板与部署 (Boilerplates & Deployment)

- [ ] [**Full Stack FastAPI PostgreSQL**](https://github.com/tiangolo/full-stack-fastapi-postgresql) - 官方出品的全栈模板（Next.js + FastAPI）。
- [ ] [**FastAPI Best Practices Repo**](https://github.com/zhanymkanov/fastapi-best-practices) - 值得反复阅读的项目结构与代码风格指南。
- [ ] [**Pydantic to TypeScript**](https://github.com/phillipdupuis/pydantic-to-typescript) - 自动同步前后端类型定义。

---

## 💡 选型建议
1. **企业级复杂业务**：选 **SQLAlchemy** + **Alembic** + **SQLAdmin**。
2. **AI 原生应用**：选 **FastAPI** + **Pydantic V2** + **uv** 环境管理。
3. **极速验证 MVP**：选 **Tortoise ORM** + **FastAPI Admin**。
4. **地理信息系统 (GIS)**：选 **TiTiler** 基于 FastAPI 的地图瓦片服务。