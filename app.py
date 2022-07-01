from flask import Flask, jsonify, request

app = Flask(__name__)
List = [
    {
        'id': 1,
        'Language': u'Javascript',
        'Purpose': u'It is used for making apps and games.',
        'Rank': 1,
        'done': False
    },
    {
        'id': 2,
        'Language': u'Python',
        'Purpose': u'It is used for backend purposes.',
        'Rank': 2,
        'done': False
    },
    {
        'id': 3,
        'Language': u'Java',
        'Purpose': u'It is used because it is platform-independent.',
        'Rank': 3,
        'done': False
    },
    {
        'id': 4,
        'Language': u'C+',
        'Purpose': u'It is used as it helps in optimizing the resources.',
        'Rank': 4,
        'done': False
    },
    {
        'id': 5,
        'Language': u'PHP',
        'Purpose': u'It is used to develop dynamic and interactive websites.',
        'Rank': 5,
        'done': False
    }
]

@app.route("/")
def main_window():
    return (
        "Hello World!"
        "                "
        "Type 'get' in front of url to see the data."
    )

@app.route("/add", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please provide the data!"
        },400)

    new_data = {
        'id': List[-1]['id'] + 1,
        'Language': request.json['Language'],
        'Purpose': request.json.get('Purpose', ""),
        'Rank': request.json['Rank'],
        'done': False
    }
    List.append(new_data)
    return jsonify({
        "status": "Success",
        "message": "Data added succesfully!"
    })
    

@app.route("/get")
def get_task():
    return jsonify({
        "Data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)