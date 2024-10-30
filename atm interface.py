users = {
    "123456": {"pin": "1234", "balance": 2000, "transaction_history": []},
    "789012": {"pin": "5678", "balance": 100, "transaction_history": []},
    "543567": {"pin": "9012", "balance": 500, "transaction_history": []},
}
def deposit(user_id, amount):
    if user_id in users:
        users[user_id]["balance"] += amount
        users[user_id]["transaction_history"].append(f"Deposited ${amount}")
        print(f"Deposited ${amount} successfully.")
    else:
        print("User not found.")
def withdraw(user_id, amount):
    if user_id in users:
        if users[user_id]["balance"] >= amount:
            users[user_id]["balance"] -= amount
            users[user_id]["transaction_history"].append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount} successfully.")
        else:
            print("Insufficient funds.")
    else:
        print("User not found.")
def transfer(sender_id, recipient_id, amount):
    if sender_id in users and recipient_id in users:
        if users[sender_id]["balance"] >= amount:
            users[sender_id]["balance"] -= amount
            users[sender_id]["transaction_history"].append(f"Transferred ${amount} to {recipient_id}")
            users[recipient_id]["balance"] += amount
            users[recipient_id]["transaction_history"].append(f"Received ${amount} from {sender_id}")
            print(f"Transferred ${amount} to {recipient_id} successfully.")
        else:
            print("Insufficient funds.")
    else:
        print("User not found.")
def view_transaction_history(user_id):
    if user_id in users:
        print("Transaction History:")
        for transaction in users[user_id]["transaction_history"]:
            print(transaction)
    else:
        print("User not found.")
def atm():
    print("Welcome to the ATM")
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")

    if user_id in users and users[user_id]["pin"] == pin:
        while True:
            print("\nChoose an option:")
            print("1. View Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_transaction_history(user_id)

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_id, amount)

            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                deposit(user_id, amount)

            elif choice == "4":
                recipient_id = input("Enter recipient's user ID: ")
                amount = float(input("Enter amount to transfer: "))
                transfer(user_id, recipient_id, amount)

            elif choice == "5":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid user ID or PIN")
if __name__== "__main__":
    atm()