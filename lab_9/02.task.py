file_name = input("Please enter file -> ")

def read_line_by_line(f_name):
    try:
        file = open(file_name,"r")
        for line in file:
            print(line)

    except FileNotFoundError:
        print("File not found !")
    finally:
        file.close()

read_line_by_line(file_name)