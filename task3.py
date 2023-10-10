# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


balance = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600
operation = []

def add_money(withdow: float):
    global balance
    global count
    global FREENDERING
    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        count += 1
        balance += withdrow
    print(balance)


def take_money(withdow: float):
    global balance
    global count
    global FREENDERING
    global COMMISSIONOUTDROW
    global MAXLIMIT
    global MINLIMIT

    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        comission = withdrow * COMMISSIONOUTDROW
        if comission < MINLIMIT:
            comission = MINLIMIT
        elif comission > MAXLIMIT:
            comission = MAXLIMIT
        if (comission + withdrow) < balance:
            balance -= (withdrow + comission)
            count += 1
        print(balance)

operation = []

while True:
    
    action = input('Введите операцию 1 - пополнение, 2 - снятие, 3 - выход: ')
    if balance >= RICHLIMIT:
        balance *= RICHTAX
    if count % THREEOPERATIONS == 0 and count != 0:
        balance *= BONUSTHREE
        count = 0
    if action == '1':
        add_money(balance)
        operation.append(['Сумма после пополнения', balance])
    elif action == '2':
        take_money(balance)
        operation.append(['Сумма после снятия', balance])
    else:
        break
print(*operation, sep='\n')
print("Ваш баланс ", balance)