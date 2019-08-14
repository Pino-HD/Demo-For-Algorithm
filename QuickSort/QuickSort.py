import random

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