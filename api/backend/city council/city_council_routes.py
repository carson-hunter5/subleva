from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

city_council = Blueprint('city_council', __name__)

# Community Events

# Get all community events from the DB
@city_council.route('/city_council', methods=['GET'])
def get_communityEvents():
    current_app.logger.info('city_council_routes.py: GET /city_council/communityEvents')
    cursor = db.get_db().cursor()
    cursor.execute('select date, eventID, name,\
        duration, venueCapacity from communityEvents')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Creates a new appointment for a migrant
@city_council.route('/city_council', methods=['POST'])
def add_communityEvent():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    date = the_data['date']
    eventID = the_data['eventID']
    name = the_data['name']
    duration = the_data['duration']
    venueCapacity = the_data['venueCapacity']

    # Constructing the query
    query = 'insert into communityEvent (date, eventID, name, duration, venueCapacity) values ("'
    query += date + '", '
    query += eventID + '", "'
    query += name + '", "'
    query += duration + '", "'
    query += venueCapacity + '", "'
    
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
    duration = event_info['duration']
    name = event_info['name']
    date = event_info['date']
    venueCapacity = event_info['venueCapacity']

    query = 'UPDATE communityEvent SET duration = %s, name = %s, date = %s, venueCapacity = %s'
    data = (duration, name, date, venueCapacity)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Event updated!'

# Delete the event for a specifc migrant
@city_council.route('/city_council/communityEvent/<eventID>', methods=['DELETE'])
def delete_event(eventID):
    current_app.logger.info('DELETE /city_council/communityEvent/<eventID> route')
    
    query = 'DELETE FROM communityEvent WHERE eventtID = {0}'.format(eventID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Event cancelled!'


# Appointments

# Get all appointments from the DB
@city_council.route('/city_council', methods=['GET'])
def get_appointments():
    current_app.logger.info('city_council_routes.py: GET /appointments')
    cursor = db.get_db().cursor()
    cursor.execute('select migrantID, volunteerID, date,\
        appointmentID from communityEvent')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


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