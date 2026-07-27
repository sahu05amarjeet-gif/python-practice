# Default Arguments = 
                    # A default value for certain parameters 
                    # Default is used when the arguments is omitted 
                    # Make your functions more flexible, reduces # of arguments 
                    # 1. Positional 2. DEFAULT 3. Keyword 4. arbitary

def net_price(list_price, discount=0, tax=0.08):
    return list_price * (1 - discount) * (1 + discount)

# print(net_price(480))
# print(net_price(480, 0.2))

# import time
# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE")
# count(0,  5)


import time 

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Times Up!!!")
    
no = count(0, 1000000000000000000000000000000000000000000)
print(no)