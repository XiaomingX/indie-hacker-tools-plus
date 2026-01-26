# awesome-wordpress：2026 实用资源大全


## 一、核心资源与文档
这部分是 WordPress 开发的「基础工具书」，涵盖核心代码和官方权威指南，替代了过时的 Codex 文档。

- **[WordPress 官方源码仓库](https://github.com/WordPress/WordPress)**  
  托管 WordPress 核心全部代码，是查看底层逻辑、提交代码贡献（修复漏洞/新增功能）或自定义核心行为的唯一入口。
- **[WordPress 开发者手册](https://developer.wordpress.org/)**  
  官方替代了老旧的 Codex，包含主题开发、插件开发、REST API 等所有核心知识，是最权威的学习文档。
- **[Hook 参考工具集](https://developer.wordpress.org/reference/hooks/ & https://hookr.io/)**  
  - 官方 **Hook Reference**：精准查询所有动作钩子（Action）和过滤钩子（Filter）的用法；  
  - Hookr.io：第三方可视化 Hook 索引，支持按功能筛选，新手更易上手。
- **[WordPress REST API 官方文档](https://developer.wordpress.org/rest-api/)**  
  替代了过时的 wp-api.org，详细说明如何通过 API 调用/修改文章、用户、评论等所有 WordPress 数据，是开发前后端分离项目的核心指南。


## 二、主题开发
重点补充「块主题」相关资源（WordPress 5.9+ 主推），移除停更的老旧框架。

### 1. 主题开发框架
- **[Genesis](https://studiopress.com/genesis/)**  
  老牌稳定的商业主题框架，主打性能和 SEO 优化，适合搭建企业站，有大量成熟子主题。
- **[Understrap](https://understrap.com/)**  
  基于 Bootstrap 5 和 Underscores 的免费框架，支持传统主题和块主题开发，兼容性强，新手友好。
- **[Gantry](https://gantry.org/)**  
  基于 Bootstrap 的响应式框架，自带可视化布局编辑器，适合快速搭建复杂页面结构。

### 2. 入门主题（新手起步模板）
- **[Underscores (_s)](https://underscores.me/)**  
  官方推荐的「裸框架」主题，只保留核心结构，无多余代码，是自定义主题的最佳起点。
- **[Emi](https://github.com/zoerooney/Emi)**  
  支持 Sass（样式预处理）和 Gulp（自动化构建），适合想学习现代化前端工具链的开发者。

### 3. 块主题工具
- **[Create Block Theme](https://wordpress.org/plugins/create-block-theme/)**  
  官方插件，可在 WordPress 后台直接创建/编辑块主题，无需手动写代码，降低块主题入门门槛。


## 三、插件开发
聚焦「现代插件开发」，补充块编辑器插件相关工具。

- **[插件开发官方指南](https://developer.wordpress.org/plugins/)**  
  从基础结构到高级功能（如权限控制、数据库操作）的完整教程，替代了老旧的 Codex 内容。
- **[Create Block](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-create-block/)**  
  官方命令行工具，一键生成块编辑器插件的基础结构，支持 React 开发，适配最新 WordPress 编辑器生态。
- **[Fieldmanager](https://fieldmanager.org/)**  
  轻量工具包，快速创建后台表单、可重复字段（Metabox），避免重复编写表单逻辑。


## 四、开发工具与环境
这些工具能大幅提升开发效率，替代了部分功能重叠的老旧工具。

### 1. 本地开发环境
- **[Local](https://localwp.com/)**  
  最流行的 WordPress 本地开发工具，一键创建站点、切换 PHP 版本、配置 SSL，支持同步到线上服务器。

### 2. 代码与功能工具
- **[TGM 插件激活](https://github.com/thomasgriffin/TGM-Plugin-Activation)**  
  主题/插件必备工具，可强制或推荐用户安装依赖插件（如 WooCommerce），简化用户操作。
- **[Aqua Resizer](https://github.com/syamilmj/Aqua-Resizer)**  
  动态调整图片尺寸的轻量工具，虽 WordPress 核心已支持 `wp_get_attachment_image_srcset`，但它仍适合复杂尺寸需求。

### 3. 版本控制辅助
- **[WordPress Git Ignore](https://github.com/github/gitignore/blob/main/WordPress.gitignore)**  
  官方推荐的 `.gitignore` 模板，避免提交冗余文件（如缓存、上传目录）到代码仓库。


## 五、前端组件
精选当前主流的前端工具，移除了活跃度低的框架。

- **[Bootstrap 5](https://getbootstrap.com/)**  
  最成熟的响应式框架，提供栅格系统、组件（按钮/卡片），快速适配移动端。
- **[Tailwind CSS](https://tailwindcss.com/)**  
  实用优先的 CSS 框架，通过原子类快速编写样式，适合追求定制化设计的项目。
- **[Font Awesome 6](https://fontawesome.com/)**  
  最全面的图标库，支持 SVG/字体格式，包含 2 万+ 图标，替代了老旧的 Fort Awesome 链接。
- **[Swiper](https://swiperjs.com/)**  
  现代轮播图插件，支持触摸滑动、动画效果，适配移动端，替代了老旧的 JSSor Slider。


## 六、调试与测试工具
精准定位问题的「利器」，补充了比 Debug Bar 更强大的工具。

- **[Query Monitor](https://wordpress.org/plugins/query-monitor/)**  
  开发者必备调试插件，显示数据库查询、PHP 错误、API 请求、缓存状态等详细信息，比 Debug Bar 更全面。
- **[Debug Bar](https://wordpress.org/plugins/debug-bar/)**  
  轻量调试面板，可搭配 **Debug Bar Extender** 扩展，查看钩子执行、脚本加载等信息。
- **[主题检查工具集](https://wordpress.org/plugins/theme-check/ & https://wordpress.org/plugins/block-theme-check/)**  
  - Theme Check：验证传统主题是否符合 WordPress 规范；  
  - Block Theme Check：专门检查块主题的兼容性和标准。
- **[WordPress 测试数据](https://developer.wordpress.org/themes/advanced-topics/theme-test-data/)**  
  官方提供的测试内容（文章、评论、分类等），替代了老旧的 Theme Unit Test，用于验证主题显示效果。


## 七、多站点管理与托管服务
适合管理多个 WordPress 站点的工具和专业托管平台。

- **[ManageWP](https://managewp.com/)**  
  云端多站点管理平台，支持一键更新、备份、监控多个站点，适合维护 10+ 站点的开发者。
- **[InfiniteWP](https://infinitewp.com/)**  
  可自建服务器的多站点管理工具，数据更私密，适合对隐私要求高的用户。
- **[WP Engine](https://wpengine.com/)**  
  顶级 WordPress 托管服务商，提供自动备份、CDN、安全防护，适合企业级站点。


## 八、资源素材
免费、高质量的设计素材，覆盖图片和图标需求。

- **[Unsplash](https://unsplash.com/)**  
  免费高分辨率图片库，无版权限制，适合网站 banner、文章配图。
- **[Pexels](https://www.pexels.com/)**  
  与 Unsplash 类似，提供大量免费视频和图片，支持按场景精准筛选。
- **[Burst](https://burst.shopify.com/)**  
  专注商业场景的免费图片库（如电商、办公），画质清晰，分类明确。


## 九、命令行工具：WP-CLI
通过命令行高效管理 WordPress，替代重复的后台操作。

- **[WP-CLI 官方文档](https://make.wordpress.org/cli/handbook/)**  
  核心功能：安装 WordPress、更新核心/插件/主题、导出数据、执行数据库查询等。  
  常用命令示例：  
  - 安装插件：`wp plugin install woocommerce --activate`  
  - 导出文章：`wp export --post_type=post --output=posts.xml`  
  - 更新核心：`wp core update`


## 十、主题/插件交易市场
涵盖免费和商业资源，补充官方资源库。

- **[WordPress.org 官方库](https://wordpress.org/themes/ & https://wordpress.org/plugins/)**  
  免费主题/插件集散地，所有资源经过安全审核，适合个人站点和预算有限的项目。
- **[Themeforest](https://themeforest.net/)**  
  最大的商业主题市场，覆盖电商、博客、企业站等场景，部分主题自带可视化编辑器。
- **[Creative Market](https://creativemarket.com/)**  
  优质商业资源平台，除主题插件外，还提供字体、模板等设计素材。


## 十一、技术社区与支持
遇到问题时的「求助渠道」，覆盖从新手到专家的需求。

- **[WordPress Stack Exchange](https://wordpress.stackexchange.com/)**  
  专注 WordPress 的技术问答社区，回答质量高，适合复杂开发问题。
- **[Stack Overflow (WordPress 标签)](https://stackoverflow.com/questions/tagged/wordpress)**  
  全球最大编程社区，可搜索历史问题，或提问获取快速响应。
- **[Reddit r/WordPress](https://www.reddit.com/r/WordPress/)**  
  活跃的非技术向社区，适合交流使用技巧、推荐资源、解决基础问题。
- **[WordPress 官方论坛](https://wordpress.org/support/)**  
  官方支持渠道，可直接与核心开发者和社区志愿者交流。
