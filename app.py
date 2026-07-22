# first define the table structure

# users = {
#     account1 :{
#         'name':Username,
#         'email':Email,
#         'password':Password,
#         'balance':Balance
#     },
#     account2 :{
#         'name':Username,
#         'email':Email,
#         'password':Password,
#         'balance':Balance
#     }
# }

users = {
    1234 :{
        'name': 'Jayaram',
        'email': 'pollajayaram@gmail.com',
        'password': '1234',
        'balance': 10000
    },
    1235 :{
        'name': 'Polla',
        'email': 'collajayaram@gmail.com',
        'password': '1235',
        'balance': 5000
    }
}

## Require services
# register function defination
def register(username:str, email:str, password:str, initial_deposite:int=0)->str:
    return "Registration page under development process...."


def login(account:int, password:str)->bool:
    if account in users:
        if password == users[account].get('password'):
            return True
        else:
            return False
    return False
    

#Balance function defination
def balance(account:int)->str:
    curr_amount = users[account].get('balance', -1)
    return curr_amount
    

#withdraw function defination
def withdraw(account:int, withdraw_amount:int)->str:
    curr_amount = users[account].get('balance', -1)
    if curr_amount >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"Withdraw successful and current balance {users[account]['balance']}"
    else:
        return "Insufficient Balance "
    
    

#Deposite function defination
def deposite(account:int, deposite_amount:int)->str:
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} Deposite successful and current balance is {users[account]['balance']}"

    

#Transfer function defination
def transfer(from_account:int,to_account:int, transfer_amount:int)->str:
    if to_account in users:
        curr_amount = users[from_account].get('balance', -1)
        if curr_amount >= transfer_amount:
            users[from_account]['balance'] -= transfer_amount
            users[to_account]['balance'] += transfer_amount
            return f"{transfer_amount} Amount transfered successful and current amount is {users[from_account]['balance']}"
        else:
            return "Insufficient Balance "
    else:
        return "check your reciever account number"

#ministatement function defination
def ministatement(account:int)->str:
    return "Ministatement page under development process..."


#logout function defination
def logout()->str:
    return "Bye bye see you later buddy"
    

# main
if __name__ == "__main__":
    print("Welcome to small scale ATM")
    print("1.Register \n 2.Login")
    choice = int(input("Select your choice:"))
    if choice == 1:
        print("your selected 1.Register")
        name = input("Enter username:")
        email = input("Enter Email:")
        password = input("Enter Password:")
        deposite = int(input("Enter initial deposite amount:"))
        # call register function
        account = register(username=name,
                           email=email,
                           password=password,
                           initial_deposite=deposite
                           )
        print("Your account number is:", account)
    elif choice == 2:
        print("Your selected 2.login operation")
        account_no = int(input("Enter your account no:"))
        password = input("Enter your password:")
        #login function calling
        login_val = login(account=account_no, password=password)
        while login_val:
            print("1.Balance \n 2.Withdraw \n 3.Deposite \n 4.Transfer \n 5. Ministatement \n 6.Logout ")
            choice = int(input("Enter your choice:"))
            print(choice)
            if choice == 1:
                res = balance(account=account_no)
                print(res)

            elif choice == 2:
                amount = int(input("Enter withdraw amount:"))
                res = withdraw(account=account_no,withdraw_amount=amount)
                print(res)

            elif choice == 3:
                amount = int(input("Enter Deposite amount:"))
                res = deposite(account=account_no,deposite_amount=amount)
                print(res)

            elif choice == 4:
                reciever_acc = int(input("Enter the reciever account no:"))
                amount = int(input("Enter Transfer amount:"))
                res = transfer(from_account=account_no,to_account=account_no,transfer_amount=amount)
                print(res)

            elif choice == 5:
                res = ministatement(account=account_no)
                print(res)

            elif choice == 6:
                print(logout())
                exit()

            else:
                print("Invalid choice !!! /n Select you choice in between 1-6")