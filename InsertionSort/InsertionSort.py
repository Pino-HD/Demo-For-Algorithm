import random

#插入排序
#对于未排序的数据，在已排序的数组从后向前扫描，插入到合适的位置
#在排序的时候，需要将已排序的元素一个一个的向后挪位置，为新元素腾地方
#在python的实现中，可以通过交换的方式，跟冒泡的实现很像
#但是冒泡是一个数据跟其他所有的数据都进行比较
#而插入排序只是相邻的进行比较
def InsertionSort(L: list) -> list:
	length = len(L)
	for i in range(1, length):
		for j in range(i, 0, -1):
			if L[j] < L[j-1]:
				L[j], L[j-1] = L[j-1], L[j]
			else:
				break
	return L



if __name__ == '__main__':
	test_l = [random.randint(0, 1000) for x in range(1000)]
	test_l = InsertionSort(test_l)
	print(test_l)