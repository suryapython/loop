a=int(input("enter value:"))
b=int(input("enter value:"))
def sum(a,b):
    if a==b:
        return (a+b)*2
    else:
        print("sum;",a+b)
print(sum(a,b))