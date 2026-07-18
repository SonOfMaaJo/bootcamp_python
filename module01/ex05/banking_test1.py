from the_bank import Bank, Account

bank = Bank()
jane = Account(name='jane', to='', zip=895839, value=10, e='', addr='94boulevard')
willy = Account(name='willy', to='', zip=90, value=0, e='', addr='31Avenue')
bank.add(jane)
bank.add(willy)

print(jane.id, willy.id, jane.ID_COUNT, willy.ID_COUNT,  bank.transfer('jane', 'willy', 5))
del jane.__dict__['id']
bank.fix_account('jane')
print(jane.id, willy.ID_COUNT, jane.ID_COUNT)

