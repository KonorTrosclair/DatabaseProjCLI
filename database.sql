DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Club;
DROP TABLE IF EXISTS Membership;
DROP TABLE IF EXISTS Member_Event;
DROP TABLE IF EXISTS Public_Event;
DROP TABLE IF EXISTS Meeting_Room;

CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Major VARCHAR(100) NOT NULL,
    Class VARCHAR(100) NOT NULL
);

CREATE TABLE Faculty (
    Faculty_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL
);

CREATE TABLE Club (
    Club_ID INT PRIMARY KEY,
    Club_Name VARCHAR(100) NOT NULL,
    Description VARCHAR(100) NOT NULL
);

CREATE TABLE Membership (
    Student_ID INT NOT NULL,
    Member_ID INT NOT NULL,
    Club_ID INT NOT NULL,
    Role VARCHAR(100) NOT NULL,
    PRIMARY KEY (Student_ID, Member_ID, Club_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Club_ID) REFERENCES Club(Club_ID)
);

CREATE TABLE Member_Event (
    Event_ID INT NOT NULL,
    Club_ID INT NOT NULL,
    Member_ID INT NOT NULL,
    Room_Number INT NOT NULL,
    Activity VARCHAR(100) NOT NULL,
    PRIMARY KEY (Event_ID, Club_ID, Member_ID),
    FOREIGN KEY (Club_ID) REFERENCES Club(Club_ID),
    FOREIGN KEY (Member_ID) REFERENCES Membership(Member_ID)
);

CREATE TABLE Public_Event (
    Event_ID INT NOT NULL,
    Club_ID INT NOT NULL,
    Room_Number INT NOT NULL,
    Activity VARCHAR(100) NOT NULL,
    PRIMARY KEY (Event_ID, Club_ID),
    FOREIGN KEY (Club_ID) REFERENCES Club(Club_ID)
);

CREATE TABLE Meeting_Room (
    Room_Number INT NOT NULL,
    Building VARCHAR(100) NOT NULL,
    Capacity INT,
    PRIMARY KEY (Room_Number, Building)
);


INSERT INTO Student (Student_ID, Name, Major, Class) VALUES
(89450, 'Jordan', 'Computer Science', 'Compiler Construction'),
(89555, 'Robert', 'Mechanical Engineering', 'Thermodynamics'),
(89460, 'Shaquille', 'Chemical Engineering', 'CHEM4000'),
(89775, 'Alice', 'Computer Science', 'Database Design'),
(89651, 'Cassandra', 'Electrical Engineering', 'Circuit Design');

INSERT INTO Faculty (Faculty_ID, Name, Department) VALUES
(101, 'Denny', 'CSC'),
(102, 'Saha-Roy', 'CSC'),
(103, 'Eldewahi', 'CSC'),
(104, 'PersonA', 'ENG'),
(105, 'PersonB', 'IDK');

INSERT INTO Club (Club_ID, Club_Name, Description) VALUES
(1, 'Robotics', 'Makes robots'),
(2, 'Board Game Club', 'Plays board games'),
(3, 'SASE', 'Creates opportunities'),
(4, 'ClubA', 'description A'),
(5, 'ClubB', 'description B');


INSERT INTO Membership (Student_ID, Member_ID, Club_ID, Role) VALUES
(89450, 1001, 2, 'Member'),
(89555, 1002, 3, 'President'),
(89460, 1003, 4, 'Vice President'),
(89775, 1004, 1, 'Treasurer'),
(89651, 1005, 5, 'Member');

INSERT INTO Member_Event(Event_ID, Club_ID, Member_ID, Room_Number, Activity) VALUES
(45000, 1, 1004, 67, 'Something important'),
(46000, 2, 1001, 20, 'Feeding ducks'),
(44000, 3, 1002, 33, 'Feeding other ducks'),
(47000, 4, 1003, 22, 'feeding geese'),
(48000, 5, 1005, 10, 'feeding geese to ducks');

INSERT INTO Public_Event(Event_ID, Club_ID, Room_Number, Activity) VALUES
(43000, 1, 49, 'something cool'),
(42000, 2, 64, 'something not cool'),
(41000, 3, 45, 'something with ducks'),
(40000, 4, 12, 'something without ducks'),
(39000, 5, 10, 'something very normal');

INSERT INTO Meeting_Room(Room_Number, Building, Capacity) VALUES
(55, 'PFT', 1000),
(43, 'Lockett', 10000),
(25, 'Tureaud', 12),
(44, 'Coates', 10),
(87, 'Nicholson', 100);
