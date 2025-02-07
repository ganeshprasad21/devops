with open("./example.txt",'w') as f:
    # x = 0
    f.writelines("0123456789\n\n")
    f.writelines([f"line {x} content here\n" for x in range(69)])

with open("./example.txt") as d:
    print(type(d))
    d.seek(3)
    print(d.read(3))
    print(d.readlines())

