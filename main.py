from activity.find_square_root_integer import find_square_root_integer
# from activity.comparison import check_many_values, timing

def check_some_values():
    print(find_square_root_integer(0))  # 0
    print(find_square_root_integer(1))  # 1
    print(find_square_root_integer(4))  # 2
    print(find_square_root_integer(5))  # 2
    print(find_square_root_integer(7))  # 2
    print(find_square_root_integer(9))  # 3
    print(find_square_root_integer(17))  # 4
    print(find_square_root_integer(64))  # 8

def main():
    check_some_values()
    # check_many_values()
    # timing()

if __name__ == "__main__":
    main()
