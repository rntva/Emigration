import re

p = re.compile("a.b")
m = p.match("a\nb")
print(m)

pp = re.compile("a.b", re.S)
m = pp.match("a\nb")
print(m)

p = re.compile("[a-z]+")
pp = re.compile("[a-z]+", re.I)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))
print(pp.match("python"))
print(pp.match("Python"))
print(pp.match("PYTHON"))

p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

pp = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(pp.findall(data))