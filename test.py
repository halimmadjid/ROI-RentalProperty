
expenses = {}

while True:
    try: 
        a = 'HOA Dues'
        a1 = int(input("What is the total monthly HOA dues? If none, type '0'. "))
        break
    except: 
        print('Not a valid response. Provide an integer value')
        continue
while True:
    try: 
        b = 'tax'
        b2 = int(input("What is the total monthly HOA dues? "))
        break
    except: 
        print('Not a valid response. Provide an integer value. \nIf none, type 0.')
        continue
while True:
    try: 
        c = 'utiliy'
        c2 = int(input("What is the total monthly HOA dues? If none, type '0' "))
        break
    except: 
        print('Not a valid response. Provide an integer value)')
        continue

expenses[a] = a1
expenses[b] = b2
expenses[c] = c2

for key, value in expenses.items(): 
    print(key, ' : ', value)