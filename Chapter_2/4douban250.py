import requests
import re

url = "https://movie.douban.com/top250"
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "cookie": 'll="118159"; bid=HEumb7IkfuQ; _pk_id.100001.4cf6=908dbd8a0a5ed975.1717338423.; _vwo_uuid_v2=D27535A071AB6D960A0E671D15469F267|15a5e1bf7967df2e82475bb2a717b447; __yadk_uid=QBOlwWXY1VJOcMneVDptpOyxj1Wwfifl; _vwo_uuid_v2=D79E135C76A148F373923BA6A26037ACF|91df469269675d8067ee18d47a05d1d7; viewed="35158799_27612832"; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1737522989%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1122590998.1717338423.1737520369.1737522989.7; __utmb=30149280.0.10.1737522989; __utmz=30149280.1737522989.7.4.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1403889562.1717338423.1737520369.1737522989.5; __utmb=223695111.0.10.1737522989; __utmz=223695111.1737522989.5.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; dbcl2="276369851:bCv6Vadrjhc"; ck=F0tE',
}

block = re.compile(r"<li>.*?</li>", re.S)
name = re.compile(
    r'<em class="">(?P<count>\d+)</em>.*?<a href=".*?">.*?<img width="\d*" alt=(?P<name>".*?") src=".*?" class="">',
    re.S,
)
id = re.compile(r'<span class="inq">(.*?)</span>', re.S)
f = open("douban250.txt", mode="w", encoding="utf-8")

for i in range(0, 250, 25):
    param = {"start": f"{i}"}
    resp = requests.get(url=url, params=param, headers=dic)
    assert resp.status_code == 200
    block_list = block.findall(resp.text)
    for content in block_list:
        b_name = next(name.finditer(content), None)
        b_id = next(id.finditer(content), None)

        if not b_name:
            continue
        f.write(b_name.group("count") + " " + b_name.group("name") + "\n")
        wri_t = b_id.group(1) if b_id else "None"
        f.write("Tag: " + wri_t + "\n")
    resp.close()

f.close()
print("done")
