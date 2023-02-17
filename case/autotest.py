from selenium import webdriver

# 无界面的浏览器
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(options=option)

# 访问百度首页
browser.get(r'https://www.baidu.com/')
print(browser.current_url)
print(browser.page_source)
# 截图预览
browser.get_screenshot_as_file('截图.png')

# 关闭浏览器
browser.close()