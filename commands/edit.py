import sqlite3
import os

def edit_command():
    db_path = os.path.abspath("database.db")
    print("Connecting to:", db_path)
    
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    
    print("\nWhat field would you like to edit: ")
    print("1. Faculty")
    print("2. Student")
    print("3. Membership")
    print("4. Club")
    print("5. Member Event")
    print("6. Public Event")
    print("7. Meeting Room")
    
    field = input("\nEnter choice (1-7): ").strip()
    
    if field == "1":
        edit_faculty(conn, cursor)
    elif field == "2":
        edit_student(conn, cursor)
    elif field == "3":
        edit_membership(conn, cursor)
    elif field == "4":
        edit_club(conn, cursor)
    elif field == "5":
        edit_member_event(conn, cursor)
    elif field == "6":
        edit_public_event(conn, cursor)
    elif field == "7":
        edit_meeting_room(conn, cursor)
    else:
        print("Invalid choice.")
        
def edit_faculty(conn, cursor):
    print("\nEdit Faculty")
    facultyID = input("Enter Faculty ID to edit: ").strip()
    
    cursor.execute("SELECT * FROM Faculty WHERE Faculty_ID = ?", (facultyID,))
    record = cursor.fetchone()
    
    if not record:
        print("Faculty ID not found.")
        return
    
    print(f"\nCurrent:")
    print(f"1. Name: {record[1]}")
    print(f"2. Department: {record[2]}")
    
    new_name = input("New Name (press ENTER to keep current): ").strip()
    new_dept = input("New Department (press ENTER to keep current): ").strip()
    
    new_name = new_name if new_name else record[1]
    new_dept = new_dept if new_dept else record[2]
    
    cursor.execute(
        "UPDATE Faculty SET Name = ?, Department = ? WHERE Faculty_ID = ?",
        (new_name, new_dept, facultyID)
    )
    conn.commit()
    print("Faculty updated successfully!")
    
def edit_student(conn, cursor):
    print("\nEdit Student")
    studentID = input("Enter Student ID to edit: ").strip()

    cursor.execute("SELECT * FROM Student WHERE Student_ID = ?", (studentID,))
    record = cursor.fetchone()

    if not record:
        print("Student ID not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Name: {record[1]}")
    print(f"2. Major: {record[2]}")
    print(f"3. Class: {record[3]}")

    new_name = input("New Name (ENTER to keep): ").strip()
    new_major = input("New Major (ENTER to keep): ").strip()
    new_class = input("New Class (ENTER to keep): ").strip()

    new_name = new_name if new_name else record[1]
    new_major = new_major if new_major else record[2]
    new_class = new_class if new_class else record[3]

    cursor.execute(
        "UPDATE Student SET Student_Name = ?, Student_Major = ?, Student_Class = ? WHERE Student_ID = ?",
        (new_name, new_major, new_class, studentID)
    )
    conn.commit()
    print("Student updated successfully!")


def edit_membership(conn, cursor):
    print("\nEdit Membership")
    studentID = input("Enter Student ID: ").strip()
    memberID = input("Enter Member ID: ").strip()

    cursor.execute(
        "SELECT * FROM Membership WHERE Student_ID = ? AND Member_ID = ?",
        (studentID, memberID)
    )
    record = cursor.fetchone()

    if not record:
        print("Membership not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Club ID: {record[2]}")
    print(f"2. Role: {record[3]}")

    new_club_id = input("New Club ID (press ENTER to keep): ").strip()
    new_role = input("New Role (press ENTER to keep): ").strip()

    new_club_id = new_club_id if new_club_id else record[2]
    new_role = new_role if new_role else record[3]

    cursor.execute(
        "UPDATE Membership SET Club_ID = ?, Role = ? WHERE Student_ID = ? AND Member_ID = ? AND Club_ID = ?",
        (new_club_id, new_role, studentID, memberID, record[2])
    )
    conn.commit()
    print("Membership updated successfully!")


