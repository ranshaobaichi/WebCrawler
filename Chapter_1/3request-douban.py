import requests
from json import dump

# 网址详细内容
url = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "30",
}

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp = requests.get(url, params=param, headers=header)

with open("douban.json", mode="w+", encoding="utf-8") as f:
    dump(resp.json(), f, ensure_ascii=False, indent=4)

cnt = 0
for item in resp.json():
    print(item["title"], end=" ")
    cnt += 1
print(f"\n{cnt}")
resp.close()
