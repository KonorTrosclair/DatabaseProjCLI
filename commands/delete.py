import sqlite3
import os

def delete_command():
    db_path = os.path.abspath("database.db")
    print("Connecting to:", db_path)
    
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    
    print("\nWhat field would you like to delete from:")
    print("1. Faculty")
    print("2. Student")
    print("3. Membership")
    print("4. Club")
    print("5. Member Event")
    print("6. Public Event")
    print("7. Meeting Room")
    
    field = input("\nEnter choice (1-7): ").strip()
    
    if field == "1":
        delete_faculty(conn, cursor)
    elif field == "2":
        delete_student(conn, cursor)
    elif field == "3":
        delete_membership(conn, cursor)
    elif field == "4":
        delete_club(conn, cursor)
    elif field == "5":
        delete_member_event(conn, cursor)
    elif field == "6":
        delete_public_event(conn, cursor)
    elif field == "7":
        delete_meeting_room(conn, cursor)
    else:
        print("Invalid choice.")
        

def delete_faculty(conn, cursor):
    print("\nDelete Faculty")
    facultyID = input("Enter Faculty ID to delete: ").strip()
    
    cursor.execute("SELECT * FROM Faculty WHERE Faculty_ID = ?", (facultyID,))
    record = cursor.fetchone()
    
    if not record:
        print("Faculty ID not found.")
        return
    
    print(f"Delete Faculty: ID={record[0]}, Name={record[1]}, Dept={record[2]}")
    confirm = input("Are you sure? (yes/no): ").lower()
    
    if confirm == "yes":
        cursor.execute("DELETE FROM FACULTY WHERE Faculty_ID = ?", (facultyID,))
        conn.commit()
        print("Faculty deleted successfully.")
    else:
        print("Cancelled.")
        
def delete_student(conn, cursor):
    print("\nDelete Student")
    studentID = input("Enter Student ID to delete: ").strip()
    
    cursor.execute("SELECT * FROM Student WHERE Student_ID = ?", (studentID,))
    record = cursor.fetchone()
    
    if not record:
        print("Student ID not found.")
        return
    
    print(f"Delete Student: ID={record[0]}, Name={record[1]}, Major={record[2]}, Class={record[3]}")
    confirm = input("Are you sure? (yes/no): ").lower()
    
    if confirm == "yes":
        cursor.execute("DELETE FROM Student WHERE Student_ID = ?", (studentID,))
        conn.commit()
        print("Student deleted successfully.")
    else:
        print("Cancelled.")
        
def delete_membership(conn, cursor):
    print("\nDelete Membership")
    memberID = input("Enter Member ID: ").strip()
    
    cursor.execute(
        "SELECT * FROM Membership WHERE Member_ID = ?", (memberID,))
    record = cursor.fetchone()
    
    if not record:
        print("Membership not found.")
        return
    
    print(f"Delete Membership: Student={record[0]}, Member={record[1]}, Club={record[2]}, Role={record[3]}")
    confirm = input("Are you sure? (yes/no): ").lower()
    
    if confirm == "yes":
        cursor.execute(
            "DELETE FROM MEMBERSHIP WHERE Member_ID = ?", (memberID,))
        conn.commit()
        print("Membership deleted successfully.")
    else:
        print("Cancelled.")
        
def delete_club(conn, cursor):
    print("\nDelete Club")
    clubID = input("Enter Club ID to delete: ").strip()

    cursor.execute("SELECT * FROM Club WHERE Club_ID = ?", (clubID,))
    record = cursor.fetchone()

    if not record:
        print("Club not found.")
        return

    print(f"Delete Club: Club_ID={record[0]}, Club_Name={record[1]}, Description={record[2]}")
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        cursor.execute("DELETE FROM Club WHERE Club_ID = ?", (clubID,))
        conn.commit()
        print("Club deleted successfully.")
    else:
        print("Cancelled.")


def delete_member_event(conn, cursor):
    print("\nDelete Member Event")
    eventID = input("Enter Event ID: ").strip()

    cursor.execute("SELECT * FROM Member_Event WHERE Event_ID = ?", (eventID,))
    record = cursor.fetchone()

    if not record:
        print("Event not found.")
        return

    print(f"Delete Member Event: ID={record[0]}, Club={record[1]}, Member={record[2]}, Room={record[3]}, Activity={record[4]}")
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        cursor.execute("DELETE FROM Member_Event WHERE Event_ID = ?", (eventID,))
        conn.commit()
        print("Member event deleted successfully.")
    else:
        print("Cancelled.")


def delete_public_event(conn, cursor):
    print("\nDelete Public Event")
    eventID = input("Enter Event ID: ").strip()

    cursor.execute("SELECT * FROM Public_Event WHERE Event_ID = ?", (eventID,))
    record = cursor.fetchone()

    if not record:
        print("Public event not found.")
        return

    print(f"Delete Public Event: ID={record[0]}, Club={record[1]}, Room={record[2]}, Activity={record[3]}")
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        cursor.execute("DELETE FROM Public_Event WHERE Event_ID = ?", (eventID,))
        conn.commit()
        print("Public event deleted successfully.")
    else:
        print("Cancelled.")


def delete_meeting_room(conn, cursor):
    print("\nDelete Meeting Room")
    roomNum = input("Enter Room Number: ").strip()
    building = input("Enter Building: ")

    cursor.execute("SELECT * FROM Meeting_Room WHERE Room_Number = ? AND Building = ?", (roomNum, building))
    record = cursor.fetchone()

    if not record:
        print("Meeting room not found.")
        return

    print(f"Delete Meeting Room: Room={record[0]}, Building={record[1]}, Capacity={record[2]}")
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        cursor.execute("DELETE FROM Meeting_Room WHERE Room_Number = ? AND Building = ?", (roomNum, building))
        conn.commit()
        print("Meeting room deleted successfully.")
    else:
        print("Cancelled.")
