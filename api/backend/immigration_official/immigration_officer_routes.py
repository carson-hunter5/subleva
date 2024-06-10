from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict
from backend.ml_models.model02 import train_predict

immigration_official = Blueprint('immigration official', __name__)

# Get population from the database 
@immigration_official.route('/immigration_official/population', methods=['GET'])
def get_demographics(population):
    current_app.logger.info('GET /immigration_official/population route')
    cursor = db.get_db().cursor()
    cursor.execute('select population from countryStats where countryID = {0}'.format(population))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

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

#ml model call for prediction
@immigration_official.route('/prediction/<var01>/<var02>/<var03>/<var04>', methods=['GET'])
def predict_value(var01, var02, var03, var04):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')
    current_app.logger.info(f'var03 = {var03}')
    current_app.logger.info(f'var04 = {var04}')

    var01 = int(var01)
    returnVal = predict(var01, var02, var03, var04)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#gets the countries from the country list
@immigration_official.route('/countrylist', methods = ['GET'])
def get_countries():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT country from country_table')
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

#gets the decision stats from the model
@immigration_official.route('/testing/<year>/<coo>/<coa>/<applicationNum>', methods= ["GET"])
def get_decisionstats(year,coo,coa,applicationNum):
    returnArray = train_predict(year, coo, coa, applicationNum)
    returnval = returnArray[0]
    return_dict = {'result': returnval}
    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    
#gets the population
@immigration_official.route('/get_population')
def get_populationStats():
    cursor = db.get_db().cursor()
    query = 'SELECT Country, Population FROM populationStats'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response