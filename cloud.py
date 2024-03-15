from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return '21BCS8471'

if name == 'main':
    app.run(debug=True)
