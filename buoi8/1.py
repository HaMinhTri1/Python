
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
newBt = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("tea")
coffee = TreeNode("coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBt.leftChild = leftChild
newBt.rightChild = rightChild

def preOderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOderTraversal(rootNode.leftChild)
    preOderTraversal(rootNode.rightChild)

def inOderTraversal(rootNode):
    if not rootNode:
        return
    inOderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOderTraversal(rootNode.rightChild) 

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
levelOrderTraversal(newBt)    

    