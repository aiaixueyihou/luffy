'''
list
    增：insert、append、extend
    删：pop、remove、 clear、del
    该：切片该li[2] = "asdf" ,当步长不为一时，切片长度必须和迭代长度相等
    查：for循环
'''
#
# a = ["a","a","b"]
# print(a.count("a"))
# for i in range(1,5,2):
#     print(i)

'''
字典：
    key:不可变类型，可哈西
    value：任何类型数据
    增：如果key存在执行修改操作，不存在，直接创建
        setdefault
    删：
        pop()
        del.dic
    该：
        直接改：通过key去改，dict1.update(dict2)
        把dict2更新到dict1中去，有key就修改没有就增加
        dict2不变
    查：dic.get(key,default)

'''
# dic = {1: 2, 3: 4, 5: 6, 7: 8}
# dic.setdefault(1,3)
# print(dic)
# dic.setdefault(1,4)
# print(dic)
# del dic[1]
# print(dic)
# dic.clear()
# print(dic)
# t = ()
# t = dic.popitem()
# print(dic)
# print(t)
# a = dic.get(0)
# print(a)
# a = dict.fromkeys([1,2,3],"dfdsdf")
# print(a)
# a[1] = "我就是神"
# print(a)
# s1 = {1,2,3,4,5}
# s2 = {1,2,3,6,7}
# print(s1-s2)
# print(s1|s2)
# print(s1&s2)
# s = set([1,2,3])
# s = set("123456")
# s = set({1:2,3:4})
# print(s,type(s))
# print(s)
# s.pop()
# print(s)
# a = -100.123456
# b = round(a,3)
# print(b)

# i = 1
# def test():
#     print(i)
#     # i += 1
# test()

# def v1(addr):
#     # 取每个数
#     id = [int(x) for x in addr.split(".")]
#     print(id)
#     return sum(id[i] << [24, 16, 8, 0][i] for i in range(4))
#
# print(v1("127.0.0.1"))
'''
字符串：split ,strip replace find index startswith endswith captalize
upper lower

'''


#
# print(2<<2)
# a = 'adsfsdf'
# print(a.endswith("f"))
# li1 = [1, 2, 3]
# li2 = li1.copy()
# li1.append(4)
# print(li1, li2)  # [1, 2, 3, 4] [1, 2, 3]
# print("\n".join("\t".join(["%s*%s=%s" % (j,i,j*i) for j in range(1,1+i)]) for i in range(1,10)))
# print("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1,10)) )
# print(( i % 2 for i in range(10) ) )
# print(1 < 2 == 2)
# print("1,2,3".split(','))
# print([int(x) for x in ["1","2"]])
# import random
# li = [1,5,6,4,9,7,8,3,2]
#
# def partition(li,left,right):
#     i = random.randint(left,right)
#     li[left],li[i] = li[i],li[left]
#     tem = li[left]
#     while left<right:
#         while left <right and li[right]>=tem:
#             right -=1
#         li[left] = li[right]
#
#         while left < right and li[left] <=tem:
#             left +=1
#         li[right] = li[left]
#
#     li[left] = tem
#     return left
#
# def _quick(li,left,right):
#     if left <right:
#         mid = partition(li,left,right)
#
#         _quick(li,left,mid-1)
#         _quick(li,mid+1,right)
#
# def quick(li):
#     _quick(li,0,len(li)-1)
# quick(li)
# print(li)

# def make_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     print("............",count)
#     return counter
#
#
# def make_counter_test():
#     mc = make_counter()
#     print(mc())
#     print(mc())
#     # print(mc())
#
# make_counter_test()
# def func1():
#     b = 6
#
#     def func2():
#         b = 666
#         print(b)
#
#     func2()
#     print(b)  # 父级不受影响
#
#
# func1()

# gcount = 0
# def global_test():
#     # gcount = 1
#     print(gcount)
#
#
# global_test()
# class Stack():
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items ==[]
#
#     def push(self,item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items)-1]
#
#     def size(self):
#         return len(self.items)
# if __name__ == '__main__':
#     stack = Stack()
#     stack.push("H")
#     stack.push("J")
#     stack.push("O")
#     stack.push("P")
#     print(stack.size())
#     print(stack.peek())
#     print(stack.pop())
#     print(stack.pop())

#
# def bin_search(data,value,low,hight):
#     if low <=hight:
#         mid = (low+hight) //2
#         if data[mid] == value:
#             return mid
#         elif data[mid] >value:
#             return bin_search(data,value,low,mid-1)
#         else:
#             return bin_search(data,value,mid+1,hight)
#     else:
#         return
#
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(bin_search(li,8,12,len(li)-1))
# import random
# print(random.sample(range(100), 10))
# for i in range(1,10):
#     print(i)

