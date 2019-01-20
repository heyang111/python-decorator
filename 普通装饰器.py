# 装饰器
# 函数function1打印function功能


# 例子
def deco(function):
    def addfunction():
        print("添加的功能")
        function()
    return addfunction


# @deco
def function():
    print("functon功能")


function=deco(function)
'''
        再执行function
    '''
function()
'''这样就在function加上新的执行内容
再说@deco，@deco实际上等于function=deco（function）,把这一行放到function下面，再执行得到一样的结果
所以最后执行的function（）实际上等于deco(function)(),而deco(function)执行后返回的是addfunction的地址，
所以最后执行的是addfunction的内容
内容
'''
