mylists = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
mylists.sort(key=lambda x: x[1])		
print(mylists)


mylists_dict = {}
for mylist in mylists:
	mylists_dict = {mylist[1] : mylist[:1] + mylist[2:]}
	print(mylists_dict)
	array = set(mylist[:1] + mylist[2:])

mylists_dict_r = {}
for mylist in reversed(mylists):
	mylists_dict_r = {mylist[1] : mylist[:1] + mylist[2:]}
	print(mylists_dict_r)
	array = set(mylist[:1] + mylist[2:])
print(array)


arrayTostr = ' '.join([str(elem) for elem in array])
print(arrayTostr)


