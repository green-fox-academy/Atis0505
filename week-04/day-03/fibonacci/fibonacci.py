def fibonacci_counter(int_index):
    if int_index == None:
        return None
    else:
        if type(int_index) is not int:
            return 0
        if int_index == 0:
            return 0
        elif int_index == 1:
            return 1
        else:
            return fibonacci_counter(int_index-1) + fibonacci_counter(int_index-2)
        