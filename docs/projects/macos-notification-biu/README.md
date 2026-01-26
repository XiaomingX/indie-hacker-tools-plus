# macos-notification
程序运行完成之后，在右上角弹出提示.

```
import subprocess

def send_notification(title, message):
    script = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    subprocess.run(script, shell=True, check=True)

# 使用示例
send_notification("任务完成", "您的程序已运行结束。")
```
