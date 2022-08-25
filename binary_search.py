#Program to search for a target number using the binary search method in a function

def Binary_Search(list, t):
    left, right=0, n-1
    while left<=right:
        m=(left+right)//2
        if list[m]<t:
            left=m+1
        elif list[m]>t:
            right=m-1
        elif list[m]==t:
            return m
    return 0

if __name__=="__main__":
    list=[]
    n=int(input("How many items does your list have? "))
    for i in range(0,n):
        list.append(int(input("Enter a number: ")))
    
    print(list) #original list
    list.sort()   
    print(list) #sorted list
    t=int(input("Enter the target number: "))
    index=Binary_Search(list, t)
    if index!=0:
        print(f"The number {t} was found in at position {index} of the list")
    else:
        print("The number was not founds")
