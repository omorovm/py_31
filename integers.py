def func():
    def inner():
        # var = 3
        print(var)
    var = 2
    inner()
    
func()