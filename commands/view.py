import sqlite3
import os

def view_command():
    db_path = os.path.abspath("database.db")
    print("Connecting to:", db_path)

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    print("\nWhat field would you like to view:")
    print("1. All Faculty Members")
    print("2. All Students")
    print("3. All Memberships")
    print("4. All Clubs")
    print("5. All Member Events")
    print("6. All Public Events")
    print("7. All Meeting Rooms")

    field = input("\nEnter choice (1-7): ").strip()
    # insertedField = ""

    if field == "1":
        print("You selected: Faculty")
        # insertedField = "Faculty"
        view_faculty(conn, cursor)
    elif field == "2":
        print("You selected: Student")
        # insertedField = "Student"
        view_student(conn, cursor)
    elif field == "3":
        print("You selected: Membership")
        # insertedField = "Membership"
        view_membership(conn, cursor)
    elif field == "4":
        print("You selected: Club")
        # insertedField = "Club"
        view_club(conn, cursor)
    elif field == "5":
        print("You selected: Member Event")
        # insertedField = "Member_Event"
        view_member_event(conn, cursor)
    elif field == "6":
        print("You selected: Public Event")
        # insertedField = "Public_Event"
        view_public_event(conn, cursor)
    elif field == "7":
        print("You selected: Meeting Room")
        # insertedField = "Meeting_Room"
        view_meeting_room(conn, cursor)
    else:
        print("Invalid choice. Please enter 1-7.")

    
def view_faculty(conn, cursor):
    print("\nFaculty:")
    cursor.execute("SELECT * FROM Faculty")
    faculty = cursor.fetchall()
    for fac in faculty:
        print(f"ID: {fac[0]}, Name: {fac[1]}, Department: {fac[2]}")

def view_student(conn, cursor):
    print("\nStudents:")
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    for stu in students:
        print(f"ID: {stu[0]}, Name: {stu[1]}, Major: {stu[2]}, Class: {stu[3]}")

def view_membership(conn, cursor):
    print("\nMemberships:")
    cursor.execute("SELECT * FROM Membership")
    memberships = cursor.fetchall()
    for mem in memberships:
        print(f"Student ID: {mem[0]}, Member ID: {mem[1]}, Club ID: {mem[2]}, Role: {mem[3]}")

def view_club(conn, cursor):
    print("\nClubs:")
    cursor.execute("SELECT * FROM Club")
    clubs = cursor.fetchall()
    for club in clubs:
        print(f"ID: {club[0]}, Name: {club[1]}, Description: {club[2]}")

def view_member_event(conn, cursor):
    print("\nMember Events:")
    cursor.execute("SELECT * FROM Member_Event")
    memberEvents = cursor.fetchall()
    for memE in memberEvents:
        print(f"Event ID: {memE[0]}, Club ID: {memE[1]}, Member ID: {memE[2]}, Room: {memE[3]}, Activity: {memE[4]}")

def view_public_event(conn, cursor):
    print("\nPublic Events:")
    cursor.execute("SELECT * FROM Public_Event")
    publicEvents = cursor.fetchall()
    for pubE in publicEvents:
        print(f"Event ID: {pubE[0]}, Club ID: {pubE[1]}, Room: {pubE[2]}, Activity, {pubE[3]}")

def view_meeting_room(conn, cursor):
    print("\nMeeting Rooms:")
    cursor.execute("SELECT * FROM Meeting_Room")
    meetingRooms = cursor.fetchall()
    for meetR in meetingRooms:
        print(f"Room: {meetR[0]}, Building: {meetR[1]}, Capacity: {meetR[2]}")

def view_student_clubs_and_roles():
    print()

def view_member_count():
    print()

def view_member_only_events_with_student_club_info():
    print()
