x = "Hello world!"
print(x[1])
print(len(x))
y = 5
print(x + " " + str(y))





print(2>0)
print(0>2)
a = 17
b = 13
c = 14
d = 21
print(a>b)

if a>b or c>d:
    print("yay")
elif a == b:
    print("Nay")
else: 
    print("Nothing is true")





fruits = ["apple","banana","Peach"]
for item in fruits:
    if item == "banana":
        continue
    print(item)



i = 1
while i<4:
    print(i)
    i += 1



def my_function():
    print("Whatever")

my_function()




def add(a,b):
    return a + b

result = add(1,1)
print(result)

def function1(a,b):
    return a + " " + b

print(function1("hello", "concordia"))