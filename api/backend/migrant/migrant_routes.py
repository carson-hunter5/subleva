from flask import Flask, Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

migrant = Blueprint('migrant', __name__)
app = Flask(__name__)

# Get all appointments from the database for a specifc migrant
@migrant.route('/migrant/appointments/<id>', methods=['GET'])
def get_migrant_appointment(id): 
     cursor = db.get_db().cursor()
     query  = f"""SELECT subject, appDate, weekday, v.name, COUNT(aa.attendeeID) FROM appointments JOIN appointmentAttendees
                    aa  ON appointments.appointmentID = aa.appointmentID 
                    JOIN volunteers v ON v.id = appointments.volunteerID WHERE aa.attendeeID = {id} GROUP BY aa.appointmentID"""
     cursor.execute(query)

    # grab the column headers from the returned data
     column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
     json_data = []

    # fetch all the data from the cursor
     theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
     for row in theData:
        json_data.append(dict(zip(column_headers, row)))

     return jsonify(json_data)

# Get all appointments from the database based on the weekday
@migrant.route('/migrant/show_appt/<weekday>', methods=['GET'])
def get_appt(weekday):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f"""SELECT appointments.appointmentID, subject, appDate, weekday, v.name, COUNT(aa.attendeeID) 
                   FROM appointments 
                   JOIN appointmentAttendees aa ON appointments.appointmentID = aa.appointmentID 
                   JOIN volunteers v ON appointments.volunteerID = v.id 
                   WHERE weekday = '{weekday}' 
                   GROUP BY aa.appointmentID""")

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Adds the assigned migrantID to the attendee appointments table
@migrant.route('/make_appointment', methods=['POST'])
def add_appointment():
    try:
        # Collecting data from the request object
        the_data = request.json
        current_app.logger.info(the_data)

        attendeeID = the_data['attendeeID']
        appointmentID = the_data['appointmentID']

        # Constructing the query using parameterized queries to prevent SQL injection
        query = f"""INSERT INTO appointmentAttendees (attendeeID, appointmentID) VALUES ('{attendeeID}','{appointmentID}')"""
        current_app.logger.info(query)

        # Executing and committing the insert statement
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        return jsonify({'message': 'Appointment added successfully'}), 200
    except Exception as e:
        current_app.logger.error(f"Error adding appointment: {e}")
        return jsonify({'error': 'Failed to add appointment', 'details': str(e)}), 500

# Show all the appoinments linked to a certain migrant
@migrant.route('/migrant/appointments_cancel/<id>', methods=['GET'])
def get_migrant_appointment_to_cancel(id): 
     cursor = db.get_db().cursor()
     query  = f"""SELECT  appDate as Date, v.name, appointments.appointmentID FROM appointments JOIN appointmentAttendees
                    aa  ON appointments.appointmentID = aa.appointmentID 
                    JOIN volunteers v ON v.id = appointments.volunteerID WHERE aa.attendeeID = {id} GROUP BY aa.appointmentID"""
     cursor.execute(query)

    # grab the column headers from the returned data
     column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
     json_data = []

    # fetch all the data from the cursor
     theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
     for row in theData:
        json_data.append(dict(zip(column_headers, row)))

     return jsonify(json_data)

# Delete the appointment for a specifc migrant
@migrant.route('/migrant/appointment_delete/<migrantID>/<apptID>', methods=['DELETE'])
def delete_migrant_appointment(migrantID, apptID):
    current_app.logger.info('DELETE /migrant/appointment/<migrantID> route')
    cursor = db.get_db().cursor()
    try:
        cursor.execute(f"""DELETE FROM appointmentAttendees WHERE AttendeeID = %s AND appointmentID = %s""", (migrantID, apptID))
        db.get_db().commit()
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting appointment: {e}")
        return jsonify({'error': 'Failed to delete appointment', 'details': str(e)}), 500


# Get all posts from the database for a specific migrant
@migrant.route('/migrant/posts', methods=['GET'])
def get_posts():

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT postContent, displayName, createdAt FROM posts ORDER BY createdAt DESC LIMIT 10')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# Gets a all posts from a certain migrant
@migrant.route('/migrant/<migrantID>', methods=['GET'])
def get_post(migrantID):
    current_app.logger.info('GET /posts/<migrantID> route')
    cursor = db.get_db().cursor()
    cursor.execute('select migrantID from users where id = {0}'.format(migrantID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Creates a new post for a migrant
@migrant.route('/migrant/add_post', methods=['POST'])
def add_new_post():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    postContent = the_data['postContent']
    displayName = the_data['displayName']
    migrantID = the_data['migrantID']

    # Constructing the query
    query = 'INSERT INTO posts (postContent, createdAt, displayName, migrantID) VALUES ('
    query += "'" + postContent + "',"
    query += 'NOW(),'
    query += "'" + displayName + "',"
    query += "'" + str(migrantID) + "')"
    
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
      
    return 'New Post'

# Delete the post for a specifc migrant
@migrant.route('/migrant/post/<postID>', methods=['DELETE'])
def delete_migrant_post(postID):
    current_app.logger.info('DELETE /migrant/post/<postID> route')
    
    query = 'DELETE FROM posts WHERE postID = {0}'.format(postID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Post deleted!'

# Get all community events from the DB 
@migrant.route('/migrant/events', methods=['GET'])
def get_events():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('select eventDate, name, duration from communityEvent')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)