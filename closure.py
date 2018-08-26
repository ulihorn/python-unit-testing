def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    
    return inner_function

if __name__ == '__main__':
    my_func = outer_function()
    my_func()
    print(type(my_func))
