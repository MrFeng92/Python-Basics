from collections import namedtuple

# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# user=User(name='Tom',age=22)
# print(user.name,user.age)

# 使用namedtuple实现user对象创建
# namedtuple比class更节省空间，少了class很多内置变量
User=namedtuple("User",["name","age","height"])
user=User(name="Tom",age=30,height=172)
print(user.name,user.age,user.height)

User=namedtuple("User",["name","age","height","edu"])
user_tuple=("Tom",22,173)
user=User(*user_tuple,"master")
print(user.name,user.age,user.height)

# 函数参数
def ask(*args,**kwargs):
    pass

# ask("Tom",12)  不指定name会都赋值给args
# ask(name="Tom",age=25) 指定name会到kwargs

user_dict={
    "name":"Tom",
    "age":29,
    "height":175
}
user2=User(**user_dict,edu="master")
print(user.name)

# user2._asdict() 将Tuple转成dict
# user2._make(user_tuple) 传入可迭代对象生成user对象


