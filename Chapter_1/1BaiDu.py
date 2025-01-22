from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

# 自动检测网页的编码
data = resp.read().decode("utf-8")

# 使用检测到的编码解码内容

with open("m_baidu.html", mode="w", encoding="utf-8") as f:
    f.write(data)

print("done", end="")
