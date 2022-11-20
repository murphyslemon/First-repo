# Problem 1
from flask import Flask, request, Response
import json
import mysql.connector

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
#
#
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
        sql = "SELECT name, municipality from airport where ident = '" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        response = {
            "ICAO": icao,
            "Name:": result[0][0],
            "Location": result[0][1]
        }
        return response

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
