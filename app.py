def swapFileData():
    with open("file1.txt", "r") as a:
        data_a = a.read()

    with open("file2.txt", "r") as b:
        data_b = b.read()

    with open("file3.txt", "r") as c:
        data_c = c.read()

    with open("file3.txt", "w") as c:
        c.write(data_b)    

    with open("file2.txt", "w") as b:
        b.write(data_a)    

    with open("file1.txt", "w") as a:
        a.write(data_c)    

swapFileData()
