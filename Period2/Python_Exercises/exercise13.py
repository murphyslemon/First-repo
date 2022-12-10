from flask import Flask, request, Response
import json
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["JSON_SORT_KEYS"] = False
#
# Problem 1
# @app.route('/prime_number')
# def prime_number():
#     try:
#         args = request.args
#         number = int(args.get("number"))
#         half = number // 2
#         if number > 2:
#             for i in range(2, half + 1):
#                 if (number % i) == 0:
#                     answer = 'a composite number'
#                     break
#             else:
#                 answer = 'a prime number'
#         else:
#             answer = 'neither prime nor composite'
#         response = {
#             "number": number,
#             "is": answer
#         }
#         return response
#
#     except ValueError:
#         response = {
#             "message": "Invalid number as addend",
#             "status": 400
#         }
#         json_response = json.dumps(response)
#         http_response = Response(response=json_response, status=400, mimetype="application/json")
#         return http_response
#
#
# @app.errorhandler(404)
# def page_not_found(error_code):
#     response = {
#         "message": "Invalid endpoint",
#         "status": 404
#     }
#     json_response = json.dumps(response)
#     http_response = Response(response=json_response, status=404, mimetype="application/json")
#     return http_response
#
#
# if __name__ == '__main__':
#     app.run(use_reloader=True, host='127.0.0.1', port=5000)

# Problem 2
connection = mysql.connector.connect(
  host='127.0.0.1',
  port=3306,
  database='flight_game',
  user='root',
  password='root'
)


@app.route('/airport/<string:icao>')
def get_airport_info(icao):
    airport_info = get_airport(icao)
    return json.dumps(airport_info)


def get_airport(icao):
    try:
        sql = "SELECT name, municipality, iso_country from airport where ident = '" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        response = {
            "ICAO": icao,
            "Name:": result[0][0],
            "Location": result[0][1]
        }
        return {'ICAO': icao, 'Name': result[0][0], 'Location': result[0][1], 'Iso_country': result[0][2]}

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
