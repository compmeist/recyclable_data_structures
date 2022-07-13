#  
# this is a recyclable linked list
# (should be memory allocator friendly) 
#


class node:
	def __init__(self, data=None):
    	  self.data = data
    	  self.next = None
    	  self.nextMemNode = None

class rcyc_linked_list: # first element has no data
	def __init__(self,ll_head_to_recycle=None):
       	if (ll_head_to_recycle == None): 
        	self.head = node()
        else:
       		self.head = ll_head_to_recycle
       		self.head.next = None  # (do not overwrite nextMemNode here)

	def append(self, data):
        cnode = self.head
        while (cnode.next != None):
        	cnode = cnode.next
        if (cnode.nextMemNode == None):
        	cnode.next = node(data)
        	cnode.nextMemNode = cnode.next  # save this for recycle
        else:
        	cnode.next = cnode.nextMemNode  # use the previously allocated memory
        	cnode.next.data = data  # copy data into node (similar to constructor node())
        	cnode.next.next = None 

	def display(self):
		elems = []
		cnode = self.head
		while cnode.next != None:
			cnode = cnode.next
			elems.append(cnode.data)
		print elems

my_list = rcyc_linked_list(None)

my_list.display()
my_list.append('one')
my_list.append('two')
my_list.display()

# now, instead de-allocating the memory, we can recycle it ( assuming we no longer need the other list)

my_list2 = rcyc_linked_list(my_list.head)

my_list2.display()
my_list2.append('oneone')
my_list2.append('twotwo')
my_list2.display()

