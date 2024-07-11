 Managing a Fitness Center Database
----------------------------------------------
1: Setting Up the Flask Environment and Database Connection
•	Create a new Flask project and set up a virtual environment.
•	pip install sqlalchemy marshmallow-sqlalchemy Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow mysql-connector-python
•	Establish a connection to your MySQL database.
•	Use the Members and WorkoutSessions tables 

2: Implementing CRUD Operations for Members
•	Create Flask routes to add, retrieve, update, and delete members from the Members table.
•	Use appropriate HTTP methods: POST for adding, GET for retrieving, PUT for updating, and DELETE for deleting members.
•	Ensure to handle any errors and return appropriate responses.

3: Managing Workout Sessions
•	Develop routes to schedule, update, and view workout sessions.
•	Implement a route to retrieve all workout sessions for a specific member.



Advanced Data Querying in a Fitness Center Database
--------------------------------------------------------
1:SQL DISTINCT Usage
Problem Statement:Identify the distinct trainers working with gym members.

Return the list of unique trainer IDs
@app.route('/trainers/distinct', methods=['GET'])

2:SQL COUNT Functionality
Problem Statement:Count the total number of members assigned to each trainer,Focusing on understanding the GROUP BY clause.
Expected Outcome:A count of members grouped by their trainer IDs.

Connect to the database
SQL query using COUNT and GROUP BY to count members per trainer
Execute and fetch results
Return the count of members for each trainer
@app.route('/trainers/count_members', methods=['GET'])

Task 3:SQL BETWEEN Usage
Problem Statement:Retrieve the details of members whose ages fall between 25 and 30.
Expected Outcome:A list of members (including their names,ages,and trainer IDs)who are between the ages of 25 and 30.

Return the list of members within the specified age range
@app.route('/members/age_range', methods=['GET'])