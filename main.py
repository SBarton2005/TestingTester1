print("This is a test")
a = "This is a test"
print(a)
b = "This"
c = "is"
d = "a"
e = "test"
print(b, c, d, e)
print(f"This {c} a {e}")
def tester():
  return "This is a test"
f = tester()
print(f)
g = ["This", "is", "a", "test"]
h = ""
i = 0
for i in g:
  h = h + i + " "
print(h)