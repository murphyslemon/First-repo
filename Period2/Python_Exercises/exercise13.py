# Problem 1
from flask import Flask, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route('/prime_number')
def prime_number():
    args = request.args
    number = int(args.get("number"))
    half = number // 2
    if number > 2:
        for i in range(2, half + 1):
            if (number % i) == 0:
                answer = 'a composite number'
                break
        else:
            answer = 'a prime number'
    else:
        answer = 'neither prime nor composite'

    response = {
        "number": number,
        "is": answer
    }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
