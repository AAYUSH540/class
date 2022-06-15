# Lab Exercise
# 4 Enter Account deails such as name and account_no then delete name using account number
print("Lab Q 4 : ")

bank_details = dict()
i = 0
n = int(input("Number of Accounts = "))

while i < n:
    name = str(input("Name : "))
    account_no = int(input("Account Number : "))
    bank_details[name] = account_no
    i += 1

print()

print("{:^10} \t {:^10}".format("Name of account holder", "Account no."))
for i in bank_details:
    print("\t{:^16} \t {:^10}".format(i, bank_details[i]))

print()

del_name=str(input("Name for deletion of account number = "))

del bank_details[del_name]

print()

print("Details of bank after deletion of account : ")
print("{:^10} \t {:^10}".format("Name of account holder", "Account no."))
for i in bank_details:
    print("\t{:^16} \t {:^10}".format(i, bank_details[i]))

print()

# 5 Enter Account deails such as name and account_no then display all account holder info in ascending order based on acount no
print("Lab Q 5 : ")

bank_details = dict()
i = 0
n = int(input("Number of Accounts = "))

while i < n:
    name = str(input("Name : "))
    account_no = int(input("Account Number : "))
    bank_details[name] = account_no
    i += 1

print()

print("{:^10} \t {:^10}".format("Name of account holder", "Account no."))
for i in sorted(bank_details,key=bank_details.get):
    print("\t{:^16} \t {:^10}".format(i, bank_details[i]))