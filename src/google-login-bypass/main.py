from seleniumbase import SB
from selenium.webdriver.common.by import By
import time

class GoogleLogin:
    def __init__(self) -> None:
        self.login_url = 'https://accounts.google.com/ServiceLogin'
        self.verification_wait_time = 10
    
    def login(self, email: str, password: str) -> None:
        with SB(uc=True) as driver:
            driver.open(self.login_url)
            time.sleep(2)
            driver.type('identifier', f'{email}\n', By.NAME)  # 'identifier'是邮箱输入框的name属性
            time.sleep(2)
            driver.type('Passwd', f'{password}\n', By.NAME)  # 'Passwd'是密码输入框的name属性
            self.wait_for_verification()

    def wait_for_verification(self) -> None:
        time.sleep(self.verification_wait_time)

def main():
    google_login = GoogleLogin()
    user_email = "your_email@gmail.com"
    user_password = "your_password"
    try:
        google_login.login(user_email, user_password)
        print("登录流程已执行完成（含验证等待）")
    except Exception as e:
        print(f"登录过程中出现错误：{str(e)}")

if __name__ == "__main__":
    main()