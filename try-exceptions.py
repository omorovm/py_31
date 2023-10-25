'===================Exceptions===================='
# Исключения (ошибки) - объектыб которые прерываютработу когда, если не были обработаны

SyntaxError
# исключение, которое выходит, когда в коде допущена синтаксическая ошибка
'''
print( 
# SyntaxError: '(' was never closed

a =
# SyntaxError: invalid syntax
(когда мы сделали что-то нето в синтаксисе)
'''

NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
"""
name.split()
# NameError: name 'name' is not defined
"""

TypeError
# исключение, которое выходит, когда мы проводим неправильные операции мужду типами данных
"""
'asdfg' + 2
TypeError: can only concatenate str (not "int") to str

{1,2,3,4,[1,23,4]}
TypeError: unhashable type: 'list'

for i in 12435:
    pass
TypeError: 'int' object is not iterable

input('введи возраст', 1)
TypeError: input expected at most 1 argument, got 2

#[].append()
TypeError: list.append() takes exactly one argument (0 given)
"""

IndexError
# выходит, когда указали несуществующий индекс
'''
list_ = [1,2,3,4,5]
list_[23]
IndexError: list index out of range

list_.pop(1000)
IndexError: pop index out of range
'''

KeyError
# выходит, когда мы передали несуществующий ключ
"""
dict_ = {'a': 6}
print(dict_['b'])
KeyError: 'b'
"""

ValueError
# выходит,когда мы передаем неправильный тип данных в определенную функцию 
"""
int('sdfg')
ValueError: invalid literal for int() with base 10: 'sdfg'

a, b, c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""

ZeroDivisionError
# выходит при делении на 0
"""
45/0
13%0
12//0
ZeroDivisionError: division by zero
"""

AttributeError
#  выходит, когда мы обращаемся к несуществующему методу объекта (тип данных)
"""
list_ = [1,2,3,4]
list_.replace()
'ghhdg'.pop()
AttributeError: 'list' object has no attribute 'replace'
"""

IndentationError
# выходит,когда мы неправильно используем отступы
"""
 a=5
for i in range(21):
print(i)
"""

Exception
# исключение, которое создали, чтобы его вызвать 

"=====================Вызов исключения=========================="

#raise NameError('выходиииии',a)


"=====================Обработка исключения=========================="
# чтобы код продолжал работать, мы можем использовать конструкцию try-except, и обрабатывать исключения
'''
try:
    age = int(input()) 
except ValueError as e:
    print('afdsghf', type(e))
'''

try:
    a = int(input())
    b = int(input())
    a/b
    # код, который возможно вызовет ошибку
except ValueError:
    print('введи число а не строку')
    # код, который отработает при возникновении указанной ошибки
except ZeroDivisionError:
    print('Нельзя делить на 0')
else:
    print(a/b)
    # код, который отработает при отсутствии ошибок
finally:
    print("Работаю всегда")
    # код, который отработает в любом случае


KeyboardInterrupt

# исключения - мы можем словить (косяк со стороны клиента)
# ошибка - мы не можем словить(обработать) (косяк со стороны разраба)
