import random

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