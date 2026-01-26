# Google登录绕过脚本
基于SeleniumBase实现的未被检测的Google登录绕过脚本，可规避Google对自动化工具的登录限制。

YouTube教程：[youtube.com/google-login-bypass](https://youtu.be/GcTGurNyf6Y)（注：境外链接可能需要特殊网络环境访问）


## 使用方法
1. 在 `main` 函数中，将占位符凭据替换为你的实际Google账号信息：
   ```python
   user_email = "your_email@gmail.com"  # 替换为你的Google邮箱
   user_password = "your_password"      # 替换为你的Google密码
   ```


## 错误示例
本脚本可解决使用常规Selenium登录时常见的如下错误：

![Google登录错误提示](https://user-images.githubusercontent.com/98614666/157562373-526db685-ae97-430c-8cf3-73235b883adb.png)
（错误提示：“该浏览器或应用可能不安全。建议使用其他浏览器。若已在支持的浏览器中操作，可刷新页面后重试登录。”）


## 所需依赖包
- SeleniumBase（内置未被检测的浏览器能力，无需额外安装undetected-chromedriver）  
  执行以下命令安装：
  ```bash
  pip install seleniumbase
  ```


## 注意事项
1. 脚本默认预留10秒等待时间，供用户完成手动验证（如二次验证、验证码输入），若需调整时间，可修改 `GoogleLogin` 类中的 `verification_wait_time` 参数。
2. Google的反自动化策略会持续更新，若遇到登录失败，建议先执行 `pip install --upgrade seleniumbase` 更新依赖包。
3. 使用本脚本需遵守Google《服务条款》，请勿用于违规场景。


## 致谢
credits: https://github.com/xtekky