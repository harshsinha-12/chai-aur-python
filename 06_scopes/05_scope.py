x = 99

def f1():
    def f2():
        print(x)
    f2()

f1()