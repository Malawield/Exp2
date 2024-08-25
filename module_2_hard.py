import random


def first_field():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher


n = first_field()


def second_field(n):
    password = {}
    password.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    password.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    password.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    password.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    password.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    password.update({20: 13141911923282183731746416515614713812911})
    passcode = password.get(n)
    return passcode


print('Шифр :', n)

num1 = list(range(1, n))
num2 = list(range(1, n))
pairs = []
result = ''

for i in num1:
    for j in num2:
        if i >= j:
            continue
        else:
            kratno = n % (i + j)
            if kratno == 0:
                pairs.append([i, j])
                result = result + str(i) + str(j)
print('Пары чисел', *pairs)
print('Введите пароль', result)
if int(result) == second_field(n):
    print('Выход открыт!')
