def dec1(func):
    print("1111")
    def one():
        print("2222")
        func()
        print("3333")
    return one

def dec2(func):
    print("aaaa")
    def two():
        print("bbbb")
        func()
        print("cccc")
    return two

@dec1
@dec2
def test():
    print("test test")

test()
"""结果是
aaaa
1111
2222
bbbb
test test
cccc
3333
所以多个装饰器执行的顺序就是从离函数最近的一个装饰器开始，执行到第一个装饰器，再执行函数本身
"""