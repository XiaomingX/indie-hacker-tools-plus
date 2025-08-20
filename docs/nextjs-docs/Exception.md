高价值：否

标题：
Next.js错误处理指南：预期与未捕获异常全攻略

### Next.js错误处理全解析

#### 开篇：主题与背景
主题是Next.js的错误处理，背景是理解并妥善处理错误能让应用更健壮、用户体验更佳。目的是向大家详细介绍Next.js中预期错误和未捕获异常的处理方法。

#### 1. 预期错误的处理
##### （1）预期错误概述
预期错误是应用正常运行中可能出现的错误，比如服务器端表单验证失败（用户提交数据不符合服务器验证规则）、API请求失败（网络问题或服务器错误导致获取数据失败）。这类错误要明确处理并将信息返回客户端，不用`try/catch`块，而是把错误信息当返回值。
##### （2）`useActionState` Hook（React 19）
- **作用**：React 19引入的新Hook，用于管理Server Actions的状态和处理预期错误，能简化错误处理，避免手动管状态和写`try/catch`块。它接收一个Server Action作参数，返回包含状态、action函数和pending状态的数组。
- **示例**：
  - 在`app/actions.ts`中：
    ```typescript
    'use server'
    
    export async function createPost(prevState: any, formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      const res = await fetch('https://api.vercel.app/posts', {
        method: 'POST',
        body: { title, content },
      })
      const json = await res.json()
     
      if (!res.ok) {
        return { message: 'Failed to create post' }
      }
    }
    ```
  - 在`app/ui/form.tsx`中：
    ```typescript
    'use client'
    
    import { useActionState } from 'react'
    import { createPost } from '@/app/actions'
    
    const initialState = {
      message: '',
    }
    
    export function Form() {
      const [state, formAction, pending] = useActionState(createPost, initialState)
     
      return (
        <form action={formAction}>
          <label htmlFor="title">Title</label>
          <input type="text" id="title" name="title" required />
          <label htmlFor="content">Content</label>
          <textarea id="content" name="content" required />
          {state?.message && <p aria-live="polite">{state.message}</p>}
          <button disabled={pending}>Create Post</button>
        </form>
      )
    }
    ```
##### （3）Server Components
在Server Components获取数据时，可通过判断response的`ok`属性确定请求是否成功。若失败，能直接返回错误信息或重定向。示例：
```typescript
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()
 
  if (!res.ok) {
    return 'There was an error.'
  }
 
  return '...'
}
```
##### （4）Not Found
可用`notFound`函数处理未找到资源情况，并用`not-found.js`文件显示404页面。示例：
- 在`app/blog/[slug]/page.tsx`中：
```typescript
import { getPostBySlug } from '@/lib/posts'

export default async function Page({ params }: { params: { slug: string } }) {
  const post = getPostBySlug((await params).slug)

  if (!post) {
    notFound()
  }

  return <div>{post.title}</div>
}
```
- 在`app/blog/[slug]/not-found.tsx`中：
```typescript
export default function NotFound() {
  return <div>404 - Page Not Found</div>
}
```

#### 2. 未捕获的异常处理
##### （1 ）错误边界
Next.js用错误边界处理未捕获异常。错误边界是React组件，能捕获子组件错误并显示备用UI，防止组件树崩溃。通过在路由段添加`error.js`文件并导出React组件创建错误边界。示例：
```typescript
// app/dashboard/error.tsx
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```
错误会冒泡到最近父级错误边界，可在路由层次不同级别放`error.tsx`文件实现细粒度错误处理。
##### （2）全局错误
可用`global-error.js`文件处理根布局中的错误，全局错误UI需定义自己的`<html>`和`<body>`标签。

#### 总结
通过上述方法能有效处理Next.js应用中的各种错误，提高应用稳定性和用户体验。要理解预期错误与未捕获异常的区别并采取相应处理策略，熟悉`useActionState` Hook和错误边界的使用，能编写出更健壮、易维护的Next.js应用。