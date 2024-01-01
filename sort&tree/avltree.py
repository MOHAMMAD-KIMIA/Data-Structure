#avl tree should have balance factor of -1,0,1
#balance factor=height of left-height of right
class Node(object):
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.height=1

class AVL_Tree(object):
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key<root.data:
            root.left=self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key) 

        #update the height of the node
        root.height=1+max(self.getheight(root.left), 
                           self.getheight(root.right)) 
        # update the balance factor 
        balance=self.getbalancefactor(root) 
  
        #check if the node is balance or not
        #if not, go check these 4 cases
        #case 1
        if balance>1 and key<root.left.data: 
            return self.rightrotate(root) 
  
        #case 2  
        if balance<-1 and key>root.right.data: 
            return self.leftrotate(root) 
  
        #case 3 
        if balance>1 and key>root.left.data: 
            root.left=self.leftrotate(root.left) 
            return self.rightrotate(root) 
  
        #case 4 
        if balance<-1 and key<root.right.data: 
            root.right=self.rightrotate(root.right) 
            return self.leftrotate(root) 
  
        return root  
    

    def delete(self,root,key):
        if not root:
            return Node(key)
        elif key<root.data:
            root.left=self.delete(root.left,key)
        elif key>root.data:
            root.right = self.delete(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp=self.minvalue(root.right)
            root.key=temp.value
            root.right=self.delete(root.right,temp.key)
        if root is None:
            return root
        root.height=1+max(self.getheight(root.left),self.getheight(root.right)) 
        balance=self.getbalancefactor(root)
 
        # Balance the tree
        if balance>1:
            if self.getbalancefactor(root.left)>=0:
                return self.rightrotate(root)
            else:
                root.left=self.leftrotate(root.left)
                return self.rightrotate(root)
        if balance<-1:
            if self.getbalancefactor(root.right)<=0:
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right)
                return self.leftrotate(root)
        return root
    

    def getheight(self,root):
        if root is None:
            return 0
        else:
            return root.height  
        

    def getbalancefactor(self,root):
        if root is None:
            return 0
        else:
            return self.getheight(root.left)-self.getheight(root.right)
        

    def minvalue(self,root):
        if root is None or root.left is None:
            return root
        return self.minvalue(root.left)
        
    
    def rightrotate(self, z): 
        y = z.left 
        T3 = y.right 
        #rotation 
        y.right = z 
        z.left = T3 
        z.height = 1 + max(self.getheight(z.left), 
                        self.getheight(z.right)) 
        y.height = 1 + max(self.getheight(y.left), 
                        self.getheight(y.right)) 
        return y 
    
    def leftrotate(self, z): 
        y = z.right 
        T2 = y.left 
        #rotation 
        y.left = z 
        z.right = T2  
        z.height = 1 + max(self.getheight(z.left), 
                         self.getheight(z.right)) 
        y.height = 1 + max(self.getheight(y.left), 
                         self.getheight(y.right)) 
        return y 




