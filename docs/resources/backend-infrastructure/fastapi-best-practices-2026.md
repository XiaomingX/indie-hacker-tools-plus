# FastAPI 最佳实践笔记（2026年最新）

## 管理后台（Admin）

- [fastapi-admin](https://github.com/fastapi-admin/fastapi-admin) :star: 3400+ :fork_and_knife: 420+  
  基于 FastAPI 和 TortoiseORM 结合 Tabler UI 的管理后台，灵感源自 Django Admin。近期有更新，支持 Redis、MySQL、PostgreSQL。

- [sqladmin](https://github.com/aminalaee/sqladmin) :star: 700+ :fork_and_knife: 90+  
  基于 SQLAlchemy, FastAPI 和 Starlette 的现代异步管理后台，功能丰富且活跃，适合大多数生产环境。

- [fastapi_amis_admin](https://github.com/amisadmin/fastapi_amis_admin) :star: 400+ :fork_and_knife: 40+  
  高性能且易扩展的管理后台，结合阿里巴巴 AMIS 前端框架，界面美观且功能强大。

- [piccolo_admin](https://github.com/piccolo-orm/piccolo_admin) :star: 200+ :fork_and_knife: 30+  
  轻量且强大的数据库管理后台，支持多种数据库，适合轻量项目的后台需求。

- [vue-element-admin-fastapi](https://github.com/heyfavour/vue-element-admin-fastapi) :star: 160+ :fork_and_knife: 30+  
  前端基于 vue-element-admin，后端采用FastAPI + PostgreSQL 的全栈解决方案。

***

## API 相关

- [fastapi-crudrouter](https://github.com/awtkns/fastapi-crudrouter) :star: 900+ :fork_and_knife: 110+  
  自动为模型生成 CRUD 路由，极大提升 API 开发效率。

- [titiler](https://github.com/developmentseed/titiler) :star: 320+ :fork_and_knife: 90+  
  动态光栅地图瓦片服务构建工具，适合地理信息系统 (GIS) 相关应用。

- [fastapi-gino-arq-uvicorn](https://github.com/leosussan/fastapi-gino-arq-uvicorn) :star: 320+ :fork_and_knife: 40+  
  结合 GINO ORM、异步任务队列 Arq 和 Uvicorn 的高性能异步 REST API 模板。

- [fastapi-tortoise](https://github.com/prostomarkeloff/fastapi-tortoise) :star: 150+ :fork_and_knife: 15+  
  基于 FastAPI 和 TortoiseORM 的可扩展 Web API 模板，适合熟悉 TortoiseORM 的开发者。

- [freddie](https://github.com/tinkoffjournal/freddie) :star: 50+ :fork_and_knife: 3+  
  FastAPI 上类似 Django REST Framework 风格的声明式视图集库。

***

## 异步相关（Async）

- [fastapi](https://github.com/tiangolo/fastapi) :star: 53000+ :fork_and_knife: 4500+  
  高性能 Python ASGI 框架，易学且适用于生产。

- [starlette](https://github.com/encode/starlette) :star: 7200+ :fork_and_knife: 650+  
  轻量且功能强大的 ASGI 框架，FastAPI 的底层基础。

- [slowapi](https://github.com/laurentS/slowapi) :star: 550+ :fork_and_knife: 45+  
  基于 Starlette/FastAPI 的速率限制器。

- [fastapi-events](https://github.com/melvinkcx/fastapi-events) :star: 250+ :fork_and_knife: 12+  
  异步事件调度和处理库，适合基于事件驱动的应用。

- [fastapi-limiter](https://github.com/long2ice/fastapi-limiter) :star: 110+ :fork_and_knife: 25+  
  请求速率限制器，结合 Redis 实现。

- [agraffe](https://github.com/odd12258053/agraffe) :star: 30+ :fork_and_knife: 2+  
  适合无服务器架构（AWS Lambda、GCF、Azure Functions）的基于 ASGI 的 API 构建。

***

## 缓存相关（Caching）

- [fastapi-cache2](https://github.com/OMLab-python/fastapi-cache2) :star: 300+ :fork_and_knife: 50+  
  活跃的缓存解决方案，支持 Redis 和 Memcached，支持多种缓存策略。

- [fastapi-redis-cache](https://github.com/a-luna/fastapi-redis-cache) :star: 90+ :fork_and_knife: 12+  
  基于 Redis 的高速缓存库，支持请求头和响应头缓存解析。

- [cache-house](https://github.com/Turall/cache-house) :star: 20+ :fork_and_knife: 3+  
  支持 Redis 单实例和集群模式的 Python 缓存工具。

***

## 命令行工具（Commands）

- [manage-fastapi](https://github.com/ycd/manage-fastapi) :star: 950+ :fork_and_knife: 65+  
  FastAPI CLI 工具，快捷生成项目结构和模板。

- [restish](https://github.com/danielgtaylor/restish) :star: 320+ :fork_and_knife: 40+  
  功能丰富的 REST API 命令行交互工具。

- [pydantic-to-typescript](https://github.com/phillipdupuis/pydantic-to-typescript) :star: 120+ :fork_and_knife: 12+  
  将 Pydantic 模型转换为 TypeScript 类型定义。

***

## 配置管理（Configuration）

- [dynaconf](https://github.com/dynaconf/dynaconf) :star: 2800+ :fork_and_knife: 220+  
  多环境、动态配置管理，支持多种格式。

***

## 项目模板和实战

- [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql) :star: 5500+ :fork_and_knife: 1200+  
  Tiangolo 官方生产级全栈项目模板，含前端、后台、数据库迁移、Docker 支持。

- [fastapi-sqlalchemy](https://github.com/tiangolo/fastapi-sqlalchemy) :star: 950+ :fork_and_knife: 150+  
  展示 SQLAlchemy 及 Alembic 集成的规范实践。

***

# 说明

- 本笔记聚焦项目活跃度、通用性和现代实践，剔除或弱化了多年未更新、社区较冷的项目。  
- 推荐项目均有良好的文档支持，便于快速入门和深度定制。  
- 鼓励结合官方 FastAPI 示例和项目模板来搭建高质量的应用架构。  
- 如需定制化解决方案，例如基于特定 ORM 的后台，建议评估项目活跃度和社区支持后选用。  