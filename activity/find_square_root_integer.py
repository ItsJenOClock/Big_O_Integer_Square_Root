# Returns the closest integer (rounded down) to the
# square root of the parameter `squared_number`
# O(log n), where n is the magnitude of the input value
def find_square_root_integer(squared_number):    
    max_of_search = squared_number + 1
    floor_of_search = 0
    
    while True:
        number_to_check = (max_of_search + floor_of_search) // 2
        squared_num_to_check = number_to_check * number_to_check
    
        # We've found the true square root or the closest integer rounded down
        if (squared_num_to_check == squared_number
            or floor_of_search == max_of_search - 1):
                
            return number_to_check

        # number_to_check is too large, cut high values out of our search space
        elif squared_num_to_check > squared_number:
            max_of_search = number_to_check

        # number_to_check is too small, cut low values out of our search space
        elif squared_num_to_check < squared_number:
            floor_of_search = number_to_check

# O(n)
def find_square_root_integer_linear(squared_number):
    for i in range(squared_number + 1):
        if i * i > squared_number:
            return i - 1

    return i
