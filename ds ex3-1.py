 stack =[]
while True:
    print("\n1.push 2.pop 3.peek 4.display 5.exit")
    ch=int(input("enter choice :"))
    if ch==1:
        item=input("Enter item : ")
        stack.append(item)
    elif ch==2:
        if stack:
            print("popped :",stack.pop())
        else:
            print("stack is empty")
    elif ch==3:
        if stack:
            print("top elements :",stack[-1])
        else:
            print("stack is empty")
    elif ch==4:
        print("stack:",stack)
    elif ch==5:
        break
    else:
        print("invalid choice")
