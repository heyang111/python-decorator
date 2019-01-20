# 函数带两个参数a,b，打印a和b，最后返回a+b

# def function(a,b):
#     print("functon功能:%s,%s"%(a,b))
#     return a+b

# q=function(5,10)
# print(q)


def deco(function):
    def addfunction(a,b):
        print("增加的功能")
        ret=function(a,b)
        return ret
    return addfunction

@deco
def function(a,b):
    print("functon功能:%s,%s"%(a,b))
    return a+b

"""deco等于   因为function=deco(function)，而所以function(5,3)执行的是deco(function)(5,3)，先执行的deco(function)返回值
是addfunction的地址，deco(function)(5,3)==addfunction（5，3）
"""

q=function(5,3)
print(q)