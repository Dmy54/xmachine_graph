def logger(function_to_decorate):
    def wrapper(*args, **kwargs):
        function_to_decorate(*args)

        f = open("./log/test_log", "a")

        string_to_write = ''
        for element in args:
            string_to_write += str(element) + "\\"

        f.write(string_to_write + '\n')

    return wrapper

def managed_logger(arg1):
    def decorator(func):
        def wrapper(*args):
            string_to_write = ''
            if arg1 == '1':
                string_to_write = "from main"
            else:
                string_to_write = "from gui"

            f = open("./log/test_log", "a")
            for element in args:
                string_to_write += str(element) + " "

            f.write(string_to_write + '\n')

            return func(*args)
        return wrapper
    return decorator


@managed_logger('1')
def func2(a):
    print(a)



@logger
def func(a, b):
    print(a, b)
#
# func(1, 2)
# func('asd', 987)

func2("hello")