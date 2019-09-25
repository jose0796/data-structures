#!/usr/bin/python3
###################################################################
###
### Author: Jose Moran 
### Email : jmoran071996@gmail.com
### Github: jose0796
### Description: Binary Search Tree implementation for
### illustrative and self-educational purposes. It is 
### based on:
### 
###  Intro to Algorithms, Thomas H. Cormen, 3rd Ed., p286
### 
###
###
####################################################################


class node:

    """ 
        Node object 

        Contains fundamental data about a node 
        in the subsequent BST implementation 
    
    
    """

    def __init__(self,val):
        self.key = val
        self.p = None 
        self.right = None
        self.left = None
        self.height = -1 # avl augmentation
        self.bf = 0

class nil(node):

    def __init__(self):
        super().__init__(-100000000)

class tree:

    def __init__(self):
        self.nil = nil()
        self.root = self.nil

class bst(tree):

    """ 
    
        Binary-Search Tree class object 

        It represents a complete vanilla BST object with 
        most basic operations (no DS-augmentation)
    
    
    """
        

    def inorder_walk(self,key):

        """ 
        
            Prints the tree in decreasing order 

            ex: 

                       ( y )
                      /     \ 
                    ...     ...
                    /         \ 
                  (x2)        (z2)
                  /  \        /  \ 
               (x1) (x3)   (z1)  (z3)
                /      \    /      \  
               NIL    NIL  NIL     NIL


            would print ... 

                x1 x3 x2 ... y ... z1 z2 z3
        
            @param int key      key from which to init the walk

            time-complexity: O(n)
            space-complexity: O(1)
        
        """
        
        def __inorder__(x):
            if x != self.nil:
                __inorder__(x.left)
                print(x.key)
                __inorder__(x.right)
            
        __inorder__(self.search(key))

    def insert(self,k):

        """ 
            Inserts in the appropiate position a given key 
            while maintaining the bst-property

            insert(10):

                          ( 15 )            // 10 < 15 --> left
                       /         \  
                    (13)         (17)       // 10 < 13 --> left
                   /   \        /    \ 
                 (9)  (14)    (18)   (19)   // 10 > 9 --> right
                /  \  /  \    /  \   /  \ 
               NIL  NIL  NIL(17)  NIL   (21)


            turns into -->

                          ( 15 )            // 10 < 15 --> left
                       /         \  
                    (13)          (17)       // 10 < 13 --> left
                   /   \         /    \ 
                 (9)  (14)     (18)   (19)   // 10 > 9 --> right
                /  \           /  \   /  \ 
              NIL  (10)     (17)  NIL   (21)

            
            @param int k    key to be inserted        
            Time-complexity: O(h)
            Space-complexity: O(1)
        
        """

        z = node(k)
        y = self.nil
        x = self.root


        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else: x = x.right

        z.p = y
        if y == self.nil:
            self.root = z 
        elif z.key < y.key:
            y.left = z
        else: y.right = z

        z.right = self.nil
        z.left = self.nil


    def search(self,key):


        """ 
            The procedure begins its search at the root and traces 
            a simple path downwards comparing the key to each node.

            search(19): 

                         ( 15 )         // 19 > 15 --> right 
                       /         \  
                    (13)         (17)   // 19 > 17 --> right
                   /   \        /    \ 
                 (9)  (14)    (18)   (19) // 19 == 19 --> return  
                /  \  /  \    /  \   /  \ 
               NIL  NIL  NIL(17)  NIL   (21)


            @param int key      key of node 
            @return node n      reference to the node that contains such key

            time-complexity: O(h)
            spaced-complexity: O(1)

        """


        def __search__(nod,key):

            if nod == self.nil or nod.key == key:
                return nod
            elif nod.key < key: 
                return __search__(nod.right, key)
            else:
                return __search__(nod.left, key)
        
        return __search__(self.root,key)
    
    def min(self,x):

        """ 
            Calculates minimun element of the tree 

            @return node x
            time-complexity: O(h)
            space-complexity: O(1)
        
        """

        
        while x.left != self.nil:
            x = x.left
        return x

    def max(self,x):

        """ 
            Calculates maximun element of the tree 

            @return node x 

            time-complexity: O(h)
            space-complexity: O(1)

        """

        
        while x.right != self.nil:
            x = x.right
        return x


    def succ(self,x):


        """ 
        
            The successor of a node x is the node with the 
            smallest key greater than x.key

            case 1:
                      ( x )
                         \      (x.right != NIL)
                        ( y )
                         /  \ 
                       ...  ...
                       / 
                 succesor(x)

            case 2:
                    if (x.right == NIL)

                     
                successor(x) 
                    /  
                 ( z ) 
                    \   
                    ...  
                      \  
                     ( y )   
                        \ 
                       ( x )
                       /   \ 
                     ...   NIL          

            @param int key      key to calculate successor 
            @param node n       reference to the successor node     

            time-complexity: O(h)
            space-complexity: O(1)       

        
        """
        
        if x.right != self.nil: #case 1
            return self.min(x.right)
        
        #case 2
        y = x.p
        while y != self.nil and y.right == x:
            x = y
            y = y.p

        return y

    def delete(self,z):
        
        """ 
        
            The overall strategy for deleting a node z 
            from a BST has 3 basic cases: 


            1. If z has no children, then we simply remove it 
            by modifying its parent to replace z with NIL as 
            its child. 

            2. If z has one child, then we elevate that child to 
            take z's position in the tree by modifying z's parent
            to replace z by z's child.

            3. If z has two children, then we find z's successor y 
            which must be on z's right subtree, and have y take z's 
            position in the tree. The rest of z's original right sub
            tree becomes y's new right subtree, and z's left subtree 
            becomes y's new left subtree

            @param int key      key of node to be remove
            
            time-complexity: O(h)
            space-complexity: O(1)
        
        """

        def transplant(u,v):

            """ 
                Sub procedure to replace u's subtree with 
                v's subtree 
            
            """
            if u.p == self.nil:
                self.root = v
            elif u == u.p.left:
                u.p.left = v 
            else:
                u.p.right = v
            if v != self.nil:
                v.p = u.p

        
        


        if z != self.nil:
            if z.left == self.nil:
                transplant(z,z.right)
                    
            else:
                if z.right == self.nil:
                    transplant(z,z.left)
                else:
                    y = self.succ(z)
                    if y.p != z:
                        transplant(y,y.right)
                        y.right = z.right 
                        y.right.p = y
                    
                    transplant(z,y)
                    y.left = z.left 
                    y.left.p = y


    def __str__(self):
        s = ""
        def tabs(b):
            
            s = ""
            for x in b:
                if x:
                    s += " \u2502"
                else:
                    s += "  "
            return s
            
        def show(x,b):
            s = ""
            if x != self.nil:
                s += "[" + str(x.key) + "]\n"
                s += tabs(b)
                s += " \u251c"
                b.append(True)
                s += show(x.right,b)
                b.pop()

                s += tabs(b)
                s += " \u2514"
                b.append(False)
                s += show(x.left,b)
                b.pop()

            else:
                s += " |\n"
            return s
                

        b = []
        
        s = show(self.root,b)
        return s
       
