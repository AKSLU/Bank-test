from main import *

def test_create_account():
    acc = BankAccount("Akslu", 100)
    return acc.owner == "Akslu" and acc.balance == 100

def test_deposit_positive():
    acc = BankAccount("Person", 50)
    acc.deposit(30)
    return acc.balance == 80

def test_deposit_zero_negative():
    acc = BankAccount("Person", 50)
    acc.deposit(0)
    acc.deposit(-20)
    return acc.balance == 50

def test_withdraw_valid():
    acc = BankAccount("Person", 100)
    acc.withdraw(40)
    return acc.balance == 60

def test_withdraw_more_than_balance():
    acc = BankAccount("Person", 30)
    acc.withdraw(50)
    return acc.balance == 30

def test_withdraw_negative_zero():
    acc = BankAccount("Person", 70)
    acc.withdraw(0)
    acc.withdraw(-10)
    return acc.balance == 70

def test_transfer_valid():
    acc1 = BankAccount("Akslu", 100)
    acc2 = BankAccount("Person", 50)
    acc1.transfer_to(acc2, 30)
    return acc1.balance == 70 and acc2.balance == 80

def test_transfer_fails_when_insufficient_funds():
    acc1 = BankAccount("Akslu", 10)
    acc2 = BankAccount("Person", 100)
    acc1.transfer_to(acc2, 50)
    return acc1.balance == 10 and acc2.balance == 100

def test_transfer_fails_with_negative_amount():
    acc1 = BankAccount("Akslu", 100)
    acc2 = BankAccount("Person", 50)
    acc1.transfer_to(acc2, -20)
    return acc1.balance == 100 and acc2.balance == 50

print("Создание аккаунта:", test_create_account())
print("Положительный депозит:", test_deposit_positive())
print("Нулевой депозит:", test_deposit_zero_negative())
print("Допустимое снятие:", test_withdraw_valid())
print("Снятие больше баланса:", test_withdraw_more_than_balance())
print("Нулевое снятие:", test_withdraw_negative_zero())
print("Корректный перевод:", test_transfer_valid())
print("Перевод не проходит нехватке средств:", test_transfer_fails_when_insufficient_funds())
print("Перевод не проходит отрицательной сумма:", test_transfer_fails_with_negative_amount()," Error!")





    
