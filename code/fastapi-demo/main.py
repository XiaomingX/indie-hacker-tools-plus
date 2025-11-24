from fastapi import FastAPI, BackgroundTasks
import asyncio

app = FastAPI()

async def async_operation():
    await asyncio.sleep(5)  # 模拟耗时操作
    print("后台操作完成")  # 用于验证后台任务是否执行

def background_task():
    asyncio.run(async_operation())

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/async")
async def asyncb(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task)
    return {"result": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)