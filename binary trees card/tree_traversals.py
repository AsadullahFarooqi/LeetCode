def in_order(root):
    if root != None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

def pre_order(root):
    if root != None:
        print(root.val)
        pre_order(root.left)
         pre_order(root.right)

def post_order(root):
    if root != None:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

def in_order_iterative(root):
    if root == None:
        return root
    
    stack = []
    stack.append(root)
    while len(stack):
        

def pre_order_iterative(root):
    if root != None:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def post_order_iterative(root):
    if root != None:
        post_order(root.left)
        post_order(root.right)
        print(root.val)
