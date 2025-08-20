高价值：否

标题：
Next.js服务器操作：创建、调用及相关功能全解析

### Next.js中服务器操作的创建与调用教程

#### 开篇：主题与背景
本教程主题是介绍在Next.js应用中如何创建和调用服务器操作，目的是让开发者掌握利用服务器操作来进行数据更新等相关功能。背景是Next.js允许使用React的服务器操作来更新数据，这为高效的数据管理提供了途径。

#### 创建服务器操作
- **定义方式**：服务器操作通过`use server`指令定义。可以将该指令放在异步函数顶部标记函数为服务器操作，也可放在单独文件顶部标记文件所有导出为服务器操作。一般建议大多数情况使用单独文件。例如在`app/lib/actions.ts`文件中：
```typescript
// app/lib/actions.ts
'use server'
 
export async function createPost(formData: FormData) {}
 
export async function deletePost(formData: FormData) {}
```
- **服务器组件内联使用**：服务器操作还能在服务器组件中内联使用，通过将`"use server"`指令添加到函数体顶部。示例如下：
```typescript
export default function Page() {
  // Server Action
  async function createPost() {
    'use server'
    // Update data
    // ...
 
  return <></>
}
```

#### 客户端组件调用服务器操作
不能在客户端组件中定义服务器操作，但可以从顶部有`"use server"`指令的文件中导入并在客户端组件中调用。比如在`app/actions.ts`中定义服务器操作：
```typescript
// app/actions.ts
'use server'
 
export async function createPost() {}
```
然后在客户端组件`app/ui/button.tsx`中调用：
```typescript
'use client'
 
import { createPost } from '@/app/actions'
 
export function Button() {
  return <button formAction={createPost}>Create</button>
}
```

#### 调用服务器操作的方式
主要有两种调用方式：表单和事件处理程序。
- **表单**：React扩展了HTML`<form>`元素，允许用HTML`action`属性调用服务器操作。在表单中调用时，函数会自动接收`FormData`对象，可使用原生`FormData`方法提取数据。例如在`app/ui/form.tsx`中：
```typescript
import { createPost } from '@/app/actions'
 
export function Form() {
  return (
    <form action={createPost}>
      <input type="text" name="title" />
      <input type="text" name="content" />
      <button type="submit">Create</button>
    </form>
  )
}
```
对应的`app/actions.ts`中服务器操作函数：
```typescript
'use server'
 
export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')
 
  // Update data
  // Revalidate cache
}
```
- **事件处理程序**：可以在客户端组件中通过事件处理程序（如`onClick`）调用服务器操作。例如在`app/like-button.tsx`中：
```typescript
'use client'
 
import { incrementLike } from './actions'
import { useState } from 'react'
 
export default function LikeButton({ initialLikes }: { initialLikes: number }) {
  const [likes, setLikes] = useState(initialLikes)
 
  return (
    <>
      <p>Total Likes: {likes}</p>
      <button
        onClick={async () => {
          const updatedLikes = await incrementLike()
          setLikes(updatedLikes)
        }}
      >
        Like
      </button>
    </>
  )
}
```

#### 显示待定状态
执行服务器功能时，可使用React的`useActionState`钩子显示加载指示器。该钩子返回一个待处理的布尔值。例如在`app/ui/button.tsx`中：
```typescript
'use client'
 
import { useActionState } from 'react'
import { createPost } from '@/app/actions'
import { LoadingSpinner } from '@/app/ui/loading-spinner'
 
export function Button() {
  const [state, action, pending] = useActionState(createPost, false)
 
  return (
    <button onClick={async () => action()}>
      {pending ? <LoadingSpinner /> : 'Create Post'}
    </button>
  )
}
```

#### 重新验证缓存
执行更新后，可在服务器功能中调用`revalidatePath`或`revalidateTag`来重新验证Next.js缓存并显示更新的数据。例如在`app/lib/actions.ts`中：
```typescript
'use server'
 
import { revalidatePath } from 'next/cache'
 
export async function createPost(formData: FormData) {
  // Update data
  // ...
 
  revalidatePath('/posts')
}
```

#### 重定向
若执行更新后希望将用户重定向到其他页面，可在服务器功能中调用`redirect`。例如：
```typescript
'use server'
 
import { redirect } from 'next/navigation'
 
export async function createPost(formData: FormData) {
  // Update data
  // ...
 
  redirect('/posts')
}
```

#### 总结
总而言之，Next.js的服务器操作提供了一种在服务器上执行数据更新的强大方法，可以从服务器组件和客户端组件调用。通过`use server`指令的简单使用，开发者可以无缝地创建和调用服务器端函数，从而实现高效的数据管理和用户体验。其核心是通过明确的指令定义、多种调用方式以及相关的状态显示、缓存验证、重定向等功能，来保障数据更新和用户体验的高效实现。