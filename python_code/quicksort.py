import random
def quick_sort(seq):
    if(len(seq) < 2):
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quick_sort(left) + [base] + quick_sort(right)

if __name__ == '__main__':
    seq = [9,8,7,6,5,4]
    random.shuffle(seq)
    print(seq)
    print(quick_sort(seq))