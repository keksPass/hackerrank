if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
   
    max_elem= max(arr)
    for x in range(n):
        if max_elem== max(arr):
         arr.remove(max(arr))
    print(max(arr))
