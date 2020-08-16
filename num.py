import list
year = int(input("Enter the year:"))
if (year%4==0 and year%100!=0):
    print("given year is leap year")

else:
    print("not a leap year")

#febo nachi number

def fib(n):
    a = 0
    b = 1
    if n == 1 :
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)

fib(100)


#define number

def add (n1,n2):
    sum = n1+n2

    return sum
v = add(5,6)
print (v)

# creating a dictunary
module = {
      " Model": "costum",
       " Color": "Black",
       "year":  "2020"
}

list = {
       "car":"Toyta",
       "color":"blue",
       "prize": "140000"

}

defolt = {


      "model ": "good",
      "curb": "well",
      " light": "white",
}
print(module)
print(list)
print(defolt)

x = list["color"]
print(x)

for x in list :
    print(x)


