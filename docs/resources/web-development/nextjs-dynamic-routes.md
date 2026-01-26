高价值：否

标题：
Next.js动态路由：从基础到高级用法全解析

### Next.js动态路由详解

#### 开篇：主题与背景
主题是介绍Next.js的动态路由相关内容。背景是在处理像博客文章、电商产品详情、用户个人资料页面等场景时，需要根据动态参数来创建不同的页面，而Next.js的动态路由能很好地满足这一需求。其目的是让开发者了解Next.js动态路由的基础、高级用法以及其他相关要点，从而能在Next.js应用中灵活运用动态路由来构建更灵活的Web应用。

#### 动态路由的基础
- **约定**：通过将文件夹名称放在方括号中来创建动态片段，比如`[id]`或者`[slug]`，这些动态片段会作为`params`属性传递给布局、页面和路由函数。就好比给一个盒子起了个带括号的名字，里面装的内容会以特定方式传递出去。
- **实现方式**：在`app`目录下，通过在文件夹和文件名中使用方括号来创建动态路由。例如`app/blog/[slug]/page.js`表示一个使用`slug`作为动态参数的路由。在`page.tsx`页面组件中，能通过`params`属性直接获取路由参数。就像在一个特定的页面组件里，有个专门的地方可以拿到根据动态路由来的参数。下面是一个示例代码：
```typescript
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const slug = (await params).slug
  return <div>My Post: {slug}</div>
}
```
- **示例**：要是你的博客有路由`app/blog/[slug]/page.js`，那么访问`/blog/a`时，`params`的值就会是`{ slug: 'a' }`。通过表格来看更清晰：
| 路由                     | 示例 URL | params            |
| :----------------------- | :------- | :---------------- |
| `app/blog/[slug]/page.js` | `/blog/a` | `{ slug: 'a' }` |
| `app/blog/[slug]/page.js` | `/blog/b` | `{ slug: 'b' }` |
| `app/blog/[slug]/page.js` | `/blog/c` | `{ slug: 'c' }` |

#### 动态路由的高级用法
- **捕获所有片段**：通过在方括号内添加省略号`[...folderName]`，能让动态片段捕获所有后续片段。例如`app/shop/[...slug]/page.js`会匹配`/shop/clothes`、`/shop/clothes/tops`以及`/shop/clothes/tops/t-shirts`等。用表格展示：
| 路由                        | 示例 URL           | params                  |
| :-------------------------- | :----------------- | :---------------------- |
| `app/shop/[...slug]/page.js` | `/shop/a`          | `{ slug: ['a'] }`      |
| `app/shop/[...slug]/page.js` | `/shop/a/b`        | `{ slug: ['a', 'b'] }` |
| `app/shop/[...slug]/page.js` | `/shop/a/b/c`      | `{ slug: ['a', 'b', 'c'] }` |
- **可选捕获所有片段**：把参数放在双重方括号`[[...folderName]]`中，能让捕获所有片段成为可选的。比如`app/shop/[[...slug]]/page.js`会匹配`/shop`、`/shop/clothes`、`/shop/clothes/tops`以及`/shop/clothes/tops/t-shirts`等。表格如下：
| 路由                         | 示例 URL           | params                    |
| :--------------------------- | :----------------- | :------------------------ |
| `app/shop/[[...slug]]/page.js` | `/shop`           | `{ slug: undefined }`     |
| `app/shop/[[...slug]]/page.js` | `/shop/a`          | `{ slug: ['a'] }`        |
| `app/shop/[[...slug]]/page.js` | `/shop/a/b`        | `{ slug: ['a', 'b'] }`   |
| `app/shop/[[...slug]]/page.js` | `/shop/a/b/c`      | `{ slug: ['a', 'b', 'c'] }` |

#### 其他需要了解的点
- **params属性**：因为`params`属性是一个Promise，所以必须使用`async/await`或者React的`use`函数来访问这些值。就像要打开一个需要等待才能开启的盒子一样，得用特定方式获取里面的内容。
- **静态参数生成**：`generateStaticParams`函数能和动态路由片段结合使用，在构建时静态生成路由，而不是在请求时按需生成，这有点像提前把一些东西准备好，而不是用的时候再临时去弄。
- **类型定义**：使用TypeScript时，可以根据配置的路由片段为`params`添加类型。通过表格来看不同路由对应的`params`类型定义：
| 路由                                 | params 类型定义                |
| :----------------------------------- | :----------------------------- |
| `app/blog/[slug]/page.js`            | `{ slug: string }`            |
| `app/shop/[...slug]/page.js`          | `{ slug: string[] }`          |
| `app/shop/[[...slug]]/page.js`        | `{ slug?: string[] }`         |
| `app/[categoryId]/[itemId]/page.js` | `{ categoryId: string, itemId: string }` |

#### 总结
本文围绕Next.js的动态路由展开，先介绍了动态路由的基础，包括约定、实现方式和示例；接着讲解了动态路由的高级用法，如捕获所有片段和可选捕获所有片段；还提及了其他需要了解的点，像params属性、静态参数生成和类型定义等。通过理解这些内容，开发者能更有效地在Next.js应用中运用动态路由，构建出更灵活动态的Web应用。