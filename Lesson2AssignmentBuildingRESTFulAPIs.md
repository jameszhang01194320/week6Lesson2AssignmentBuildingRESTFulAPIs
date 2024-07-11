Lesson 2: Assignment | Building RESTFul APIs
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
________________________________________
1. Managing a Fitness Center Database
Objective: The aim of this assignment is to develop a Flask application to manage a fitness center's database, focusing on interacting with the Members and WorkoutSessions tables. This will enhance your skills in building RESTful APIs using Flask, handling database operations, and implementing CRUD functionalities.

Task 1: Setting Up the Flask Environment and Database Connection
•	Create a new Flask project and set up a virtual environment.
•	Install necessary packages like Flask, Flask-Marshmallow, and MySQL connector.
•	Establish a connection to your MySQL database.
•	Use the Members and WorkoutSessions tables used on previous Lessons
Expected Outcome: A Flask project with a connected database and the required tables created.

Task 2: Implementing CRUD Operations for Members
•	Create Flask routes to add, retrieve, update, and delete members from the Members table.
•	Use appropriate HTTP methods: POST for adding, GET for retrieving, PUT for updating, and DELETE for deleting members.
•	Ensure to handle any errors and return appropriate responses.
Expected Outcome: Functional endpoints for managing members in the database with proper error handling.
Code Example:
@app.route('/members', methods=['POST'])
def add_member():
    # Logic to add a member
    pass

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    # Logic to retrieve a member
    pass

# other routes to update and delete

Task 3: Managing Workout Sessions
•	Develop routes to schedule, update, and view workout sessions.
•	Implement a route to retrieve all workout sessions for a specific member.
Expected Outcome: A comprehensive set of endpoints for scheduling and viewing workout sessions, with the ability to retrieve detailed information about each session.


2.Advanced Data Querying in a Fitness Center Database
objective:The goal of this assignment is to enhance your skills in advanced SQL querying within a Flask application context.You'll Focus on
implementing specific SQL Functionalities,such as DISTINCT,COUNT,and BETWEEN,to extract meaningFul information from the Fitness center's database.
Task 1:SQL DISTINCT Usage
Problem Statement:Identify the distinct trainers working with gym members.
Expected Outcome:A list of unique trainer IDs from the Members table.
Example Code Structure:
'python
@app.route(/trainers/distinct',methods=['GET)
def list distinct trainers(:
Connect to the database
SQL query using DISTINCT to Find unique trainer IDs
Execute and fetch results
Return the list of unique trainer IDs

Task 2:SQL COUNT Functionality
Problem Statement:Count the total number of members assigned to each trainer,Focusing on understanding the GROUP BY clause.
Expected Outcome:A count of members grouped by their trainer IDs.
Example Code Structure:
.python
@app.route(/trainers/count_members',methods=['GET])
def count_members_per_trainer(:
Connect to the database
SQL query using COUNT and GROUP BY to count members per trainer
Execute and fetch results
Return the count of members for each trainer

Task 3:SQL BETWEEN Usage
Problem Statement:Retrieve the details of members whose ages fall between 25 and 30.
Expected Outcome:A list of members (including their names,ages,and trainer IDs)who are between the ages of 25 and 30.
Example Code Structure:
..python
@app.route(/members/age_range',methods=['GET])
def get_members_in_age_range(start_age=25,end_age=30):
Connect to the database
SQL query using BETWEEN to Filter members within a certain age range
Execute and fetch results
Return the list of members within the specified age range


