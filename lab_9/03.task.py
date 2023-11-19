
def convert_message(message):
    ascii_values = []
    for l in message:
        ascii_values.append(ord(l))
    return ascii_values

def write_data(ascii_values):
    try:
        file = open("document.bin","wb+")
        for n in ascii_values:
            file.write(n.to_bytes())
    except FileNotFoundError:
        print("File not found !")
    finally:
        file.close()


message = "This is good"
ascii_values = convert_message(message)
write_data(ascii_values)