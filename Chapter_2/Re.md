# 正则表达式元字符

![image-20250121153530492](D:\VS CODE\Python\WebCrawler\MD_photots\image-20250121153530492.png)

`[ ]`中的`-`表示范围，例如`[1-9]`可以匹配1~9的各数字

`( )`匹配括号内的字符，可多个连接使用并按下标访问组内各个匹配的字符（即按组捕获），如：

#### 示例：

```python
(\d{3})-(\d{3})-(\d{4})
```

这个正则表达式用于匹配格式如 `123-456-7890` 的电话号码。它有三组捕获：

1. `(\d{3})` 捕获前三个数字。
2. `(\d{3})` 捕获接下来的三个数字。
3. `(\d{4})` 捕获最后的四个数字。

```python
import re
pattern = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(pattern, "123-456-7890")
if match:
    print(match.group(1))  # 输出 '123'
    print(match.group(2))  # 输出 '456'
    print(match.group(3))  # 输出 '7890'
```

**注：元字符都为匹配一次**

# 量词

![image-20250121155538785](D:\VS CODE\Python\WebCrawler\MD_photots\image-20250121155538785.png)

# 贪婪匹配和惰性匹配

![image-20250121161725912](D:\VS CODE\Python\WebCrawler\MD_photots\image-20250121161725912.png)

**注：默认为贪婪匹配**

![image-20250121161805283](D:\VS CODE\Python\WebCrawler\MD_photots\image-20250121161805283.png)

# 使用

![image-20250121171504781](D:\VS CODE\Python\WebCrawler\MD_photots\image-20250121171504781.png)