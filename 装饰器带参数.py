# 带参数装饰器将参数传入
# def function():
#     print("function功能")

def deco(arg):
    def _deco(function):
        def __deco():
            print("addfunction:%s"%arg)
            function
        return __deco
    return _deco


@deco("hahaha")
def function():
    print("function功能")

"""@deco("hahaha")等于 function==deco("hahaha")(function),先执行第一个括号的,而deco("hahaha")返回的是_deco(function)的
地址，所以接下来执行_deco(function),返回的是__deco的地址，所以最后function()==deco("hahaha")(function)()还是执行
__deco的内容，arg是最开始装饰器传入的参数"""
function()