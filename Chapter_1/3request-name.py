# 安装requests


# 浏览器地址栏中 一律使用get方式请求
# requests.get()
import requests

name = input("输入查找的人名\n")
url = f"https://www.sogou.com/web?query={name}"

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}  # 处理反爬，添加请求头，伪装正常设备

resp = requests.get(url, headers=dic)
print(resp.text)  # 拿到页面源代码
