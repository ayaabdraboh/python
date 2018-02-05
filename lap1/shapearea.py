def calculate(a,c,b=0):



    if c=='t':

        area=0.5*a*b
    elif c=='c':
        
        area=3.14*a*a
    elif c=='s':
        
        area=a*a
    elif c=='r':
        
        area=a*b
    return area


if __name__ == '__main__':
    print("if you want to calculate area of shape input char from below")
    c = input("enter char between t,s,c,r : ")
    a=int(input("enter num1"))
    b=int(input("enter num2"))
    print(calculate(a,c,b))
