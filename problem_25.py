import time

start = time.time()

a, b = 1, 2
term = 3
while a < b: #stops if meet break at line 8
    a, b = b, a+b
    term += 1 #adding term by 1 every cycle
    if len(str(b)) >= 1000:
        print("term:", term) #print current term
        break #breaks the loop
    else:
        continue

elapsed = time.time() - start

print("solved in %s seconds") % (elapsed)