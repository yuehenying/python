import re
pattern = re.compile(r'\d+')
result1 = re.search(pattern, 'abc192qwfwa')
if result1:
    print(result1.group())
else:
    print('匹配失败1')