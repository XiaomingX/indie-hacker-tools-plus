# 精选Golang生态资源

## Actor 模型框架
构建分布式和高可靠性系统的并发模型。
- [Ergo](https://github.com/ergo-services/ergo)  
  Go语言实现的Actor框架，灵感源自Erlang，支持网络透明、分布式集群、监督树机制，具备高性能消息传递。
- [ProtoActor](https://github.com/asynkron/protoactor-go)  
  跨多语言的高效分布式Actor框架，支持Go、C#、Java/Kotlin，设计现代且功能丰富。

## 人工智能 (AI) 框架
简化构建语言模型与AI应用。
- [langchaingo](https://github.com/tmc/langchaingo)  
  方便快速构建基于语言模型的应用，支持链式调用和扩展。
- [LocalAI](https://github.com/mudler/LocalAI)  
  开源且可自托管的本地AI模型方案，是轻量级OpenAI替代品。

## 音频处理
音频文件的编码、解码与播放。
- [flac](https://github.com/mewkiz/flac)  
  Go语言实现的FLAC音频格式编码与解码。
- [Oto](https://github.com/hajimehoshi/oto)  
  跨平台音频播放库，支持低延迟和多操作系统。

## 认证与权限控制
身份验证和访问控制核心组件。
- [authboss](https://github.com/volatiletech/authboss)  
  模块化身份验证框架，简单集成常用认证功能。
- [casbin](https://github.com/casbin/casbin)  
  多模型访问控制框架，支持ACL、RBAC、ABAC等灵活策略。
- [goth](https://github.com/markbates/goth)  
  多OAuth身份认证客户端，支持多种社交平台登录。
- [jwt-go](https://github.com/golang-jwt/jwt)  
  标准的JSON Web Token工具库，支持签名、验证和生成。

## 区块链核心库
构建区块链应用的底层框架和协议。
- [cosmos-sdk](https://github.com/cosmos/cosmos-sdk)  
  用于搭建区块链应用的模块化框架，广泛用于Cosmos生态系统。
- [go-ethereum](https://github.com/ethereum/go-ethereum)  
  以太坊官方Go语言客户端，实现以太坊节点功能。
- [tendermint](https://github.com/tendermint/tendermint)  
  高性能的拜占庭容错共识引擎和网络层中间件。

## 聊天机器人框架
快速开发多平台聊天机器人的工具。
- [bot](https://github.com/go-telegram/bot)  
  轻量无依赖的Telegram机器人库，内置UI组件。
- [telebot](https://github.com/tucnak/telebot)  
  简洁易上手的Go语言Telegram机器人框架。

## 自动化构建与开发工具
编写和管理构建任务，提高开发效率。
- [air](https://github.com/cosmtrek/air)  
  代码变动实时编译并重启应用，极大提升本地开发效率。
- [mage](https://github.com/magefile/mage)  
  用Go写的make替代品，支持复杂构建逻辑。

## 命令行工具开发库
构建现代命令行程序的基础库。
- [cobra](https://github.com/spf13/cobra)  
  功能强大，支持子命令、自动生成文档，广泛被采用。
- [pflag](https://github.com/spf13/pflag)  
  兼容POSIX/GNU风格参数解析，作为`flag`包的更强版本。

## 配置管理
灵活读取和管理多种格式的配置。
- [viper](https://github.com/spf13/viper)  
  支持JSON、YAML、TOML等格式，还能自动监听配置变更。
- [env](https://github.com/caarlos0/env)  
  将环境变量映射到结构体，支持默认值和转换。
- [godotenv](https://github.com/joho/godotenv)  
  从 .env 文件加载环境变量，方便本地开发。

## 数据库工具
包括嵌入式和关系数据库支持。
- [bbolt](https://github.com/etcd-io/bbolt)  
  纯Go实现的嵌入式键值数据库，性能稳定。
- [badger](https://github.com/dgraph-io/badger)  
  高性能键值存储，支持事务，适合嵌入式场景。
- [gorm](https://github.com/go-gorm/gorm)  
  功能全面的ORM库，支持多种SQL数据库，简化数据库操作。

## 分布式系统框架
支持微服务、RPC和高可用服务架构。
- [go-zero](https://github.com/zeromicro/go-zero)  
  稳定且高性能的分布式Web & RPC框架，带代码生成和中间件。
- [go-kit](https://github.com/go-kit/kit)  
  功能模块化，支持服务发现、熔断等，适合企业级微服务。

## 邮件处理工具
邮件生成与发送的可靠方案。
- [email](https://github.com/jordan-wright/email)  
  简洁灵活，用于构造和发送邮件。
- [MailHog](https://github.com/mailhog/MailHog)  
  本地邮件捕获服务器，便于开发调试邮件。

## 跨平台GUI库
适合构建桌面图形界面应用。
- [fyne](https://github.com/fyne-io/fyne)  
  基于Material Design，原生支持多平台（包括移动端）。
- [gio](https://gioui.org)  
  现代即时模式GUI库，性能优异，跨平台支持。
- [Wails](https://wails.io)  
  用Web技术开发桌面应用，整合本地功能与前端。

## 硬件交互
与设备和传感器接口的库。
- [ghw](https://github.com/jaypipes/ghw)  
  采集主机硬件信息的工具库。
- [go-rpio](https://github.com/stianeikeland/go-rpio)  
  树莓派GPIO控制库，不依赖cgo。
- [gocv](https://github.com/hybridgroup/gocv)  
  OpenCV的Go绑定，用于计算机视觉任务。

## 图片处理
高性能图像操作。
- [imaging](https://github.com/disintegration/imaging)  
  简单易用的图像编辑库，支持裁剪、缩放等。
- [bimg](https://github.com/h2non/bimg)  
  基于libvips，性能优异的图像处理库。

## IoT 物联网开发
外围设备与物联网集成。
- [periph](https://periph.io/)  
  访问物理设备和外设的低层库。
- [gobot](https://github.com/hybridgroup/gobot/)  
  面向机器人和物联网的框架，简化硬件控制。

## 任务调度
定时任务和周期任务管理。
- [gocron](https://github.com/go-co-op/gocron)  
  易用的定时任务库，支持秒级调度。
- [gron](https://github.com/roylee0704/gron)  
  直观的基于时间的任务执行工具。

## JSON 处理
高效读写和操作JSON数据。
- [GJSON](https://github.com/tidwall/gjson)  
  一行代码获取JSON中复杂路径的值，无需解码。
- [go-json](https://github.com/goccy/go-json)  
  替代标准库，性能优化明显。

## 日志库
提供高性能且可扩展的日志功能。
- [zap](https://github.com/uber-go/zap)  
  Uber开源的高性能结构化日志库，适合生产环境。
- [zerolog](https://github.com/rs/zerolog)  
  零内存分配的JSON日志库，API设计简洁。

## Web 框架
高效的HTTP服务开发基础。
- [Gin](https://github.com/gin-gonic/gin)  
  轻量且高性能的Web框架，社区活跃。
- [Fiber](https://github.com/gofiber/fiber)  
  基于fasthttp，性能极佳，API灵感来自Express.js。
- [Echo](https://github.com/labstack/echo)  
  简单易用，支持中间件和路由。
