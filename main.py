class solution:
    def element_removal(self,arr):
        arr.sort(reverse=True)
        res=0
        for i in range(len(arr)):
            res+=sum(arr)
            arr[i]=0
        return res


a1=solution()
a=list(map(int,input().split()))
print(a1.element_removal(a))