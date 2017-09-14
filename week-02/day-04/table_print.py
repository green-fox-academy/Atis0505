ingredients = [
	{ 'vodka': 1, 'needs_cooling': True },
	{ 'coffee_liqueur': 0, 'needs_cooling': True },
	{ 'fresh_cream': 1, 'needs_cooling': True },
	{ 'captain_morgan_rum': 2, 'needs_cooling': True },
	{ 'mint_leaves': 0, 'needs_cooling': False },
	{ 'sugar': 100, 'needs_cooling': False },
	{ 'lime juice': 10, 'needs_cooling': True },
	{ 'soda': 100, 'needs_cooling': True },
]

def main(table):
    first_keys =[]
    second_keys =[]
    for i in range(len(table)):
        first_keys += [(list(table[i].keys())[0])]
        second_keys += [(list(table[i].keys())[1])]
    len_column_1 = len(max(first_keys, key=len)) + 1
    len_column_2 = len(max(first_keys, key=len)) + 1
    max_row_width = len_column_1 + len_column_2 + 10 + len("In Stock")

    for row_number in range(len(table)+4):
        row_text=""
        line_char ="|"
        if row_number == 0 or row_number == 2 or row_number == (len(table)+3):
            for char_index_in_row in range(max_row_width):
                if char_index_in_row == 0 or char_index_in_row == (len_column_1+3) or char_index_in_row == max_row_width-1 or char_index_in_row == (len_column_1+len_column_2+7):
                    row_text+="+"
                else:
                    row_text+="-"
        elif row_number == 2:
            row_text += line_char + "Ingredient" + (space*((len_column_1-2)-len("Ingredient"))+line_char
        print(row_text)
        
    
main(ingredients)