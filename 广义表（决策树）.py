class treenode(object):
    def __init__(self):
        self.choice='#'
        self.reflect='#'
        self.child = []
class tree(treenode):
    def creat_tree(self,tree,x):
        if x=='#':
            tree = None
        else:
            tree.data=x
            while(1):
                x=input("input")
                if x=='$':
                    break
                else:
                    tree_c=tree()
                    tree.creat_tree(tree_c,x)
                    self.child.append(tree_c)

    def visit_tree(self,tree):
        stack=[]
        tag=1
        if tree!=None:
            stack.append([tree,tag])
        while len(stack)!=0:
            tem=stack.pop(0)
            tem_t=tem[0]
            print(tem_t.data)
            for i in range (len(tem_t.child)):
                stack.append([tem_t.child[i],0])
            if tem[1]==1:
                tem=stack.pop()
                tem[1]=1
                stack.append(tem)
            
            
