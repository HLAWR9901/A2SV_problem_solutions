if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #using array set
    arr_set = set(arr)
    arr_set.remove(max(arr_set))
    print(max(arr_set))
