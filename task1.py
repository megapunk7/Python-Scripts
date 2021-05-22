T = int(input())
li = []
special_characters ="$@#%&?"

def passwordVerify(password):
    n = len(password)
    if n < 10:
        return False
    if password[0].isdigit() or password[n-1].isdigit():
        return False
    if password[0].isupper() or password[n-1].isupper():
        return False    
    return (any(i.islower() for i in password) and any(i.isupper() for i in password) and any(i.isdigit() for i in password) and any(c in special_characters for c in password))
for i in range(T):
        li.append(input())

for i in range(T):
    if passwordVerify(li[i]):
        print("yes")
    else:
        print("No")
            
