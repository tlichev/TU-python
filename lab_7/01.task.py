def read_info(file_name):
    try:
        f = open(file_name , "r")
        return f.read()
    except FileNotFoundError:
        print("File not found or file name is incorrect")
    finally:
        f.close()


file_name = input()
print(read_info(file_name))

