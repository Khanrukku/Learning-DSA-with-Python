def CommonElement(A,B,C):
  i,j,k=0,0,0
  na,nb,nc=len(A),len(B),len(C)
  while i<na and j<nb and k,nc:
    if A[i]==B[j]==C[k]:
      print(A[i],end="")
      i+=1
      j+=1
      k+=1
    else:
      if A[i]<=B[j] and A[i]<=C[k]:
        i+=1
      elif:
        B[j]<=A[i] and B[j]<=C[k]:
        j+=1
      else:
        k+=1

'''#main
A=[1,2,3,5,8]
B=[1,3,8,9]
C=[3,8,10]

#RESULT
3 8
'''

      
