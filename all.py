def translate(phrase):
    translation = ""
    for latter in phrase:
        if latter in "AEIOUaeiou":
            translation = translation + "g"

        else:
            translation = translation + latter


    return translation

print(translate(input("Enter a phrase:")))

# prime number
num = int(input("enter a number :"))
for i in range(2,num):
    if num % i == 0 :
        print("NOt prime")
        break
    else:
         print("prime")

def ls (a):
    b = len(a)-1
    for x in range(b):
        for t in range(b-x):
            if a [y] > a[y+1]:
                a [y],a[y+1] = a[y+1],a[y]

    return True

a = [41,2145,3698,412,5741,3321,2331,100,1000,12223,1144]

x = ls(a)
print (a)