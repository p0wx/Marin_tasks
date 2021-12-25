def find_mean(numbers_list):
    numbers_count = len(numbers_list)
    sum = 0
    for number in numbers_list:
        sum+=number
    return sum/numbers_count


def main():
    numbers_list = [345, 8790, 2492, 56, 6785, 6, 6, 2000, 9, 67, 8 ]
    mean = find_mean(numbers_list)
    print(mean)
    

if __name__ == "__main__":
    main()
