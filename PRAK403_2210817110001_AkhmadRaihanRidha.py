A,B=input().split()
A=int(A) ; B=int(B)
if A>B:
  i=A ; j=B
  while i>= B and j <=A:
    print("%d %d"%(i, j), end='')
    if i==B : break
    else : print(" - ", end='')
    i-=1;j+=1
else:
    i=A ; j=B
    while i<=B and j >= A:
      print("%d %d"%(i,j), end='')
      if i == B : break
      else : print (" - ", end='')
      i +=1 ; j -=1




