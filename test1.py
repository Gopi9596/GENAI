# a = 5
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a//b)
# # print(a+b)

# a = int(input('enter your number'))
# if a>=6:
#     print('sucess')
# else:
#     print("failed")

# x = ['man','women']
# y = ['man','women']
# z =x
# print(x is y)
# print(z is x)
# a = 5
# b =6
# # print(a|b)

# a = ['pencial','pen','cover','pen','rest']
# a.sort(reverse=True)

# print(a)
# a.insert(0,'book')
# a.remove('pen')
# del a[0]
# for i in a:
#     print(i)
# only for if use chesinapudu
# b = ['congrats' for i in a if i=='hyd']
# # 
# print(b)
# a = {'pen','pencial','mango','banana','pen','mango',3,3,2.6}
# # a = list(a)
# # a[0:2]=['kiwi','gopi']
# print(a)

# a={'name':'kandukur',
#    'year':2026,
#    'est':1950,
#    'famous':'vegitables',
#    'year':2020

# }
# # print((a.values()))
# for x,y in a.items():
#     print('keys are ;',x)
#     print('values are:',y)


#     b,a,b,a,

# a = int(input('enter your marks'))
# if a>=90:
#    print('A grade')
# elif a>=80 or a<90:
#    print('B grade')
# elif a>=70 or a<80:
#    print('C grade')
# elif a>=60 or a<70:
#    print('D grade')
# else:
#    print('not eligible')
# age=int(input('enter your age :'))
# a = (input('enter your color :'))
# match a:
#     case 'red' if age>=18:
#         print('take dosa')
#     case 'green' if age>=18:
#         print('take meals')
#     case 'blue' if age>=18:
#         print('take water bottle')
#     case _:
#         print('Invalid color or age ')

# i = 0
# while i<30:
#     print(i)
#     i=i+2

# def my_fun(a,b):
#     if a>=20:
#         c=a+b
#         print(c)
#     else:
#         print('try again')
# my_fun(50,30)

# def kdkr(name='book'):
#     print('my ame is :',name)
# kdkr('gopi')

# import pandas
# a = pandas.series([1,2,3,4])
# print(a)
# try:
#     a = 20
#     b = 100
#     print(b/a)
# except ZeroDivisionError:
#     print('divise number is zero so it is not valid')
# except:
#     print('someting is missing')
# finally:
#     print('my task is completed')
# x = ('mango','banana','apple')
# y = iter(x)
# print(next(y))
# print(next(y))
# print(next(y))

# self.b = b
#     def land(self):
#         print('i have a land property')
#     def building(self):
#         print('i have building')
# class child(parent):
#     def __init__(self,a,b,c):
#         super().__initclass parent:
#     def __init__(self,a,b):
#         self.a = a
#         __(a,b)
#         self.c=c
#     def car(self):
#         print('i have car')
# obj = child('10 acr land','10 floor building','red car')
# print(obj.building())
# print(obj.car())
# print(obj.car())

# class father:
#     def __init__(self,a,b):
#         self.a = a
#         self.b=b
#     def own_house(self):
#         print('i have own house')
# class mother:
#     def __init__(self,c):
#         self.c = c
#     def car(self):
#         print('i have car')
# class child(father,mother):
#     def __init__(self,a,b,c,d):
#         father.__init__(a,b,c)
#         mother.__init__(a,b,c)
#         self.d = d
#     def cycle(self):
#         print('i have a cycle')
# obj = child('resurt&home','bmw car','gare cycle')
# print(object.own_house())
# print(object.car())
# print(object.cycle())

# class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def deposit(self):
#         print(f'iam depositing the amount of {self.a}')
# class village(kdkr):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#     def withdraw(self):
#         print(f"my withdraw amount is {self.c}")
# obj = village(10,20,30)
# obj.withdraw()


# class father:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def eat(self):
#         print(f'father eating {self.a} at surya restaurant')

# class son(father):
#     def __init__(self, a, b, c):
#         father.__init__(self, a, b)
#         self.c = c

#     def read(self):
#         print(f'my dad eating {self.a}, beside that I am reading {self.c} book')

# class daughter(father):
#     def __init__(self, a, b, c, d):
#         father.__init__(self, a, b)
#         self.c = c
#         self.d = d

#     def write(self):
#         print(f'my brother is reading {self.c}, beside my brother I am writing {self.d}')

# obj = daughter('chicken biriyani', 'gopi', 'novels', 'class home work')
# obj.write()
# obj.eat()

# class elimentry:
#     # def __init(self,sname,slot):
#     #     self.sname=sname
#     #     self.slot=slot
#     def study(self):
#         print(f'studying 1st class')
# class university:
#     # def __init(self,pen,paper):
#     #     self.pen=pen
#     #     self.paper=paper
#     def study(self):
#         print('iam studying btech')
# x=[elimentry(),university()]
# for i in x:
    # i.study()