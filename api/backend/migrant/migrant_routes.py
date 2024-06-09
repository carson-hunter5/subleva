from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

migrant = Blueprint('migrant', __name__)

##Appointment Calls

# Get all appointments from the database for a specifc migrant
@migrant.route('/migrant/appointments/<attendeeID>', methods=['GET'])
def get_appointments(attendeeID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f"""SELECT appointmentID FROM appointmentAttendees WHERE attendeeID = {attendeeID}""")

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

# Get all appointments from the database
@migrant.route('/migrant/show_appt/<weekday>', methods=['GET'])
def get_appt(weekday):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f"""SELECT subject, appDate, weekday, v.name, COUNT(aa.attendeeID) FROM appointments JOIN appointmentAttendees
                    aa  ON appointments.appointmentID = aa.appointmentID 
                   JOIN volunteers v on appointments.volunteerID = v.id 
                   WHERE weekday = '{weekday}' GROUP BY aa.appointmentID""")

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



# Edit the appointment for a specifc migrant
@migrant.route('/migrant/appointment', methods=['PUT'])
def update_migrant_appointment():
    current_app.logger.info('PUT /migrant route')
    migrant_info = request.json
    attendeeID = migrant_info['attendeeID']

    query = 'UPDATE appointmentAttendees SET attendeeID = %s'
    data = (attendeeID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'appointment updated!'

# Delete the appointment for a specifc migrant
@migrant.route('/migrant/appointment_delete/<date>', methods=['DELETE'])
def delete_migrant_appointment(date):
    current_app.logger.info('DELETE /migrant/appointment/<date> route')
    cursor = db.get_db().cursor()
    cursor.execute(f"""DELETE FROM appointments WHERE appDate = {date}""")
    db.get_db().commit()

#Posts
# Get all posts from the database 
@migrant.route('/migrant/posts', methods=['GET'])
def get_posts():

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT postContent, displayName, createdAt FROM posts ORDER BY createdAt DESC LIMIT 7')

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


# Get all posts from the database for a specific migrant
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
    postID = the_data['postID']
    postContent = the_data['postContent']
    displayName = the_data['displayName']
    migrantID = the_data['migrantID']

    # Constructing the query
    query = 'INSERT INTO posts (postID, postContent, createdAt, displayName, migrantID) VALUES ('
    query += "'" + str(postID) + "',"
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

# Edit the post for a specifc migrant
@migrant.route('/migrant/post', methods=['PUT'])
def update_migrant_post():
    current_app.logger.info('PUT /migrant route')
    post_info = request.json
    post_content = post_info['postContent']
    displayName = post_info['displayName']

    query = 'UPDATE posts SET post_content = %s, displayName = %s'
    data = (post_content, displayName)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Post updated!'

# Delete the post for a specifc migrant
@migrant.route('/migrant/post/<postID>', methods=['DELETE'])
def delete_migrant_post(postID):
    current_app.logger.info('DELETE /migrant/post/<postID> route')
    
    query = 'DELETE FROM posts WHERE postID = {0}'.format(postID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Post deleted!'

# Community Events

# Get all community events from the DB for a 
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

@migrant.route('/make_appointment', methods=['POST'])
def add_appointment():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    attendeeID = the_data['attendeeID']
    appointmentID = the_data['appointmentID']

    # Constructing the query
    query = f"""insert into appointmentAttendees (attendeeID, appointmentID) values ('{attendeeID}','{appointmentID}')"""
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Appointment Reserved'