def decorator(function):
    def wrapper(expression):
        try:
            result = function(expression)
        except Exception as e:
            print(f"We have problems - {e}")
        else:
            print(f"No problems, result - {result}")

    return wrapper


@decorator
def calculate(expression):
    return eval(expression)


a = input(str("What you want to do? - "))
calculate(a)
