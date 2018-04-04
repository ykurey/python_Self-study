import bank as p1
from happy import bank as p2

acct = p1.account("Justin","123",10);
print(acct);
p1.deposition(acct,50);
p2.withdraw(acct,200);
print(p2.desc(acct));
