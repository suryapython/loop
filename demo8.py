a=bool(input("enter bool:"))
b=bool(input("enter bool:"))
def monkey(a,b):
    if a == True and b == False:
        return True
    else:
        if a==False and b==False:
            return True

    if a== True or b== True:
        return False
print(monkey(a,b))

