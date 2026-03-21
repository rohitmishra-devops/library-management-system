import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="librarydb"
)

cursor = con.cursor()

while True:
    print("\n===== Library Management System =====")
    print("1 Add Book")
    print("2 Show Books")
    print("3 Search Book")
    print("4 Delete Book")
    print("5 Issue Book")
    print("6 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Book Name: ")
        book_id = int(input("Enter Book ID: "))
        author = input("Enter Author: ")

        cursor.execute(
            "INSERT INTO library (book_name, book_id, author) VALUES (%s,%s,%s)",
            (name, book_id, author)
        )
        con.commit()
        print("Book Added")

    elif choice == 2:
        cursor.execute("SELECT * FROM library")
        data = cursor.fetchall()

        if len(data) == 0:
            print("No Books Found")
        else:
            for row in data:
                print("Book Name:", row[0])
                print("Book ID:", row[1])
                print("Author:", row[2])
                print("------------------")

    elif choice == 3:
        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT * FROM library WHERE book_id = %s",
            (book_id,)
        )
        data = cursor.fetchone()

        if data:
            print("Book Found")
            print("Book Name:", data[0])
            print("Book ID:", data[1])
            print("Author:", data[2])
        else:
            print("Not Found")

    elif choice == 4:
        book_id = int(input("Enter Book ID to delete: "))

        cursor.execute(
            "DELETE FROM library WHERE book_id = %s",
            (book_id,)
        )
        con.commit()

        print("Book Deleted")

    elif choice == 5:
        book_id = int(input("Enter Book ID to issue: "))
        student = input("Enter Name: ")

        cursor.execute(
            "SELECT * FROM library WHERE book_id = %s",
            (book_id,)
        )
        data = cursor.fetchone()

        if data:
            cursor.execute(
                "INSERT INTO issue_book (book_id, student_name, issue_date) VALUES (%s,%s,NOW())",
                (book_id, student)
            )
            con.commit()

            cursor.execute(
                "DELETE FROM library WHERE book_id = %s",
                (book_id,)
            )
            con.commit()

            print("Book Issued")
        else:
            print("Book Not Found")

    elif choice == 6:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")