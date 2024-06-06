from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
""""
from backend.ml_models.model01 import predict
"""

immigration_official = Blueprint('immigration official', __name__)

# Get population from the database 
@immigration_official.route('/countryStats/<population>', methods=['GET'])
def get_demographics(population):
    current_app.logger.info('GET /countryStats/<population> route')
    cursor = db.get_db().cursor()
    cursor.execute('select countryID from countryStats where countryID = {0}'.format(population))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Community Events

# Get all country stats from the DB
@immigration_official.route('/immigration_official/countryStats', methods=['GET'])
def get_countryStats():
    current_app.logger.info('immigration_official_routes.py: GET /immigration_official/countryStats')
    cursor = db.get_db().cursor()
    cursor.execute('select countryID, year, numApplications,\
        numRejected, numGranted, numOther, numClosed, population, from countryStats')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Creates a new country stat for a country
@immigration_official.route('/immigration_official/newStat', methods=['POST'])
def add_countryStat():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    countryID = the_data['countryID']
    year = the_data['year']
    numApplications = the_data['numApplications']
    numRejected = the_data['numRejected']
    numGranted = the_data['numGranted']
    numOther = the_data['numOther']
    numClosed = the_data['numClosed']
    population = the_data['population']

    # Constructing the query
    query = 'insert into countryStat (countryID, year, numApplications, numRejected, numGranted,numOther,numClosed, population ) values ("'
    query += countryID + '", '
    query += year + '", "'
    query += numApplications + '", "'
    query += numRejected + '", "'
    query += numOther + '", "'
    query += numGranted + '", "'
    query += numClosed + '", "'
    query += population + '", "'
    
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'New Country Stat'


# Edit the country stat 
@immigration_official.route('/immigration_official/editCountryStat', methods=['PUT'])
def update_countryStat():
    current_app.logger.info('PUT /immigration_official/editCountryStat route')
    stat_info = request.json
    year = stat_info['year']
    numApplications = stat_info['numApplications']
    numGranted = stat_info['numGranted']
    numRejected = stat_info['numRejected']
    numOther = stat_info['numOther']
    numClosed = stat_info['numClosed']
    population = stat_info['population']

    query = 'UPDATE countryStat SET year = %s, numApplications = %s, numRejected = %s, numGranted = %s, numOther = %s,numClosed = %s, population = %s'
    data = (year, numApplications, numRejected, numGranted, numOther, numClosed, population)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Country Stat updated!'

# Delete the country stat
@immigration_official.route('/immigration_official/deleteCountryStat', methods=['DELETE'])
def delete_event(countryID):
    current_app.logger.info('DELETE /immigration_official/deleteCountryStat route')
    
    query = 'DELETE FROM countryStat WHERE countryID = {0}'.format(countryID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Country Stat deleted!'


# Get number of applications for a specific country at a given year 
@immigration_official.route('/immigration_official/numApplications', methods=['GET'])
def get_applications_per_year(countryID):
    current_app.logger.info('GET /immigration_official/numApplications route')
    cursor = db.get_db().cursor()
    cursor.execute('select year, numApplications from countryStats where countryID = {0}'.format(countryID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get overall trend of applications for a specific country at a given year 
@immigration_official.route('/immigration_official/applicationTrends', methods=['GET'])
def get_trends_per_year(countryID):
    current_app.logger.info('GET /immigration_official/applicationTrends route')
    cursor = db.get_db().cursor()
    cursor.execute('select year, numApplications, numRejected, numGranted, numOther, numClosed, population from countryStats where countryID = {0}'.format(countryID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
""""
@immigration_official.route('/prediction/<var01>/<var02>/<var03>/<var04>', methods=['GET'])
def predict_value(var01, var02, var03, var04):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')
    current_app.logger.info(f'var03 = {var03}')
    current_app.logger.info(f'var04 = {var04}')

    returnVal = predict(var01, var02, var03, var04)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

"""