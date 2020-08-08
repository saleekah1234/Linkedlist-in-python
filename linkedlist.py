class Node():
	def __init__(self,data=None):
		self.data=data
		self.next=None
	def printnode(self):
		print("The node created now is {}".format(self.data))
	
class Slinkedlist():
	def __init__(self):
		self.head=None
	
	def display(self):
		lists=[]
		curr_node=self.head
		while(curr_node!=None):
			lists.append(curr_node.data)
			curr_node=curr_node.next
		print(lists)
	def addnode(self):
		newdata=int(input("enter the number"))
		newnode=Node(newdata)
		if(self.head==None):
			self.head=newnode
			return
		else:
			last=self.head
			while(last.next):
				last=last.next
			last.next=newnode
	def deletenode(self):
		index=int(input("enter the index to delete"))
		count=0
		if(count==index==0):
			self.head=self.head.next
			return
		count=1
		curr_node=self.head
		while(True):
			prev_node=curr_node
			curr_node=curr_node.next	
			if(count==index):
				prev_node.next=curr_node.next
				return	
			count=count+1
	def insertatindex(self):
		index=int(input("enter the index to insert"))
		data=int(input("enter data"))
		count=1
		newnode=Node(data)
		newnode.next=None
		curr_node=self.head
		while(True):
			prev_node=curr_node
			curr_node=curr_node.next
			if(count==index):
				prev_node.next=newnode
				newnode.next=curr_node
				return
			count=count+1
	def deleteall(self):
		key=int(input("enter the number"))
		curr_node=self.head
		while(curr_node==None and curr_node.data==key):
			self.head=curr_node.next
			curr_node=self.head
		#delte all occurences otherthan head
			while(curr_node!=None):
			#seacrh the key to be deleted,keep track of previuos node to map prev.next to curr.next so that curr_node is deleted
				while(curr_node!=None and curr_node.data!=key):
					prev_node=curr_node
					curr_node=curr_node.next
		#if key is not present in linked list
				if(curr_node==None):
					return
			#otherwise the loop exited beacuause key==curr_data so delte that node,unlink that node from linked list
				prev_node.next=curr_node.next
			#(no need of free(curr_node) in python as in c
			
			#update curr_node for next iteration of outer loop
				curr_node=prev_node.next
				
							
			

		
		
node1=Slinkedlist()

while(True):
	print("1.addnode 2.displaynode 3.delete 4.addat specific index 5.deleteall 6.exit")
	choice=int(input("enter the choice number"))
	if(choice==1):
		node1.addnode()
	elif(choice==2):
		node1.display()
	elif(choice==3):
		node1.deletenode()
	elif(choice==4):
		node1.insertatindex()
	elif(choice==5):
		node1.deleteall()
	elif(choice==6):
		break



