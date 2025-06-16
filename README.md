# Bank-test

Данный проект реализует класс BankAccount, который моделирует банковский счёт с возможностью:

Создания счёта с владельцем и начальным балансом.
Внесения средств (deposit).
Снятия средств (withdraw).
Перевода средств на другой счёт (transfer_to).

Тестирование
Тесты реализованы в файле test2.py. Они проверяют корректность работы всех методов и граничных условий.

test_create_account: Создание аккаунта с правильными параметрами
test_deposit_positive: Пополнение баланса положительной суммой
test_deposit_zero_negative:	Попытка внести 0 или отрицательное число
test_withdraw_valid:	Снятие суммы, не превышающей баланс
test_withdraw_more_than_balance:	Попытка снять больше, чем есть на счёте
test_withdraw_negative_zero:	Снятие 0 или отрицательной суммы
test_transfer_valid:	Корректный перевод между двумя счётами
test_transfer_fails_when_insufficient_funds:	Попытка перевода при недостатке средств
test_transfer_fails_with_negative_amount:	Попытка перевода отрицательной суммы

