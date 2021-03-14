# Enter number of terms needed                   #0,1,1,2,3,5....
n=int(input("Enter the terms? "))
first=0                                         #first element series
second=1                                         #second elementseries
if n<=0:
    print("Please enter positive integet greater than 0")
elif n == 1:
   print("Fibonacci sequence upto",first,":")
   print(first)
else:
    print(first,second,end=" ")
    for x in range(2,n):
        next=first+second                           
        print(next,end=" ")
        first=second
        second=next
