import random

#快速排序
#选择第一个数据作为标志，遍历列表，将小于标志的数据放到前面，将大于标志的数据放在后面
#然后分而治之，对新的列表重复上面的操作，递归执行
def QuickSort(L: list) -> list:
	if len(L) < 2:
		return L
	else:
		pivot = L[0]
		left = [x for x in L[1:] if x <= pivot]
		right = [x for x in L[1:] if x > pivot]
		return QuickSort(left) + [pivot] + QuickSort(right)

if __name__ == '__main__':
	L = [random.randint(0, 1000) for x in range(1000)]
	L = QuickSort(L)
	print(L)