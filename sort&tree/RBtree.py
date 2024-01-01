class Node:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None
        self.color=1 #1=red , 0=black


class RB_Tree:
    def __init__(self):
        self.null=Node(0)
        self.null.color=0
        self.null.left=None
        self.null.right=None
        self.root=self.null

    #insert a new node
    def insertnode(self,key):
        newnode=Node(key)
        newnode.parent=None
        newnode.val=key
        newnode.left=self.null
        newnode.right=self.null
        newnode.color=1

        y=None
        x=self.root
        #find new node's position
        while x!=self.null:
            y=x
            if newnode.val<x.val:
                x=x.left
            else:
                x=x.right

        newnode.parent=y
        #if parent is none then newnode is root
        if y==None:
            self.root=newnode
        elif newnode.val<y.val:
            y.left=newnode
        else:
            y.right=newnode

        if newnode.parent==None:
            newnode.color=0
            return
        
        if newnode.parent.parent==None:
            return
        
        self.fix_insert(newnode)

    def leftrotate(self,x):
        y=x.right
        x.right=y.left
        if y.left!=self.null:
            y.left.parent=x
        y.parent = x.parent                              
        if x.parent == None :                            
            self.root = y                                
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightrotate(self,x):
        y=x.left                                       
        x.left=y.right                                
        if y.right!=self.null:
            y.right.parent=x
        y.parent=x.parent                              
        if x.parent==None :                            
            self.root=y                                
        elif x==x.parent.right:
            x.parent.right=y
        else :
            x.parent.left=y
        y.right=x
        x.parent=y


    def fix_insert(self,k):
        while k.parent.color==1:                       
            if k.parent==k.parent.parent.right:         
                u=k.parent.parent.left                 
                if u.color==1:                          
                    u.color=0                           
                    k.parent.color=0
                    k.parent.parent.color=1             
                    k=k.parent.parent                   
                else:
                    if k==k.parent.left:              
                        k=k.parent
                        self.rightrotate(k)                       
                    k.parent.color=0
                    k.parent.parent.color=1
                    self.leftrotate(k.parent.parent)
            else:                                         #if parent is left child of its parent
                u=k.parent.parent.right                 
                if u.color==1:                          
                    u.color=0                          
                    k.parent.color=0
                    k.parent.parent.color=1             
                    k=k.parent.parent                   
                else:
                    if k==k.parent.right:             
                        k=k.parent
                        self.leftrotate(k)                       
                    k.parent.color=0
                    k.parent.parent.color=1
                    self.rightrotate(k.parent.parent)             
            if k==self.root:                            
                break
        self.root.color=0                           


    def fixDelete (self,x) :
        while x!=self.root and x.color==0:          
            if x==x.parent.left:                      
                s=x.parent.right                      
                if s.color==1:                         
                    s.color=0                           
                    x.parent.color=1                    
                    self.leftrotate(x.parent)                  
                    s=x.parent.right
                if s.left.color==0 and s.right.color==0:
                    s.color=1              
                    x=x.parent
                else:
                    if s.right.color==0:              
                        s.left.color=0                 
                        s.color=1                       
                        self.rightrotate(s)                     
                        s=x.parent.right
                    s.color=x.parent.color
                    x.parent.color=0                  
                    s.right.color=0
                    self.leftrotate(x.parent)                 
                    x=self.root
            else:                                        # If x is right child of its parent
                s=x.parent.left                     
                if s.color==1 :                         
                    s.color=0                           
                    x.parent.color=1                
                    self.rightrotate(x.parent)             
                    s=x.parent.left

                if s.right.color==0 and s.right.color==0:
                    s.color=1
                    x=x.parent
                else:
                    if s.left.color==0:                # If left child of s is black
                        s.right.color=0                 
                        s.color=1
                        self.leftrotate(s)                 
                        s=x.parent.left
                    s.color=x.parent.color
                    x.parent.color=0
                    s.left.color=0
                    self.rightrotate(x.parent)
                    x=self.root
        x.color=0


    #transplanting nodes
    def transplant(self,u,v):
        if u.parent==None:
            self.root=v
        elif u==u.parent.left:
            u.parent.left=v
        else:
            u.parent.right=v
        v.parent=u.parent


    def minimum(self,node):
        while node.left!=self.null:
            node=node.left
        return node


    # Function to handle deletion
    def delete(self,node,key):
        z=self.null
        while node!=self.null:                        
            if node.val==key:
                z=node
            if node.val<=key:
                node=node.right
            else:
                node=node.left
        if z==self.null:                                
            print("error")
            return
        y=z
        y_org_color=y.color                          
        if z.left==self.null :                          
            x=z.right                                     
            self.transplant(z,z.right)         
        elif(z.right==self.null) :                       
            x=z.left                                      
            self.transplant(z,z.left)            
        else:                                            
            y=self.minimum(z.right)                  
            y_org_color=y.color                  
            x=y.right
            if y.parent==z:                              
                x.parent=y                                
            else:
                self.transplant(y,y.right)
                y.right=z.right
                y.right.parent=y
            self.transplant(z,y)
            y.left=z.left
            y.left.parent=y
            y.color=z.color
        if y_org_color==0:                          
            self.fixDelete(x)


    # Deletion of node
    def delete_node ( self , val ) :
        self.delete( self.root , val )         # Call for deletion

