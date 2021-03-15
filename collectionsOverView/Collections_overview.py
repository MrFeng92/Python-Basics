_author_='fengshuang'

from collections import *

# 抽象基类,相当于Java里面的Interface
from collections.abc import *

user_tuple=('小刚',29,172,'beijing')
name,age,height,city=user_tuple
# 元组拆包，一一对应自动匹配类型
print(name,age,height)

name,*other=user_tuple
print(name,other)

user_dict={}
user_dict[user_tuple]="tom"
user_dict[['小刚',29,172,'beijing']]='mary'
pass


