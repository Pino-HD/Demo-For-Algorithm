import random

#归并排序
#先分开在合并，分开的时候要分成单个元素，然后合并的时候按照顺序合并
def mergeSort(L:list) -> list:
	if len(L) == 1:
		return L
	mid = len(L) // 2
	left = L[:mid]
	right = L[mid:]
	lleft = mergeSort(left)
	lright = mergeSort(right)
	return merge(lleft, lright)

def merge(lleft:list, lright:list) -> list:
	result = []
	while len(lleft) > 0 and len(lright) > 0:
		if lleft[0] <= lright[0]:
			result.append(lleft.pop(0))
		else:
			result.append(lright.pop(0))
	result += lleft
	result += lright
	return result

if __name__ == '__main__':
	test_l = [random.randint(1, 1000) for x in range(1000)]
	test_l = mergeSort(test_l)
	print(test_l)
