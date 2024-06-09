from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

city_council = Blueprint('city_council', __name__)

# Community Events

# Get all community events from the DB
@city_council.route('/city_council', methods=['GET'])
def get_events():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('select date, eventID, name,duration, venueCapacity from communityEvent')

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


# Creates a new community event
@city_council.route('/council_add_event', methods=['POST'])
def add_communityEvent():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    date = the_data['date']
    name = the_data['eventName']
    duration = the_data['duration']
    venueCapacity = the_data['venueCapacity']

    # Constructing the query
    query = 'INSERT INTO communityEvent (date, name, duration, venueCapacity) VALUES ('
    query += "'" + date + "',"
    query += "'" + name + "',"
    query += "'" + str(duration) + "',"
    query += "'" + str(venueCapacity) + "')"
    
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'New Event'


# Edit the event for a specifc migrant
@city_council.route('/city_council/communityEvent', methods=['PUT'])
def update_communityEvent():
    current_app.logger.info('PUT /city_council route')
    event_info = request.json
    eventID = event_info['eventID']
    duration = event_info['duration']
    name = event_info['eventName']
    date = event_info['date']
    venueCapacity = event_info['venueCapacity']

    query = f"""UPDATE communityEvent SET duration = {duration}, name = '{name}', date = '{date}', venueCapacity = {venueCapacity} WHERE eventID = {eventID}"""
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Event updated!'

# Delete the event 
@city_council.route('/city_council/communityEvent/<eventID>', methods=['DELETE'])
def delete_event(eventID):
    current_app.logger.info('DELETE /city_council/communityEvent/<eventID> route')
    
    query = f"""DELETE FROM communityEvent WHERE eventID = {eventID}"""
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Event cancelled!'


# Appointments

# Get all appointments 
@city_council.route('/city_council/appointments', methods=['GET'])
def get_appointments():
    current_app.logger.info('city_council_routes.py: GET /appointments')
    cursor = db.get_db().cursor()
    cursor.execute('select volunteerID, date,\
        appointmentID, subject, weekday from appointments')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Creates a new appointment 
@city_council.route('/council/add_appointments', methods=['POST'])
def add_appointment():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    volunteerID = the_data['volunteerID']
    date = the_data['date']
    subject = the_data['subject']
    weekday = the_data['weekday']

    # Constructing the query
    query = 'INSERT INTO appointments (volunteerID, date, subject, weekday) VALUES ('
    query += volunteerID + '", "'
    query += date + '", '
    query += subject + '", '
    query += weekday + '", "'
    
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'New Appointment'

# Edit the appointment
@city_council.route('/city_council/edit_appointments', methods=['PUT'])
def update_appointmentEvent():
    current_app.logger.info('PUT /city_council/appointments route')
    appointment_info = request.json
    volunteerID = appointment_info['volunteerID']
    weekday = appointment_info['weekday']
    subject = appointment_info['subject']
    date = appointment_info['date']
    appointmentID = appointment_info['appointmentID']

    query = f"""UPDATE appointment SET volunteerID = {volunteerID}, subject = '{subject}', date = '{date}', weekday = {weekday} WHERE appointmentID = {appointmentID}"""
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Appointment updated!'

# Delete the appointment 
@city_council.route('/city_council/appointment/<appointmentID>', methods=['DELETE'])
def delete_appointment(appointmentID):
    current_app.logger.info('DELETE /city_council/appointment/<appointmentID> route')
    
    query = f"""DELETE FROM appointments WHERE appointmentID = {appointmentID}"""
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Event cancelled!'

# Demographics

# Get the demographics for a certain cohort of refugees
@city_council.route('/city_council/<cohortID>', methods=['GET'])
def get_demographics(cohortID):
    current_app.logger.info('GET /city_council/<cohortID> route')
    cursor = db.get_db().cursor()
    cursor.execute('select cohortID from refugeeCohort where cohortID = {0}'.format(cohortID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@city_council.route('/city_council/delete_bulletin/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    current_app.logger.info('/city_council/delete_bulletin/<post_id> route')
    query = f"""DELETE FROM posts WHERE postID = {post_id}"""
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Event cancelled!'

@city_council.route('/city_council/bulletin', methods=['GET'])
def get_posts():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT postID, postContent, migrantID, displayName from posts ORDER BY createdAt ASC')

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