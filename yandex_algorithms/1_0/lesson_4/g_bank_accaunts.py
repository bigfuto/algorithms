def deposit(names, name, money):
    if name not in names:
        names[name] = 0
    names[name] += int(money)


def withdraw(names, name, money):
    if name not in names:
        names[name] = 0
    names[name] -= int(money)


def balance(names, name):
    if name in names:
        print(names[name])
    else:
        print('ERROR')


def transfer(names, sender, receiver, money):
    money = int(money)
    if sender not in names:
        names[sender] = 0
    if receiver not in names:
        names[receiver] = 0
    names[sender] -= money
    names[receiver] += money


def income(names, percent):
    for key, value in names.items():
        if value > 0:
            names[key] += int(value / 100 * int(percent))


clients_names = {}
commands = {'DEPOSIT': deposit, 'INCOME': income, 'BALANCE': balance, 'TRANSFER': transfer, 'WITHDRAW': withdraw}

for line in open('input.txt'):
    command = line.split()
    commands[command[0]](clients_names, *command[1:4])
