import re

# r使得字符串为原始格式，避免正则表达式中\被解释为转义字符


# findall匹配字符串中所有符合规则的内容
list = re.findall(r"\d+", "wddhh:12312321,ashdiuwh:909")
print(list)
# 结果：['12312321', '909']


# finditer返回迭代器
# 迭代器：使用iter()将具有迭代器属性的元素转换为迭代器
# 访问：使用for访问，next()获取下一个元素
# next(param1：迭代器，param2：若到达末尾返回的数据)
# 如果迭代器已经到达末尾，它会抛出 StopIteration 异常。
it = re.finditer(r"\d+", "wddhh:12312321,ashdiuwh:909")
for i in it:
    print(i)
# 结果：
# <re.Match object; span=(6, 14), match='12312321'>
# <re.Match object; span=(24, 27), match='909'>
# 取出数据需要gropu方法
for i in it:
    print(i.group())
# 注：上次运行时迭代器已到末尾，本次不会输出结果
# 结果：
# 2312321
# 909


# serach返回全文第一个匹配对象 拿数据需要group
it = re.search(r"\d+", "wddhh:12312321,ashdiuwh:909")
print(it)
# 结果：
# <re.Match object; span=(6, 14), match='12312321'>

# match返回从头开始匹配的第一个匹配对象
it = re.match(r"\d+", "wddhh:12312321,ashdiuwh:909")
print(it)
# 结果：
# None


# 预加载正则匹配式
obj = re.compile(r"\d+")
print(obj.findall("wddhh:12312321,ashdiuwh:909"))

# 结果：['12312321', '909']


# 访问特定元素
s = """asdawasd111adasdsdsss10000awda
       hdgurkhgkduh222djhgfuskh20000ff
       hjgihji33333olhgkjogkujo3000
       asdwadffffff4444koiuuoipuoipuoi40000kjlkhgj
    """
# 运用()分组，可直接用group(index)访问
# 注意：gropu(0)为整体，从1开始为对应分组
obj = re.compile(r"[a-z]*(\d*)[a-z]*(\d[0]*)[a-z]*", re.S)  # re.S使得'.'可匹配换行符
res = obj.finditer(s)
for it in res:
    print(it.group(1) + " " + it.group(2))

# 使用"?P<name>"形式，可使用group(name)访问特定分组
obj = re.compile(r"[a-z]*(?P<first>\d*)[a-z]*(?P<second>\d[0]*)[a-z]*", re.S)
res = obj.finditer(s)
for it in res:
    print(it.group("first") + " " + it.group("second"))
