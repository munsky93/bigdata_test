i = """We encourage everyone to contribute to Python. If you still have 
questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new 
contributors through the process."""

i = i.upper()
list=[]
i = i.replace(",", " ")
i = i.replace(".", " ")
i = i.replace("\n", " ")
i = i.split()


a = set([])
for i in i :
    p = i+":"+str(i.count(i))
    a.add(p)

for i in a:
     list.append(i)
list.sort()
for i in list:
 print(i)