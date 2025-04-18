# Creating Three Files To Put All Data 
BOOKS = "Books.txt"
CUSTOMERS = "Customers.txt"
CIRCULATIONS = "Circulations.txt"
# End of Creating the three files
########################################################

# function read_file
def read_file(file_name):
    # Exception 
    try:
        file = open(file_name, "r")
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    except FileNotFoundError:
        return []
# End Of Function read_file
########################################################

# Function write_file
def write_file(file_name, data):
    file = open(file_name, "w")
    for line in data:
        file.write(line + "\n")
    file.close()
# End Of Function write_file
########################################################

# Function append_to_file
def append_to_file(file_name, line):
    file = open(file_name, "a")
    file.write(line + "\n")
    file.close()
#End Of Function append_to_file
########################################################

# Function is_book_exist
def is_book_exist(title):
    books = read_file(BOOKS)
    for book in books:
        if book.split(",")[0] == title:
            return True
    return False
# End Of Function is_book_exist
########################################################

# Function is_customer_exist
def is_customer_exist(customer_number):
    customers = read_file(CUSTOMERS)
    for customer in customers:
        if customer.split(",")[0] == customer_number:
            return True
    return False
# End Of Function is_customer_exist
########################################################

# Function add_new_book
def add_new_book():
    title = input("Enter book title: ")
    if is_book_exist(title):
        print("This title is already in the system")
        return
    copies = input("Enter the number of copies: ")
    append_to_file(BOOKS, f"{title},{copies}")
    print("The new book has been added")
# End Of Function add_new_book
########################################################

# Function add_new_customer
def add_new_customer():
    customer_number = input("Enter customer number: ")
    if is_customer_exist(customer_number):
        print("This number is already used")
        return
    name = input("Enter the customer's name: ")
    append_to_file(CUSTOMERS, f"{customer_number},{name}")
    print("The new customer has been added")
# End Of Function add_new_customer
########################################################

# Function borrow_book
def borrow_book():
    title = input("Enter book title: ")
    if not is_book_exist(title):
        print("There is no such a title")
        return

    customer_number = input("Enter a customer number: ")
    if not is_customer_exist(customer_number):
        print("No customer with this number")
        return

    # حساب النسخ المتاحة
    books = read_file(BOOKS)
    book_line = next(book for book in books if book.split(",")[0] == title)
    total_copies = int(book_line.split(",")[1])

    circulations = read_file(CIRCULATIONS)
    borrowed = sum(1 for c in circulations if c.split(",")[0] == title and c.split(",")[2] == "b")
    returned = sum(1 for c in circulations if c.split(",")[0] == title and c.split(",")[2] == "r")

    if total_copies > borrowed - returned:
        append_to_file(CIRCULATIONS, f"{title},{customer_number},b")
        print("The book is checked out.")
    else:
        print("No available copies.")
# End Of Function borrow_book
########################################################

# Function return_book
def return_book():
    title = input("Enter book title: ")
    if not is_book_exist(title):
        print("The book is not in the system")
        return

    customer_number = input("Enter customer number: ")
    if not is_customer_exist(customer_number):
        print("The customer is not in the system")
        return

    append_to_file(CIRCULATIONS, f"{title},{customer_number},r")
    print("Book returned successfully")
# End Of Function return_book
########################################################

# Main Function
def main():
    
    while True:

        print("Please select one of the following:")
        print("1- Add a new title")
        print("2- Add a new customer")
        print("3- Borrow")
        print("4- Return")
        print("5- Exit")

        choice = input("Your choice: ") 

        if choice == "1":
            add_new_book()
        elif choice == "2":
            add_new_customer()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
