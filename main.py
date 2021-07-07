
# Video test implement flask ajax to display result
from flask import Flask, render_template, request, jsonify
from flask.scaffold import F
import wolframalpha

client = wolframalpha.Client('JPY49W-5R97J6XYAX')
app = Flask(__name__)
global past_ans  # List of the past answers
past_ans = [["Question", "Answer"]]


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route('/result', methods=["POST"])  # Happens when the form submits.
def wolframRequest():
    # Gets the question from the input box.
    question = request.form["question"]
    res = client.query(question)  # Queries the api for the answer
    ans = next(res.results).text  # Gets the answer from the XML.
    # If the answer exists, return the q/a pair, else return error.
    if ans != None:
        past_ans.insert(1,  (question, ans))
        return render_template('qresult.html')
    return jsonify({'error': 'Missing answer'})


@app.route('/questionBot', methods=["GET"])
def loadQuestionBot():
    return render_template('questionBot.html')


@app.route('/result', methods=['GET'])
def pastAnsReq():
    return jsonify(past_ans)


@app.route('/index', methods=['GET'])
def loadHomePage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