def edit_club(conn, cursor):
    print("\nEdit Club")
    clubID = input("Enter Club ID to edit: ").strip()

    cursor.execute("SELECT * FROM Club WHERE Club_ID = ?", (clubID,))
    record = cursor.fetchone()

    if not record:
        print("Club not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Name: {record[1]}")
    print(f"2. Description: {record[2]}")

    new_name = input("New Name (press ENTER to keep): ").strip()
    new_desc = input("New Description (press ENTER to keep): ").strip()

    new_name = new_name if new_name else record[1]
    new_desc = new_desc if new_desc else record[2]

    cursor.execute(
        "UPDATE Club SET Club_Name = ?, Description = ? WHERE Club_ID = ?",
        (new_name, new_desc, clubID)
    )
    conn.commit()
    print("Club updated successfully!")


def edit_member_event(conn, cursor):
    print("\nEdit Member Event")
    eventID = input("Enter Event ID to edit: ").strip()

    cursor.execute("SELECT * FROM Member_Event WHERE Event_ID = ?", (eventID,))
    record = cursor.fetchone()

    if not record:
        print("Member event not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Club ID: {record[1]}")
    print(f"2. Member ID: {record[2]}")
    print(f"3. Room Number: {record[3]}")
    print(f"4. Activity: {record[4]}")

    new_club_id = input("New Club ID (press ENTER to keep): ").strip()
    new_memberID = input("New Member ID (press Enter to keep): ").strip()
    new_room = input("New Room Number (press ENTER to keep): ").strip()
    new_activity = input("New Activity (press ENTER to keep): ").strip()

    new_club_id = new_club_id if new_club_id else record[1]
    new_memberID = new_memberID if new_memberID else record[2]
    new_room = new_room if new_room else record[3]
    new_activity = new_activity if new_activity else record[4]

    cursor.execute(
        "UPDATE Member_Event SET Club_ID = ?, Member_ID = ?, Room_Number = ?, Activity = ? WHERE Event_ID = ? AND Club_ID = ? AND Member_ID = ?",
        (new_club_id, new_memberID, new_room, new_activity, eventID, record[1], record[2])
    )
    conn.commit()
    print("Member event updated successfully!")


def edit_public_event(conn, cursor):
    print("\nEdit Public Event")
    eventID = input("Enter Event ID to edit: ").strip()

    cursor.execute("SELECT * FROM Public_Event WHERE Event_ID = ?", (eventID,))
    record = cursor.fetchone()

    if not record:
        print("Public event not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Club ID: {record[1]}")
    print(f"2. Room: {record[2]}")
    print(f"3. Activity: {record[3]}")

    new_club_id = input("New Club ID (ENTER to keep): ").strip()
    new_room = input("New Room (ENTER to keep): ").strip()
    new_activity = input("New Activity (ENTER to keep): ").strip()

    new_club_id = new_club_id if new_club_id else record[1]
    new_room = new_room if new_room else record[2]
    new_activity = new_activity if new_activity else record[3]

    cursor.execute(
        "UPDATE Public_Event SET Club_ID = ?, Room_Number = ?, Activity = ? WHERE Event_ID = ?",
        (new_club_id, new_room, new_activity, eventID)
    )
    conn.commit()
    print("Public event updated successfully!")


def edit_meeting_room(conn, cursor):
    print("\nEdit Meeting Room")
    roomNum = input("Enter Room Number to edit: ").strip()

    cursor.execute("SELECT * FROM Meeting_Room WHERE Room_Number = ?", (roomNum,))
    record = cursor.fetchone()

    if not record:
        print("Meeting room not found.")
        return

    print(f"\nCurrent:")
    print(f"1. Building: {record[1]}")
    print(f"2. Capacity: {record[2]}")

    new_building = input("New Building (ENTER to keep): ").strip()
    new_capacity = input("New Capacity (ENTER to keep): ").strip()

    new_building = new_building if new_building else record[1]
    new_capacity = new_capacity if new_capacity else record[2]

    cursor.execute(
        "UPDATE Meeting_Room SET Building = ?, Capacity = ? WHERE Room_Number = ?",
        (new_building, new_capacity, roomNum)
    )
    conn.commit()
    print("Meeting room updated successfully!")
