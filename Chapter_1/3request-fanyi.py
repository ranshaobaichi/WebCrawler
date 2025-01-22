import requests

url = "https://fanyi.baidu.com/sug"
word = input("请输入翻译的单词")

# 给出key word
data_dic = {"kw": word}

# post形式访问
# 发送post请求 发送的数据必须放在字典中 通过data参数进行传递
resp = requests.post(url, data=data_dic)
print(resp.json())
resp.close()
