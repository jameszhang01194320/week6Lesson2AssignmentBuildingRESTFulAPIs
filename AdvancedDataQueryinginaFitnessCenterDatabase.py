# 2.Advanced Data Querying in a Fitness Center Database
# objective:The goal of this assignment is to enhance your skills in advanced SQL querying within a Flask application context.You'll Focus on
# implementing specific SQL Functionalities,such as DISTINCT,COUNT,and BETWEEN,to extract meaningFul information from the Fitness center's database.
# Task 1:SQL DISTINCT Usage
# Problem Statement:Identify the distinct trainers working with gym members.
# Expected Outcome:A list of unique trainer IDs from the Members table.
# Example Code Structure:
# 'python
# @app.route(/trainers/distinct',methods=['GET)
# def list distinct trainers(:
# Connect to the database
# SQL query using DISTINCT to Find unique trainer IDs
# Execute and fetch results
# Return the list of unique trainer IDs
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8832",
        database="ecom"
    )
    return connection

@app.route('/trainers/distinct', methods=['GET'])
def list_distinct_trainers():
    """Endpoint to get a list of unique trainer IDs from the Members table."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # SQL query using DISTINCT to find unique trainer IDs
        query = "SELECT DISTINCT trainer_id FROM Members"
        cursor.execute(query)
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Extract trainer IDs from results
        trainer_ids = [row[0] for row in results]
        
        return jsonify(trainer_ids)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()



# if __name__ == '__main__':
#     app.run(debug=True)

# Task 2:SQL COUNT Functionality
# Problem Statement:Count the total number of members assigned to each trainer,Focusing on understanding the GROUP BY clause.
# Expected Outcome:A count of members grouped by their trainer IDs.
# Example Code Structure:
# .python
# @app.route(/trainers/count_members',methods=['GET])
# def count_members_per_trainer(:
# Connect to the database
# SQL query using COUNT and GROUP BY to count members per trainer
# Execute and fetch results
# Return the count of members for each trainer

@app.route('/trainers/count_members', methods=['GET'])
def count_members_per_trainer():
    """Endpoint to count the total number of members assigned to each trainer."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # SQL query using COUNT and GROUP BY to count members per trainer
        query = """
            SELECT trainer_id, COUNT(*) as member_count
            FROM Members
            GROUP BY trainer_id
        """
        cursor.execute(query)
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Structure the results as a list of dictionaries
        count_results = [{'trainer_id': row[0], 'member_count': row[1]} for row in results]
        
        return jsonify(count_results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

# if __name__ == '__main__':
#     app.run(debug=True)


# Task 3:SQL BETWEEN Usage
# Problem Statement:Retrieve the details of members whose ages fall between 25 and 30.
# Expected Outcome:A list of members (including their names,ages,and trainer IDs)who are between the ages of 25 and 30.
# Example Code Structure:
# ..python
# @app.route(/members/age_range',methods=['GET])
# def get_members_in_age_range(start_age=25,end_age=30):
# Connect to the database
# SQL query using BETWEEN to Filter members within a certain age range
# Execute and fetch results
# Return the list of members within the specified age range

@app.route('/members/age_range', methods=['GET'])
def get_members_in_age_range():
    """Endpoint to retrieve members within a specified age range."""
    start_age = 25  # Default start age
    end_age = 30    # Default end age
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        # SQL query using BETWEEN to filter members within a certain age range
        query = """
            SELECT name, age, trainer_id
            FROM Members
            WHERE age BETWEEN %s AND %s
        """
        cursor.execute(query, (start_age, end_age))
        
        # Fetch the results
        results = cursor.fetchall()
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)