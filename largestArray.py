def largest(arr, n):
    mx = arr[0]
    for i in range (1, n):
        if arr[1] > mx:
            mx = arr[1]

        return mx
        
arr = [10, 34, 45, 90, 9809]
n = len(arr)

Ans = largest(arr, n)

print ("Largest in given array is",Ans)
        
