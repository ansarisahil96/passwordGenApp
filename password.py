import random

alpha=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','M','N','B','V','C','X','Z','A','S','D','F','G','H','J','K','L','P','O','I','U','Y','T','R','E','W','Q']
sc=['!','@','#','$','%','&','*']
num=['1','2','3','4','5','6','7','8','9','0']


def generatePassword(n, a):
    password = []

    for n in range(n):
        if a == 1:
            p = alpha + num
            z = random.choice(p)
            password.append(z)
        elif a == 2:
            p = alpha + sc
            z = random.choice(p)
            password.append(z)
        elif a == 3:
            p = alpha + sc + num
            z = random.choice(p)
            password.append(z)
        else:
            z = random.choice(alpha)
            password.append(z)

    password = ''.join(password)

    return password