class avl(bst):

    """ 
        AVL tree implementation 

        Is a self-balancing binary search tree. 
        In an AVL tree, the heights of the two child
        subtrees of any node differ by at most one.    
    
    """



    def __update_balance__(self,x):

        """ 
            
            Updates balances of nodes starting from x
            and going up on the tree levels

        """

        while x != self.nil:
            x.bf = self.__get_balance__(x)
            x = x.p

    def __update_height__(self,x):

        """ 
        
            Updates heights of nodes starting from 
            node x and going up on the tree levels 
        
        """

        while x != self.nil:
            x.height = max(x.right.height, x.left.height) + 1
            x = x.p

    def insert(self,k):

        """
            time-complexity: O(log n)
            space-complexity: O(1)

        """

        # BST insertion 

        z = node(k)
        y = self.nil 
        x = self.root 

        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else: 
                x = x.right 

        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.right = self.nil
        z.left = self.nil

        # rebalancing part

        self.__update_height__(z)
        self.balance(z)





    def delete(self,z):


        #PART 1: BST delete algorithm
        def transplant(u,v):
            if not u.p:
                self.root = v
            elif u == u.p.left:
                u.p.left = v 
            else:
                u.p.right = v
            if v:
                v.p = u.p


        if z != self.nil:

            x = self.nil


            if z.left == self.nil:
                x = z.right 
                transplant(z,z.right)
   
            else:
                if z.right == self.nil:
                    x = z.left 
                    transplant(z,z.left)

                else:
                    y = self.succ(z)
                    x = y
                    if y.p != z:
                        x = y.p
                        transplant(y,y.right)
                        y.right = z.right 
                        y.right.p = y

                    transplant(z,y)
                    y.left = z.left 
                    y.left.p = y

            #PART 2: adjust tree balance
            self.__update_height__(x)
            self.__update_balance__(x)
            self.__balance_deletion__(x)
                    

    def __get_balance__(self,x):

        """ 

            Calculate balance of node 
            based on heights 
        
        """


        if x == self.nil:
            return 0
        else:
            return x.right.height - x.left.height

    def leftRotate(self,x):

        """ 
        
            A left rotation is performed when the right subtree of 
            a node is heigher by at least 2 levels than the left 
            subtree of that node. 


                           /                                  /
                         ...                                ...
                         /                                  /
                        x           ====>                  y
                      /   \                              /   \ 
                    ...    y                           x       w
                          /  \                       /   \    /  \ 
                         z    w                    ...   z  ...  ... 
                        / \    \                        /  \ 
                      ... ...  ...                    ...  ...

        """
        
        y = x.right 
        x.right = y.left 
        if y.left != self.nil:
            y.left.p = x
        
        y.p = x.p 
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        elif x == x.p.left:
            x.p.left = y

        y.left = x
        x.p = y

        #update balance 
        self.__update_height__(x)
        x.bf = self.__get_balance__(x)
        y.bf = self.__get_balance__(y)

    def rightRotate(self,x):

        """ 
        
            A right rotation is performed when the left subtree of 
            a node is heigher by at least 2 levels than the right
            subtree of that node. 


                           /                                   /
                         ...                                 ...
                         /                                   /
                        x           ====>                   y
                      /   \                               /   \ 
                     y    ...                            z     x
                   /  \                                /     /  \ 
                  z    w                             ...    w   ... 
                 / \    \                                  /  \ 
               ... ...  ...                              ...  ...
         
        """

        y = x.left 
        x.left = y.right 
        if y.right != self.nil: 
            y.right.p = x

        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        elif x == x.p.left:
            x.p.left = y
        
        y.right = x
        x.p = y

        self.__update_height__(x)
        x.bf = self.__get_balance__(x)
        y.bf = self.__get_balance__(y)




    def __balance_deletion__(self,z):

        """ 
            Balancing routing for adjusting 
            heights of subtrees of a give node
            when deleting the node 
            A detailed description of the procedure 
            applied here can be found on 
        
            https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
            
            time-complexity: O(1)
            space-complexity: O(1)
        
        
        """




        def rebalance(z):



            #get higher height child 
            y = z.right 
            if y.height < z.left.height:
                y = z.left 
            x = y.right 
            if x.height < y.left.height:
                x = y.left

            # case 1 : 
            if z.left == y and y.left == x:
                self.rightRotate(z)
                self.__update_height__(z)
                self.__update_balance__(z)
            #case 2: 
            elif z.left == y and y.right == x:
                self.leftRotate(y)
                self.__update_height__(y)
                self.__update_balance__(y)
                self.rightRotate(z)
            #case 3:
            elif z.right == y and y.right == x:
                self.leftRotate(z)
                
            #case 4: 
            elif z.right == y and y.left == x:
                self.rightRotate(y)
                self.__update_height__(y)
                self.__update_balance__(y)
                self.leftRotate(z)

            self.__update_height__(z)
            self.__update_balance__(z)


        if z != self.nil:
            
            if z.bf < -1 or z.bf > 1:
                rebalance(z)
                
            
            if z.p != self.nil:
                self.__balance_deletion__(z.p)


    def balance(self,x):



        """ 
            Balancing routing for adjusting 
            heights of subtrees of a give node



            case 1: 
                        /                           /                           /
                     ...                          ...                         ...
                     /                            /                           /
                    x                            x                           x
                  /   \         LR(w)          /   \         RR(z)         /   \ 
                 y     z       ======>        y     z      ======>        y     v
                     /                             /                           /  \ 
                    w                             v                           w    z
                     \                           /
                       v                        w

            case 2:

                       /                           /
                     ...                         ...
                     /                           /
                    x                           x
                  /   \          LR(z)        /   \ 
                 y     z      ======>        y     v
                        \                         /  \ 
                         v                       z    w
                          \ 
                           w   



            case 3:

                        /                           /                           /
                     ...                          ...                         ...
                     /                            /                           /
                    x                            x                           x
                  /   \          RR(w)         /   \          LR(z)        /   \ 
                 y     z       ======>        y     z      ======>        y     v
                        \                            \                         /  \ 
                         w                            v                       z    w
                        /                              \ 
                       v                                w


            case 4:


                       /                           /
                     ...                         ...
                     /                           /
                    x                           x
                  /   \          LR(z)        /   \ 
                 y     z      ======>        y     w
                      /                           /  \ 
                     w                           v    z
                    /                   
                   v                    
        
        
            time-complexity: O(1)
            space-complexity: O(1)
        
        
        """

        def rebalance(x):

            if x.bf > 0:
                #case 1:
                if x.right.bf < 0:
                    self.rightRotate(x.right)
                    self.leftRotate(x)
                else:
                #case 2:
                    self.leftRotate(x)
            else:
                #case 3:
                if x.left.bf > 0:
                    self.leftRotate(x.left)
                    self.rightRotate(x)
                #case 4:
                else:
                    self.rightRotate(x)


        if x.bf < -1 or x.bf > 1:
            rebalance(x)
        else:
            #adjust balance factor 
            if x.p != self.nil:
                if x.p.left == x:
                    x.p.bf -= 1
                elif x.p.right == x:
                    x.p.bf += 1

                if x.p.bf:
                    self.balance(x.p)


    





            

    


    





















        




