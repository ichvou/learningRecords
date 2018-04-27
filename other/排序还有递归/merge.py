#encoding: utf-8
def mergeSort(l1,l2,tmp):
	while len(l1) > 0 and len(l2) >0:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]
	tmp.extend(l1)
	tmp.extend(l2)
	return tmp




a = mergeSort([1,3,5,7], [1,2,4,6,8,10], [])
print(a)

def recMerge(l1,l2,tmp):
	if len(l1) == 0 or len(l2) == 0:
		tmp.extend(l1)
		tmp.extend(l2)
		return tmp
	else:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]
		return recMerge(l1, l2, tmp)

b = recMerge([1,3,5,7], [1,2,4,6,8,10], [])
print(b)


def binSearch(l,t):
	low,high=0,len(l)-1
	while low<high:
		mid = int((low+high)/2)
		if l[mid] > t:
			high = mid
		elif l[mid] < t:
			low = mid + 1
		else:
			return mid

	# if l[low] == t:
	# 	return low
	# else:
	# 	return "fuck"
	return low if l[low] == t else "fuck"

c = binSearch([1,3,5,7,9,10,11,13,15,16,18,22,25,26,29,45,444], 0)
print(c)

def qsort(seq):
	if seq == []:
		return seq
	else:
		p = seq[0]
		smaller = qsort([x for x in seq[1:] if x<p])
		bigger = qsort([x for x in seq[1:] if x>=p])
	return smaller + [p]+ bigger

if __name__=='__main__':
	seq = [5,6,78,9,0,-1,2,3,-65,12]
	print(qsort(seq))

Python

