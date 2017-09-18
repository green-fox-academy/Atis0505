# Create a method that decrypts reversed-lines.txt
def decrypt(file_text):
    try:
        f = open(file_text, "r")
        file_string = f.readlines()
        line_text = ""
        to_file = open("normal_text_from_reversed_lines.txt", "a")
        for line in file_string:
            for i in range((len(line)-1),0,-1):
                line_text += line[i]
        to_file.write(line_text)
        f.close()
        to_file.close()
        print("Done")
    except IOError:
        print("Unable to read file, ", file_text)

decrypt("reversed_lines.txt")