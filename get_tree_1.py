import Gain as rate

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
train_list=[]
train_list.append(train_set[0])
train_list.append(train_set[1])
train_list.append(train_set[2])
train_list.append(train_set[5])
train_list.append(train_set[6])
train_list.append(train_set[9])
train_list.append(train_set[13])
train_list.append(train_set[14])
train_list.append(train_set[15])
train_list.append(train_set[16])
test_list=[]
test_list.append(train_set[3])
test_list.append(train_set[4])
test_list.append(train_set[7])
test_list.append(train_set[8])
test_list.append(train_set[10])
test_list.append(train_set[11])
test_list.append(train_set[12])
def get_state(aclist,aim=6):
    gr_max=[0,-1]
    for i in range(6):
        tem=rate.Gain_rate(aclist,i,aim)
        #print(tem)
        if gr_max[0]<tem:
            gr_max[0]=tem
            gr_max[1]=i
    #print(gr_max)
    return gr_max[1]

def get_tree(train_list,test_list,aim=6):
    R=[0]
    #R.append(train_list)
    R[0]=get_state(train_list,aim)
    #print(R[0])
    tem=rate.Ent(train_list,R[0],len(train_list),aim)
    #print(tem)
    R.append(len(tem[0]))
    count=0
    pre_rate=0
    ##calculate the attribut of train_list
    for i in range(len(train_list)):
        if train_list[i][aim]==1:
            count=count+1
        else:
            count=count-1
    if count>=0:
        R.append(1)
    else:
        R.append(0)
    #count FREE
    #获得sit[[train_set,test_set,+/-,success,]]
    sit=[]
    for i in range(3):
       sit.append([[],[]])
    #完成头两个值的处理
       count1=0
    for i in range(len(train_list)):
        #print(train_list[i][R[0]]-1,i)
        sit[train_list[i][R[0]]-1][0].append(train_list[i])
    for i in range(len(test_list)):
        sit[test_list[i][R[0]]-1][1].append(test_list[i])
    for i in range(3):
        if sit[i]==[]:
            continue
        count=0
        tem=sit[i][0]
        for j in range(len(tem)):
            tem[j][aim]==1
            count=count+1
        if count>=(len(tem)/2):
            sit[i].append(1)
        else:
            sit[i].append(0)
        tem=sit[i][1]
        forsee=sit[i][2]
        count=0
        for j in range(len(tem)):
            tem[j][aim]==forsee
            count=count+1
            count1=count1+1
        sit[i].append(count)
    ###完成数值分类
    ###获得pre_rate,和new_rate
    count=0
    new_rate=1
    for i in range(len(train_list)):
        if train_list[i][6]==R[2]:
            count=count+1
    pre_rate=count/len(train_list)
    if(len(test_list)!=0):#等待可能的修正，将new_rate改为总体的rate而非test的rate
        new_rate=count1/len(test_list)
    ###
    if(new_rate>pre_rate)&(R[1]!=1)&(R[0]!=-1):
        for i in range(R[1]):
            tem=get_tree(sit[i][0],sit[i][1])
            #print(tem)
            R.append(tem)
    return R
            
                
            
    
    
        
