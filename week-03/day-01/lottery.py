# Create a method that find the 5 most common lottery numbers otos.csv
def five_most_frequent(csv_file):
    try:
        f = open(csv_file, "r")
        csv_file_lines = f.readlines()
        lottery_numbers = []
        for line_text in csv_file_lines:
            splited_line = line_text.split(";")
            for i in range(-1, -6, -1):
                lottery_numbers.append(int(splited_line[i]))
        counted_numbers_list= []
        lottery_numbers = sorted(lottery_numbers)
        
        counter = 0
        for i in range(1,len(lottery_numbers)):
            counter += 1
            if lottery_numbers[i] > lottery_numbers[i-1] or i == len(lottery_numbers)-1:
                counted_numbers_list.append(counter)
                counter = 0
        max_numbers_dict = {}
        for i in range(5):
            max_numbers_dict[str(counted_numbers_list.index(max(counted_numbers_list))+1)] = max(counted_numbers_list)
            counted_numbers_list[counted_numbers_list.index(max(counted_numbers_list))] = 0

        print(max_numbers_dict)
        print(counted_numbers_list)
        f.close()
    except IOError:
        print("Unable to read file, ", csv_file)

five_most_frequent("otos.csv")