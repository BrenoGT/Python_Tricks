def my_sum(*args):
    result = 0
    for item in args:
        result += item
    return result


def main():
    result = my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(result)


if __name__ == '__main__':
    main()
