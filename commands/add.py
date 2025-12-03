
import sqlite3
import os



def add_command():
    db_path = os.path.abspath("database.db")
    print("Connecting to:", db_path)

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    print("\nWhat field would you like to add to:")
    print("1. Faculty")
    print("2. Student")
    print("3. Membership")
    print("4. Club")
    print("5. Member Event")
    print("6. Public Event")
    print("7. Meeting Room")

    field = input("\nEnter choice (1-7): ").strip()
    # insertedField = ""

    if field == "1":
        print("You selected: Faculty")
        # insertedField = "Faculty"
        add_faculty(conn, cursor)
    elif field == "2":
        print("You selected: Student")
        # insertedField = "Student"
        add_student(conn, cursor)
    elif field == "3":
        print("You selected: Membership")
        # insertedField = "Membership"
        add_membership(conn, cursor)
    elif field == "4":
        print("You selected: Club")
        # insertedField = "Club"
        add_club(conn, cursor)
    elif field == "5":
        print("You selected: Member Event")
        # insertedField = "Member_Event"
        add_member_event(conn, cursor)
    elif field == "6":
        print("You selected: Public Event")
        # insertedField = "Public_Event"
        add_public_event(conn, cursor)
    elif field == "7":
        print("You selected: Meeting Room")
        # insertedField = "Meeting_Room"
        add_meeting_room(conn, cursor)
    else:
        print("Invalid choice. Please enter 1-7.")


def add_faculty(conn, cursor):
    facultyID = input("\nEnter faculty ID: ").strip()
    facultyName = input("\nEnter faculty name: ").strip()
    Department = input("\nEnter department: ").strip()

    cursor.execute("SELECT 1 FROM Faculty WHERE Faculty_ID = ?", (facultyID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A faculty member with that ID already exists. Please choose a different ID.")
        return  

    cursor.execute(
        "INSERT INTO Faculty (Faculty_ID, Name, Department) VALUES (?, ?, ?)",
        (facultyID, facultyName, Department)
    )
    conn.commit()
    print("\nFaculty added successfully!")

def add_student(conn, cursor):
    studentID = input("\nEnter student ID: ").strip()
    studentName = input("\nEnter student name: ").strip()
    studentMajor = input("\nEnter student major: ").strip()
    studentClass = input("\nEnter student class: ").strip()

    cursor.execute("SELECT 1 FROM Student WHERE Student_ID = ?", (studentID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A student with that ID already exists. Please choose a different ID.")
        return 

    cursor.execute(
        "INSERT INTO Student (Student_ID, Name, Major, Class) VALUES (?, ?, ?, ?)",
        (studentID, studentName, studentMajor, studentClass)
    )
    conn.commit()
    print("\nStudent added successfully!")

def add_membership(conn, cursor):
    studentID = input("\nEnter student ID: ").strip()
    memberID = input("\nEnter member ID: ").strip()
    clubID = input("\nEnter club ID: ").strip()
    role = input("\nEnter student role: ").strip()

    cursor.execute("SELECT 1 FROM Membership WHERE Member_ID = ?", (memberID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A club member with that ID already exists. Please choose a different ID.")
        return

    cursor.execute(
        "INSERT INTO Membership (Student_ID, Member_ID, Club_ID, Role) VALUES (?, ?, ?, ?)",
        (studentID, memberID, clubID, role)
    )
    conn.commit()

    print("\nMembership added successfully!")

def add_club(conn, cursor):
    clubID = input("\nEnter club ID: ").strip()
    clubName = input("\nEnter club name: ").strip()
    description = input("\nEnter club description: ").strip()


    cursor.execute("SELECT 1 FROM Club WHERE Club_ID = ?", (clubID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A club with that ID already exists. Please choose a different ID.")
        return  

    cursor.execute(
        "INSERT INTO Club (Club_ID, Club_Name, Description) VALUES (?, ?, ?)",
        (clubID, clubName, description)
    )
    conn.commit()

    print("\nClub added successfully!")


def add_member_event(conn, cursor):
    eventID = input("\nEnter event ID: ").strip()
    clubID = input("\nEnter club ID: ").strip()
    MemberID = input("\nEnter member ID: ").strip()
    roomNum = input("\nEnter room number: ").strip()
    activity = input("\nEnter meeting activity: ").strip()

    cursor.execute("SELECT 1 FROM Member_Event WHERE Event_ID = ?", (eventID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A member event with that ID already exists. Please choose a different ID.")
        return

    cursor.execute(
        "INSERT INTO Member_Event (Event_ID, Club_ID, Member_ID, Room_Number, Activity) VALUES (?, ?, ?, ?, ?)",
        (eventID, clubID, MemberID, roomNum, activity)
    )
    conn.commit()

    print("\nMember Event added successfully!")

def add_public_event(conn, cursor):
    eventID = input("\nEnter event ID: ").strip()
    clubID = input("\nEnter club ID: ").strip()
    roomNum = input("\nEnter room number: ").strip()
    activity = input("\nEnter meeting activity: ").strip()

    cursor.execute("SELECT 1 FROM Public_Event WHERE Event_ID = ?", (eventID,))
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A public event with that ID already exists. Please choose a different ID.")
        return

    cursor.execute(
        "INSERT INTO Public_Event (Event_ID, Club_ID, Room_Number, Activity) VALUES (?, ?, ?, ?)",
        (eventID, clubID, roomNum, activity)
    )
    conn.commit()

    print("\nPublic Event added successfully!")

def add_meeting_room(conn, cursor):
    roomNum = input("\nEnter room number: ").strip()
    building = input("\nEnter building: ").strip()
    capacity = input("\nEnter meeting capacity: ").strip()

    # Check if room already exists in this building
    cursor.execute(
        "SELECT 1 FROM Meeting_Room WHERE Building = ? AND Room_Number = ?",
        (building, roomNum)
    )
    idExists = cursor.fetchone()

    if idExists:
        print("\nError: A meeting in that room already exists. Please choose a different room.")
        return

    cursor.execute(
        "INSERT INTO Meeting_Room (Room_Number, Building, Capacity) VALUES (?, ?, ?)",
        (roomNum, building, capacity)
    )
    conn.commit()

    print("\Meeting Room added successfully!")