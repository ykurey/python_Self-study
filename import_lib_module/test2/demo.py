import bank

acct = bank.account("Justin","123",10);
print(acct);
bank.deposition(acct,50);
bank.withdraw(acct,200);
print(bank.desc(acct));
