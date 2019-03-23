
#统计英文词频函数

#将代码封装入函数
def stats_text_en():                
    import d5_exercise_stats_text
    
#定义注释函数
def annotation(string) -> '''This is a text''':     #用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 

stats_text_en()         

docstr=stats_text_en.__doc__    #使用文本文档属性函数

annotation(docstr)              #对文本文档进行注释


#统计中文词频函数

cndic={}                        #初始化一个空的字典

def stats_text_cn(checkstr):    #定义检索中文函数
    for i in checkstr:
        if u'\u4e00' <= i <= u'\u9fff':
            cndic[i] = checkstr.count(i)
    return cndic

#一个中英混杂的文本
text = '''                       
we got two trucks leaving the target building
 我们发现有两辆卡车正要离开目标建筑
 you're clear to engage to ruin vehicle
 你们可以摧毁车辆了
 Don't let the trucks get away!
 不要让那些卡车跑了!
 bloody Gawain... Get your car
 血腥高文...上你的车!
 get back to the room!
 回到房里去!

 we have been let the vehicle
 我们已经摧毁了那辆车!

 move your back
 快回来
 we're running to the house now
 我们现在要冲到房子里
 clear the side past
 扫清侧廊的敌人
 go go
 走走

'''

stats_text_cn(text)            


print(cndic)                           

annotation(cndic)     