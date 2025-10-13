try:
    file = open(input("enter te file name"))
    contend = file.read()
    print(contend)
    file.close()
except FileNotFoundError:
    print("File not found")
