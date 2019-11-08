def reverse():
    x = 0
    y = 0
    
    n = input("Please enter a number: ")
    
    while (int(n)>0):
        y = (int(n)%10)
        x = (int(x)*10) + int(y)
        n = int(n)/10

    if x == int(n):
        print("This is a palindrome")

    else:
        print("This is not a palindrome")

reverse()
