from random import randint

#原始数据
words = ("static","abstract","extends","implements","throw","orange","student","select","group","interface");

#随机选中的单词，猜测中的单词，单词掩码
randomIndex = randint(0,len(words)-1)
selectedWord=words[randomIndex]
wordNow='-'*len(selectedWord)
wordNowMask=selectedWord

print(wordNowMask)
print("你要猜的单词是这样的：",wordNow)

#计数器
userTimes = 5;


while(True):
    strGuess=input("你有"+str(userTimes)+"次猜测机会")
    
    if len(strGuess) != 1 or strGuess == '-' :
        print("请输入一个字母")
        
    else:
        index=wordNowMask.find(strGuess)
        
        if index >=0 :
            
            wordNow=wordNow[0:index]+strGuess+wordNow[index+1:]
            wordNowMask=wordNowMask[0:index]+'-'+wordNowMask[index+1:]
            
            print("你又猜对了一个字母，继续努力，当前结果是：",wordNow)
            if wordNowMask == '-'*len(wordNowMask):
                print("你真聪明，搞定，收工")
                break
            continue
     
    userTimes =userTimes- 1
    if userTimes <= 0 :
        print("任务失败")
        break;
    