#
# class my(type):
#     pass
#     # def __call__(self, *args, **kwargs):
#     #     return "myiohfohsd"
# class Num(object,metaclass=my):
#     # 普通方法：能用Num调用而不能用实例化对象调用
#     # def one():
#     #     print('1')
#
#     # 实例方法：能用实例化对象调用而不能用Num调用
#     def two(self):
#         print('2')

#     # 静态方法：能用Num和实例化对象调用
#     @staticmethod
#     def three():
#         print('3')
#
#     # 类方法：第一个参数cls长什么样不重要，都是指Num类本身，调用时将Num类作为对象隐式地传入方法
#     @classmethod
#     def go(cls):
#         cls.three()
# n = Num()
# print(n)
# Num.go()
# n = Num()
# n.go()
# import itertools
# print(len(list(itertools.permutations('12345', 3))))

# class MyType(type):
#     def __call__(self, *args, **kwargs):
#         return 'MyType'
#
#
# class Foo(object, metaclass=MyType):
#     def __init__(self):
#         return 'init'
#
#     def __new__(cls, *args, **kwargs):
#         return cls.__init__(cls)
#
#     def __call__(self, *args, **kwargs):
#         return 'call'
#
#
# obj = Foo()
# print(obj)  # MyType


# class Students():
#     def __call__(self, *args, **kwargs):
#         print( '执行了__call__方法')
#
# s = Students()
# print(s())

# class Settings():
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Settings, cls).__new__(cls,*args,**kwargs)
#         return cls._instance

# def Singleton(cls):
#     _instance = {}
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]
#     return _singleton
# @Singleton
# class A(object):
#     a = 1
#     def __init__(self, x=0):
#         self.x = x
# a1 = A(2)
# a2 = A(3)
# def one(func):
#     print('----1----')
#     def two():
#         print('----2----')
#         func()
#         print('_________3____________')
#     return two
#
# def a(func):
#     print('----a----')
#     def b():
#         print('----b----')
#         func()
#         print('_________c______________')
#     return b
#
# @one #demo = one(a(demo))
# @a  #demo = a(demo)
# def demo():
#     print('----4----')
#
# demo()
# def Singleton(cls):
#     _instance = {}
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             print(0)
#             _instance[cls] = cls(*args, **kargs)
#             print(2)
#         return _instance[cls]
#     return _singleton
# @Singleton  #  A = singleton(A)
# class A(object):
#
#
#     def __init__(self, x=0):
#         a = 1
#         print(a)
#         self.x = x
# a1 = A()

# class Dec(object):
#
#     def __init__(self, fun):
#         self.fun = fun
#
#     def __call__(self, *args, **kwargs):
#         print("这是一个装饰器")
#
#         self.fun(*args, **kwargs)
#         print("晚饭臭豆腐")
# @Dec  # test = Dec(test)
# def test(x, y):
#     res = x + y
#     print(res)
# test(6, 7)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again   ")
#
#         raise Exception
#
# import time
# a = time.time()
# print(a)

# def htest():
#     i = 1
#     while i < 4:
#         n = yield i
#         if i == 3:
#             return 100
#         i += 1
#
#
# def itest():
#     val = yield from htest()
#     print('>>>>>>>',val)
#
# t = itest()
# t.send(None)
# j = 0
# while j < 3:
#     j += 1
#     try:
#         t.send(j)
#     except StopIteration as e:
#         print('异常了')

# def check_username(req):
#     if req.method == "POST":
#         msg = {'count': 0, 'msg': ''}
#         username = req.POST.get('username')
#         if re.findall('[A-Za-z0-9_\-\u4e00-\u9fa5]+', username):
#             obj_list = models.UserInfo.objects.filter(username=username)
#             if obj_list:
#                 msg['count'] = 1
#                 msg['msg'] = '用户名已被注册'
#         else:
#             msg['count'] = 1
#             msg['msg'] = '用户名格式不正确'
#         return JsonResponse(msg)
# def check_password(req):
#     if req.method == "POST":
#         password = req.POST.get('password')
#         msg = {'count': 0, 'msg': ''}
#         if len(password) != 0:
#             if len(password) < 8:
#                 msg['count'] = 1
#                 msg['msg'] = '密码长度不足'
#             msg['msg'] += ' 密码必须包含'
#             if not re.findall(r"[0-9]+", password):
#                 msg['count'] = 1
#                 msg['msg'] += ' "数字"'
#
#             if not re.findall(r'[a-z]+', password):
#                 msg['count'] = 1
#                 msg['msg'] += '"字母"'
#
#             if not re.findall(r'([^a-z0-9A-Z])+', password):
#                 msg['count'] = 1
#                 msg['msg'] += '"特殊字符"'
#
#         return JsonResponse(msg)






