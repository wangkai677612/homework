import numpy as np

colors=('红桃','黑桃','方片','草花')
marks=('A','2','3','4','5','6','7','8','9','10','J','Q','K')

list1 = np.hstack((np.arange(1,14).reshape((13,1)),np.arange(1,14).reshape((13,1))))
list1 = np.hstack((list1,list1))

for x in range(4):
    for y in list1[:,x]:
        print(colors[x]+marks[y-1],end=" ")

import random;

print("\n\n洗牌以后:\n\n")
list2= random.sample(range(52),52)
for x in list2:
    result1=divmod(x,4)
    print(colors[result1[1]]+marks[result1[0]],end=" ")
    

print("\n\n分到的一手牌是\n\n") 
list4color=[]
list4marks=[]
list3= random.sample(range(52),5)
for x in list3:
    result1=divmod(x,4)
    list4color.append(result1[1])
    list4marks.append(int(result1[0]))
    print(colors[result1[1]]+marks[result1[0]],end=" ")
    

#梳理牌顺序
list4marks.sort()
list4color.sort()

marksstr=''
colorstr=''
for x in list4marks :     
    marksstr=marksstr+marks[x]
    
for x in list4color :     
    colorstr=colorstr+str(x)    
    
print(colorstr)
print(marksstr)


#用正则表达式定义游戏规则

#判断是否是同花
import re

if(re.search(r'([\d])\1{4,}', colorstr)):
    print('同花',end='')
    

#判断是否是顺子

if (marksstr=='A2345') or (marksstr=='910JQK') or (marksstr=='8910JQ') or (marksstr=='78910J') or (marksstr=='876910'):
    print('顺子',end='')
    
if re.search(r'(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)){4}\d', marksstr):
    print('顺子',end='')

             
#判断是否是4条
if(re.search(r'([0-9A-Z])\1{3,}', colorstr)):
    print('4条',end='')


#判断是否是4条
if(re.search(r'([0-9A-Z])\1{3,}', colorstr)):
    print('4条',end='')
    
#判断是否是满堂红
if(re.search(r'([0-9A-Z])\1{2,}', marksstr[:3])) and (re.search(r'([0-9A-Z])\1{1,}', marksstr[3:])):
    print('满堂红',end='')

#判断是否是满堂红
if(re.search(r'([0-9A-Z])\1{1,}', marksstr[:2])) and (re.search(r'([0-9A-Z])\1{2,}', marksstr[2:])):
    print('满堂红',end='')
