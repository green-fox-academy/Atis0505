# Create a method that decrypts encoded-lines.txt
def decrypt(file_text):
    try:
        f = open(file_text, "r")
        file_string = f.readlines()
        line_text = ""
        to_file = open("normal_text_from_encoded_lines.txt", "a")
        for line_number in range((len(file_string)-1)):
            for char_number in range((len(file_string[line_number])-1)):
                if not file_string[line_number][char_number] == " ":
                    line_text += chr(ord(file_string[line_number][char_number])-1)
                else:
                    line_text += " "
            line_text += "\n"
        to_file.write(line_text)
        f.close()
        to_file.close()
        print("Done")
    except IOError:
        print("Unable to read file, ", file_text)

decrypt("encoded_lines.txt")
