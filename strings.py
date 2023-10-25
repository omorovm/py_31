# Напишите определение декоратора memoize  
from functools import wraps
def memoize(func):
    @wraps(func)
    def inner(n, dict_ = {}):
        if n in dict_.keys():
            return dict_[n]
        dict_[n] = func(n)
        return inner(n-1, dict_)
        
    return inner    

# Код ниже не удаляйте, он нужен для проверки   


@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# assert fibonacci(10) == 12586269025
# assert fibonacci(50) == 12586269025
# assert fibonacci(60) == 1548008755920
# assert fibonacci(70) == 190392490709135
# assert fibonacci(80) == 23416728348467685
# assert fibonacci(90) == 2880067194370816120
# assert fibonacci(100) == 354224848179261915075
# assert fibonacci.__name__ == 'fibonacci'
# assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
# print('Good')