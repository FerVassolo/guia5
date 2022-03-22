with open("extra_file.txt", "r")  as rf:
    with open("g6e7.txt", "a") as af:
        f_contents = rf.read()
        rf_size = len(f_contents)
        af.write(str(rf_size))




    """while len(f_contents) > 0:
        print(f_contents, end = "")
        f_contents = f.read(size_to_read)
    """
print("\n")
print("#8")

def fibbonaci(n, archivo):
    with open(archivo, "w") as f:
        # n + n-1
        n1 = 0
        n2 = 1
        f.write(str(n1))
        for elm in range(2, n+1):
            sum = n1 + n2
            n1 = n2
            n2 = sum
            f.write(str(n1))


print(fibbonaci(5, "g8.txt"))

print("\n")
print("#9")



