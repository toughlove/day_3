def find_missing(lst1,lst2):
	for element in lst2:		
		if element  not in lst1:
			return element       
print (find_missing([1,2,3], [1,2,3,4]))