def my_sum(*args):
    result = 0
    for item in args:
        result += item
    return result


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]
    result = my_sum(*list1, *list2, *list3)
    print(result)


if __name__ == '__main__':
    main()
