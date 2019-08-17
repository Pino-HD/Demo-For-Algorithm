import random

def shellSort(L: list):
	length = len(L)
	gap = length // 2
	while gap > 0:
		for i in range(0, gap):
			k = i + gap
			while k < length:
				for j in range(i+gap, length, gap):
					if L[j] < L[j-gap]:
						L[j], L[j-gap] = L[j-gap], L[j]
				k += gap
		gap //= 2
	return L

if __name__ == '__main__':
	test_l = [random.randint(0, 1000) for x in range(1000)]
	print(shellSort(test_l))
