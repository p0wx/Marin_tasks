def find_largest_number(numbers_list):
    largest_number = 0
    for number in numbers_list:
        if number > largest_number:
            largest_number = number
    return largest_number


def main():
    numbers_list = [1, 56, 8, 6, 6, 2000, 8, 9, ]
    largest_number = find_largest_number(numbers_list)
    print(largest_number)
    

if __name__ == "__main__":
    main()
