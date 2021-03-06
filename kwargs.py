def concatenate_keys(**kwargs):
    print(kwargs.get('b') + '\n\n')
    result = ""
    for arg in kwargs:
        result += arg
    return result


def concatenate_values(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]
    print(concatenate_values(a="Real", b="Python", c="Is", d="Great", e="!"))
    print(concatenate_keys(a="Real", b="Python", c="Is", d="Great", e="!"))


if __name__ == '__main__':
    main()
