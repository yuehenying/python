import re
'''
pattern = re.compile(r'\d+')
print(re.findall(pattern, 'A1B2C3D4'))
'''
'''
pattern = re.compile(r'\d+')
matchiter = re.finditer(pattern, 'A1B2C3D4')
for match in matchiter:
    print(match.group())
'''

p = re.compile(r'(?P<word1>\w+)(?P<word2>\w+)')
s = 'i say, hello world!'
print(p.sub(r'\g<word2> \g<word1>', s))
p = re.compile(r'(\w+) (\w+)')
print(p.sub(r'\2 \1', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(p.sub(func, s))