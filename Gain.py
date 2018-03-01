import math
'''
训练集（色泽，根蒂，敲声，纹理，脐部，触感，好瓜）
色泽：1青绿，2乌黑，3浅白
根蒂：1蜷缩，2稍蜷，3硬挺
敲声：1浊响，2沉闷，3清脆
纹理：1清晰，2稍模，3模糊
脐部：1凹陷，2稍凹，3平坦
触感：1硬滑，2软粘
'''
train_set=  (
	 (  1,1,1,1,1,1,1),
         (  2,1,2,1,1,1,1),
         (  2,1,1,1,1,1,1),
         (  1,1,2,1,1,1,1),
         (  3,1,1,1,1,1,1),
         (  1,2,1,1,2,2,1),
         (  2,2,1,2,2,2,1),
         (  2,2,1,1,2,1,1),
         (  2,2,2,2,2,1,0),
         (  1,3,3,1,3,2,0),
         (  3,3,3,3,3,1,0),
         (  3,1,1,3,3,2,0),
         (  1,2,1,2,1,1,0),
         (  3,2,2,2,1,1,0),
         (  2,2,1,1,2,2,0),
         (  3,1,1,3,3,1,0),
         (  1,1,2,2,2,1,0))

def Ent(train_set,state_num,sample_num=17,aim=6):
    '''
    train_set privide data
    state_number determine its coll
    '''
    ent_list=[]
    count_list=[]
    re_list=[]
    count1=[]
    count2=[]
    for i in range(4):##这个情况先写4，事后优化
        count1.append(0);
        count2.append(0);
    if(state_num!=aim):#不是最后的正负
        for i in range(sample_num):
            if (train_set[i][6]==1):
                count1[train_set[i][state_num]]=count1[train_set[i][state_num]]+1
            else:
                count2[train_set[i][state_num]]=count2[train_set[i][state_num]]+1
    else:
        for i in range(sample_num):
            if(train_set[i][6]==1):
                count1[0]=count1[0]+1
            else:
                count2[0]=count2[0]+1
    #print(count1)
    #print(count2)
    for i in range(4):##这个情况先写4，事后优化（sample_num,应该为，state的数量加个1）
        D=0;
        count=count1[i]+count2[i]
        if (count1[i]!=0):
            tem=count1[i]*1.0/count
            D=D-tem*math.log(tem,2)
        if (count2[i]!=0):
            tem=count2[i]*1.0/count
            D=D-tem*math.log(tem,2)
        #if(D!=0):
        if (count2[i]!=0)|(count1[i]!=0):
           ent_list.append(D)
           count_list.append(count)
    re_list.append(ent_list)
    re_list.append(count_list)
    return re_list

def Gain(train_set,state_num,aim=6):
    Ent_D=Ent(train_set,6,len(train_set))[0][0]
    G=Ent_D
    sample_num=len(train_set)
    Ent_state=Ent(train_set,state_num,sample_num)
    #print(Ent_state)
    for i in range(len(Ent_state[0])):
        #print(Ent_state[1][i]/sample_num*Ent_state[0][i])
    
        G=G-Ent_state[1][i]/sample_num*Ent_state[0][i]
    return G

def Gain_rate(train_set,state_num,aim=6):
    Ent_D=Ent(train_set,6,len(train_set))
    G=Ent_D[0][0]
    IV=1#原本为0 但是担心除数为0
    sample_num=len(train_set)
    Ent_state=Ent(train_set,state_num,sample_num)
    #print(Ent_state)
    for i in range(len(Ent_state[0])):
        #print(Ent_state[1][i]/sample_num*Ent_state[0][i])
        tem=Ent_state[1][i]/sample_num
        IV=IV-(tem*math.log(tem,2))
        G=G-Ent_state[1][i]/sample_num*Ent_state[0][i]
    #print(":")
    #print(IV)
    try:
        G=G/IV
    except(IOError,ZeroDivisionError):
        print("error")
        print(train_set)
        print(state_num)
        exit()
    return G
