def stars(num):

    while(num<0):
        print("invalid row ")

    for i in range(num):
          print(" "*(num-i)+"*"*(i+1))

if __name__ == '__main__':
    num=int(input("row: "))
    print(stars(num))
