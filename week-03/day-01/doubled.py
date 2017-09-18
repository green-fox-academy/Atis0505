def divide(file_text):
    try:
        f = open(file_text, "r")
        file_string = f.readlines()
        line_text = ""
        to_file = open("simple_file.txt", "a")
        for line in file_string:
            for i in range(0,(len(line)),2):
                line_text += line[i]
        to_file.write(line_text)
        f.close()
        to_file.close()
        print("Done")
    except IOError:
        print("Unable to read file, ", file_text)

divide("duplicated-chars.txt.txt")