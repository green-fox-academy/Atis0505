# Create a method that decrypts reversed-order.txt
def decrypt(file_text):
    try:
        f = open(file_text, "r")
        file_string = f.readlines()
        line_text = ""
        to_file = open("sorted_order_text.txt", "a")
        for line_number in range((len(file_string)-1), 0, -1):
            line_text += file_string[line_number]
        to_file.write(line_text)
        f.close()
        to_file.close()
        print("Done")
    except IOError:
        print("Unable to read file, ", file_text)

decrypt("reversed_order.txt")