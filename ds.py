class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.val=key
def printinorder(root):
	if root:
		printinorder(root.left)
		print(root.val,end=" ")
		printinorder(root.right)
def printpostorder(root):
	if root:
		printpostorder(root.left)
		printpostorder(root.right)
		print(root.val,end="  ")
def printpreorder(root):
	if root:
		print(root.val,end=" ")
		printpreorder(root.left)
		printpreorder(root.right)
if __name__ == "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    printpreorder(root)