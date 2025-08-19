#Merge sort
def merge_sort(vectori):
    if len(vectori)>1:
        mid = len(vectori)//2
        L=vectori[:mid]
        R=vectori[mid:]
        merge_sort(R)
        merge_sort(L)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
               vectori[k]=L[i]
               i+=1
            else:
                vectori[k]=R[j]
                j+=1
                k+=1

        while i<len(L):
            vectori[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            vectori[k]=R[j]
            j+=1
            k+=1

#Exemplu:
vectori=[56,89,12,34,56,40,10]
merge_sort(vectori)
print("Merge_sort:",vectori)

