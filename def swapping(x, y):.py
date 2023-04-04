def swapping(x, y):
	# function to swap two numbers
	t = y
	y = x
	x = t

def insert_heap_tree(hT, val):
	# function to insert a value into the heap tree
	tree_size = len(hT)
	if tree_size == 0:
		hT.append(val)
	else:
		hT.append(val)
		i = tree_size
		while i != 0 and hT[i] > hT[(i - 1) // 2]:
			swapping(hT[i], hT[(i - 1) // 2])
			i = (i - 1) // 2

def delete_value(hT, val):
	# function to delete a value from the heap tree
	tree_size = len(hT)
	i = 0
	for i in range(tree_size):
		if val == hT[i]:
			break
	swapping(hT[i], hT[tree_size - 1])
	hT.pop()

def print_array(hT):
	# function to print the heap tree
	for i in range(len(hT)):
		print(hT[i], end=" ")
	print()

heap_tree = []
del_value = 0
insert_heap_tree(heap_tree, 3)
insert_heap_tree(heap_tree, 4)
insert_heap_tree(heap_tree, 9)
insert_heap_tree(heap_tree, 5)
insert_heap_tree(heap_tree, 12)
insert_heap_tree(heap_tree, 7)
insert_heap_tree(heap_tree, 15)
insert_heap_tree(heap_tree, 20)
print("HEAP DATA STRUCTURE - INSERT & DELETE OPERATION")
print("Inserted Values in Heap-Tree")
print_array(heap_tree)
del_value = int(input("Enter one value from above heap-tree values - to delete in Heap-Tree: "))
delete_value(heap_tree, del_value)
print("\nAfter deleting an element: ", end="")
print_array(heap_tree)
