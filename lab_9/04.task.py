def read_from_binaryFile():
    try:
        file = open("document.bin", "rb")
        print(file.read(4))
    except FileNotFoundError:
        print("File not found !")
    finally:
        file.close()


read_from_binaryFile()