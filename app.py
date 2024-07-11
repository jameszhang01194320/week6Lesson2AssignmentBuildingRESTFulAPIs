# Lesson 2: Assignment | Building RESTFul APIs
# ________________________________________
# 1. Managing a Fitness Center Database
# Objective: The aim of this assignment is to develop a Flask application to manage a fitness center's database, focusing on interacting with the Members and WorkoutSessions tables. This will enhance your skills in building RESTful APIs using Flask, handling database operations, and implementing CRUD functionalities.


# Task 1: Setting Up the Flask Environment and Database Connection
# •	Create a new Flask project and set up a virtual environment.
# •	Install necessary packages like Flask, Flask-Marshmallow, and MySQL connector.
# •	Establish a connection to your MySQL database.
# •	Use the Members and WorkoutSessions tables used on previous Lessons
# Expected Outcome: A Flask project with a connected database and the required tables created.
# Task 2: Implementing CRUD Operations for Members
# •	Create Flask routes to add, retrieve, update, and delete members from the Members table.
# •	Use appropriate HTTP methods: POST for adding, GET for retrieving, PUT for updating, and DELETE for deleting members.
# •	Ensure to handle any errors and return appropriate responses.
# Expected Outcome: Functional endpoints for managing members in the database with proper error handling.
# Task 3: Managing Workout Sessions
# •	Develop routes to schedule, update, and view workout sessions.
# •	Implement a route to retrieve all workout sessions for a specific member.
# Expected Outcome: A comprehensive set of endpoints for scheduling and viewing workout sessions, with the ability to retrieve detailed information about each session.

"""
1. Create a new directory for the project:
    
    mkdir week6_project_BuildingRESTFulAPIs

2.  Set up a virtual environment:
    python -m venv venv

3. Activate the virtual environment:
    # On Windows:
    venv/Scripts/activate

    Activate the virtual environment:
    # On Windows:
    venv/Scripts/activate

    Install Necessary Packages:
    pip install sqlalchemy marshmallow-sqlalchemy Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow mysql-connector-python


    Using MySQL workbench create table Members and WorkoutSessions 
    
4. Create a Python file app.py for Flask application and set up the database connection.
app.py:
"""
# from sqlalchemy.orm import Session
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from marshmallow import ValidationError
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import exc
from datetime import datetime
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import SQLAlchemyError  #, IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:8832@localhost/ecom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init SQLAlchemy
db = SQLAlchemy(app)

# init Marshmallow
ma = Marshmallow(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    workouts = db.relationship('WorkoutSession', backref='member', cascade="all, delete-orphan", lazy=True)

class WorkoutSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    location = db.Column(db.String(100)) 
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

# Member schema
class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member

# WorkoutSession schema
class WorkoutSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutSession
        include_fk = True

workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)


# init schema
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)
session_schema = WorkoutSessionSchema()
sessions_schema = WorkoutSessionSchema(many=True)


# Set up logging
logging.basicConfig(level=logging.DEBUG)



# create table

with app.app_context():
    db.create_all()

# add member


@app.route('/members', methods=['GET'])
def get_members():
    try:
        logging.debug("Fetching all members from the database")
        all_members = Member.query.all()
        result = [{'id': member.id, 'name': member.name, 'email': member.email, 'age': member.age} for member in all_members]
        return jsonify(result), 200
    except exc.SQLAlchemyError as e:
        logging.error(f"Error fetching members: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    try:
        logging.debug(f"Fetching member with id {id}")
        member = db.session.get(Member, id)
        if not member:
            logging.warning(f"Member with id {id} not found")
            return jsonify({'error': 'Member not found'}), 404
        result = {'id': member.id, 'name': member.name, 'email': member.email, 'age': member.age}
        return jsonify(result), 200
    except exc.SQLAlchemyError as e:
        logging.error(f"Error fetching member: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    try:
        logging.debug(f"Adding new member with data {data}")
        new_member = Member(name=data['name'], email=data['email'], age=data['age'])
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'New member added'}), 201
    except exc.SQLAlchemyError as e:
        logging.error(f"Error adding member: {str(e)}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 400




# # update
# @app.route('/members/<int:id>', methods=['PUT'])
# def update_member(id):
#     member = db.session.get(Member, id) #Member.query.get(id)
#     if member is None:
#         return jsonify({'message': 'Member not found'}), 404
    
#     name = request.json.get('name', member.name)
#     email = request.json.get('email', member.email)
    
#     try:
#         member.name = name
#         member.email = email
#         db.session.commit()
#         return member_schema.jsonify(member)
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'message': str(e)}), 400



# update member
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    app.logger.info(f"Received data for update: {data}")
    name = data.get('name')
    email = data.get('email')
    age = data.get('age')

    try:
        member = db.session.get(Member, id)
        if not member:
            return jsonify({"error": "Member not found"}), 404

        app.logger.info(f"Original member data: {member_schema.dump(member)}")

        if name:
            member.name = name
        if email:
            member.email = email
        if age:
            member.age = age

        app.logger.info(f"Member data before commit: {member_schema.dump(member)}")
        db.session.commit()
        app.logger.info(f"Member data after commit: {member_schema.dump(member)}")
        return jsonify({"message": "Member updated successfully", "member": member_schema.dump(member)}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        app.logger.error(f"Error updating member: {e}")
        return jsonify({"error": str(e)}), 400









@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        logging.debug(f"Deleting member with id {id}")
        member = db.session.get(Member, id)
        if not member:
            logging.warning(f"Member with id {id} not found")
            return jsonify({'error': 'Member not found'}), 404
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted'}), 200
    except exc.SQLAlchemyError as e:
        logging.error(f"Error deleting member: {str(e)}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 400



# Get all WorkoutSessions
@app.route('/workouts', methods=['GET'])
def get_workouts():
    all_workouts = WorkoutSession.query.all()
    result = workout_sessions_schema.dump(all_workouts)
    return jsonify(result)

# Get single WorkoutSession
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = WorkoutSession.query.get(id)
    if workout is None:
        return jsonify({'message': 'Workout not found'}), 404
    return workout_session_schema.jsonify(workout)




# create new workout
@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    new_workout = WorkoutSession(
        date=datetime.fromisoformat(data['date']),
        duration=data['duration'],
        member_id=data['member_id']
    )
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({'message': 'Workout session added'}), 201


@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout_session(id):
    workout = db.session.get(WorkoutSession, id)
    if not workout:
        return jsonify({"error": "Workout session not found"}), 404
    
    data = request.get_json()
    
    try:
        workout.date = data['date']
        workout.duration = data['duration']
        workout.location = data['location']
        workout.member_id = data['member_id']
        
        db.session.commit()
        
        return jsonify({"message": "Workout session updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



# Route to retrieve workout sessions for a specific member
@app.route('/members/<int:member_id>/workout-sessions', methods=['GET'])
def get_workout_sessions_for_member(member_id):
    try:
        member_sessions = db.session.query(WorkoutSession).filter_by(member_id=member_id).all()
        return jsonify(sessions_schema.dump(member_sessions)), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)


