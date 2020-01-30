def create_variable(variable_name: str, variable_type=None, value=None):
    exec(f'{variable_name} = {variable_type.__name__}({value})')
    print(f'{variable_name} = {variable_type.__name__}({value})')


def main():
    create_variable(variable_name='testing', variable_type=int, value=4)


if __name__ == '__main__':
    main()
