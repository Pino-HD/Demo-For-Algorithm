import random

#选择排序
#在选择排序中，首先遍历整个数组，每次循环都要找到最小的那个数
#然后把它放到新的数组中，重复以上操作，新的数组就是排序好的数组
def FindSmallestIndex(L: list) -> int:
	l_smallest = L[0]
	l_smallest_index = 0
	for i in range(1, len(L)):
		if L[i] < l_smallest:
			l_smallest = L[i]
			l_smallest_index = i
	return l_smallest_index

def SelectSort(LL: list) -> list:
	new_l = []
	for i in range(len(LL)):
		ll_smallest = FindSmallestIndex(LL)
		new_l.append(LL.pop(ll_smallest))
	return new_l

if __name__ == '__main__':
	test_l = [random.randint(0, 1000) for x in range(1000)]
	test_l = SelectSort(test_l)
	print(test_l)
