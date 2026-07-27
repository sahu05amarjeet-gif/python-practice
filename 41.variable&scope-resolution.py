def func1():
    x = 1  # x = 1 is LOCAL for func1
    print(x)
def func2():
    x = 2 # x = 2 is LOCAL for func2
    print(x)

x = 3 # here x = 3 is a Global value of x for both the functions. If we remove x from both function
# x = 3 will be printed. But if we use the value under each func that value will be printed.
func1()
func2()
#Variable scope = where a variable is visible and accessible 
#Scope resolution = (LEGB) Local -> Enclosed -> Global -> Bult-in

#Enclosed = func1 is under the func2
# when we import math the value of e will be BUILT-IN but when we declare e = 3 python will
# use the Global value of e i.e e = 3 in this function. It's like BODMAS rule. 
