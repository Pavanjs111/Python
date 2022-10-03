a = "Avengers Assemble"
b = a.maketrans("A", "P")
print(a.translate(b))

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))