# Program calculates how many words have switched order

import sys

while True:
    print ("Enter a sentence:")
    mixed = input()
    if len(mixed.split()) < 2:
        print ("A sentence has to be at least 2 words long!")
        continue

    print("Enter the same sentence with a different word order")
    normal = input()
    if len(normal.split()) < 2:
        print ("A sentence has to be at least 2 words long!")
        continue

    def merge_and_count(a, b):
        c = []
        count = 0
        i, j = 0, 0
        while i < len(a) and j < len(b):
            c.append(min(b[j], a[i]))
            if b[j] < a[i]:
                count += len(a) - i
                j+=1
            else:
                i+=1
        c += a[i:] + b[j:]
        return count, c

    def sort_and_count(L):
        if len(L) == 1: 
            return 0, L

        n = len(L) // 2
        a, b = L[:n], L[n:]
        ra, a = sort_and_count(a)
        rb, b = sort_and_count(b)
        r, L = merge_and_count(a, b)
        return ra+rb+r, L

    def get_permutation(L1, L2):
        permutation = list(map(dict((v, i) for i, v in enumerate(L1)).get, L2))
        assert [L1[p] for p in permutation] == L2

        return permutation

    def calculate_mixture(mixed, normal):
        mixed_words = mixed.split()
        normal_words = normal.split()
        perm = get_permutation(normal_words, mixed_words)
        
        print("The number of words with changed order:  ",sort_and_count(perm)[0])

    calculate_mixture(mixed, normal)

    print("Type 'exit' to exit the program or press enter to continue")
    word = input()
    if word == "exit":
        sys.exit()