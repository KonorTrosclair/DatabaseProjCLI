-- q1: students w/ their clubs + roles
SELECT
  s.Student_ID,
  s.Name AS StudentName,
  c.Club_ID,
  c.Club_Name AS ClubName,
  m.Role
FROM Membership m
JOIN Student s ON m.Student_ID = s.Student_ID
JOIN Club c ON m.Club_ID = c.Club_ID
ORDER BY s.Student_ID, c.Club_ID;


-- q2: member count for each club
SELECT
  c.Club_ID,
  c.Club_Name,
  COUNT(m.Member_ID) AS MemberCount
FROM Club c
LEFT JOIN Membership m ON c.Club_ID = m.Club_ID
GROUP BY c.Club_ID, c.Club_Name
ORDER BY c.Club_ID;


-- q3: member-only events w/ student + club info
SELECT
  me.Event_ID,
  c.Club_Name,
  s.Student_ID,
  s.Name AS StudentName,
  me.Activity,
  me.Room_Number
FROM Member_Event me
JOIN Membership m ON me.Member_ID = m.Member_ID
JOIN Student s ON m.Student_ID = s.Student_ID
JOIN Club c ON me.Club_ID = c.Club_ID
ORDER BY me.Event_ID;


-- q4: public events w/ "duck" in activity
SELECT
  pe.Event_ID,
  c.Club_Name,
  pe.Activity,
  pe.Room_Number
FROM Public_Event pe
JOIN Club c ON pe.Club_ID = c.Club_ID
WHERE pe.Activity LIKE '%duck%'
ORDER BY pe.Event_ID;


-- q5: member event counts vs public event counts
SELECT
  c.Club_ID,
  c.Club_Name,
  COUNT(DISTINCT me.Event_ID) AS MemberEvents,
  COUNT(DISTINCT pe.Event_ID) AS PublicEvents,
  COUNT(DISTINCT me.Event_ID) + COUNT(DISTINCT pe.Event_ID) AS TotalEvents
FROM Club c
LEFT JOIN Member_Event me ON c.Club_ID = me.Club_ID
LEFT JOIN Public_Event pe ON c.Club_ID = pe.Club_ID
GROUP BY c.Club_ID, c.Club_Name
ORDER BY c.Club_ID;