import random

def bubbleSort(L: list) ->list:
	length = len(L)
	for i in range(0, length):
		for j in range(i+1, length):
			if L[i] > L[j]:
				L[i], L[j] = L[j], L[i]
	return L

if __name__ == '__main__':
	L = [random.randint(0, 1000) for i in range(1000)]
	L = bubbleSort(L)
	print(L)
