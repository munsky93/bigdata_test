i = """We encourage everyone to contribute to Python. If you still have 
questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new 
contributors through the process."""

i = i.upper()

i = i.replace(",", " ")
i = i.replace(".", " ")
i = i.replace("\n", " ")
i = i.split()
for j in i:
    print(j)
k = set([])
for j in i:
    p = j+":"+str(i.count(j))
    k.add(p)
for j in k:
    print(j)