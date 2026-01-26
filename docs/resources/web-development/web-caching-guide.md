高价值：否

标题：
Next.js数据获取与缓存：方式、缓存机制等全解析

### Next.js数据获取与缓存技术详解

#### 开篇：主题与背景
本文核心主题是介绍Next.js中数据获取和缓存的基础知识，目的是帮助中国开发者更好地理解和应用相关技术。背景是在现代Web开发中，高效的数据获取和缓存对于提升应用性能至关重要，Next.js提供了多种数据获取方式和缓存机制来满足开发者需求。

#### 数据获取方式
- **在服务器上使用`fetch`API获取数据**
    - **何时何地与示例**：在React服务端组件中使用`fetch`API从API获取数据，例如下面的示例代码，默认情况下`fetch`的响应不被缓存。若路由无动态API，会在`next build`期间预渲染为静态页面，可通过增量静态再生更新数据。若要防止预渲染，可添加`export const dynamic = 'force-dynamic'`到文件中，但通常使用`cookies`、`headers`等函数或读取`searchParams`会自动使页面动态渲染，无需显式使用`force-dynamic`。
    ```typescript
    export default async function Page() {
      const data = await fetch('https://api.vercel.app/blog')
      const posts = await data.json()
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
    ```
- **在服务器上使用ORM或数据库获取数据**
    - **何时何地与示例**：此组件用于获取并展示博客文章列表，默认数据库响应不缓存但可通过额外配置缓存。若不在其他地方用动态API，下次构建时会预渲染到静态页面，也可通过增量静态再生更新数据。若要防止预渲染，可添加`export const dynamic = 'force-dynamic'`到文件中，同样，使用`cookies`、`headers`等函数或读取`searchParams`会自动使页面动态渲染，无需显式使用`force-dynamic`。
    ```typescript
    import { db, posts } from '@/lib/db'
   
    export default async function Page() {
      const allPosts = await db.select().from(posts)
      return (
        <ul>
          {allPosts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
    ```
- **在客户端获取数据**
    - **说明**：建议首先尝试在服务器端获取数据，在某些情况下客户端数据获取有意义。此时可在`useEffect`中手动调用`fetch`（不推荐），或依赖社区流行的React库如SWR或React Query进行客户端获取。示例代码如下：
    ```typescript
    'use client'
 
    import { useState, useEffect } from 'react'
   
    export function Posts() {
      const [posts, setPosts] = useState(null)
   
      useEffect(() => {
        async function fetchPosts() {
          const res = await fetch('https://api.vercel.app/blog')
          const data = await res.json()
          setPosts(data)
        }
        fetchPosts()
      }, [])
   
      if (!posts) return <div>Loading...</div>
   
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
    ```

#### 数据缓存
- **概念与默认情况**：缓存是将已获取或计算的数据临时存储以便后续重用，可提升应用性能。Next.js默认会缓存数据来提高性能和降低成本。Next.js有内置数据缓存，扩展了本地`fetch`API，允许服务器上每个请求设置自己的持久缓存语义，默认使用`fetch`的数据请求会被缓存，可通过`fetch`的`cache`和`next.revalidate`选项配置缓存行为。
- **示例与缓存位置等**：可用`unstable_cache`API缓存响应，如下面示例缓存数据库查询结果1小时并添加缓存标签`posts`，然后可使用增量静态再生使缓存失效。Next.js默认将`fetch`的返回值缓存到服务器上的数据缓存中，使用`POST`方法的`fetch`请求也会自动缓存，除非在使用`POST`方法的路由处理程序中，且数据缓存是持久的HTTP缓存，可自动扩展并在多个区域共享。
```typescript
import { unstable_cache } from 'next/cache'
import { db, posts } from '@/lib/db'
   
const getPosts = unstable_cache(
  async () => {
    return await db.select().from(posts)
  },
  ['posts'],
  { revalidate: 3600, tags: ['posts'] }
)
   
export default async function Page() {
  const allPosts = await getPosts()
   
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```
- **四种缓存机制**
|机制|是什么|在哪里|目的|持续时间|
|----|----|----|----|----|
|请求记忆化|函数返回值|服务器|在React组件树中重用数据|每请求生命周期|
|数据缓存|数据|服务器|跨用户请求和部署存储数据|持久性（可重新验证）|
|全路由缓存|HTML和RSC有效负载|服务器|降低渲染成本并提高性能|持久（可重新验证）|
|路由器缓存|RSC有效负载|客户端|减少导航时的服务器请求|用户会话或基于时间的请求|

#### 数据重用
在Next.js中，若在多个函数（如`generateMetadata`和`generateStaticParams`）中使用相同数据，若使用`fetch`，可通过添加`cache: 'force-cache'`记忆化请求，这样可安全使用相同URL和选项调用，仅发一个请求；若不使用`fetch`而是直接用ORM或数据库，可使用React`cache`函数包装数据fetch，会删除重复数据，仅发一个查询。

#### 并行和串行数据获取
- **串行**：组件树中的请求彼此依赖，可能导致更长加载时间。
- **并行**：路由中的请求会尽早启动，同时加载数据，减少加载数据所需总时间。

#### 预加载数据
可使用预加载模式防止瀑布流，创建实用程序函数，在阻塞请求前尽早调用。例如，`checkIsAvailable()`阻止`<Item/>`渲染，可在之前调用`preload()`尽早启动`<Item/>`数据依赖项，使`<Item/>`渲染时数据已获取。

#### 敏感数据保护
建议使用React的taint API（`taintObjectReference`和`taintUniqueValue`）防止整个对象实例或敏感值传递给客户端。

#### 总结
深入理解Next.js的数据获取和缓存机制对高效使用该框架至关重要，合理运用这些机制能显著提升应用性能与用户体验。