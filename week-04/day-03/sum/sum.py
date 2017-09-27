class Sum:
    def get_sum(self, integ_list):

        if len(str(integ_list)) == 0:
            return 0
        elif len(str(integ_list)) == 1:
            return str(integ_list)
        elif integ_list == None:
            return None
        else:
            return sum(integ_list)