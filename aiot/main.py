from flask import Flask, render_template, request
# from flask_cors import CORS
# from flask_socketio import SocketIO
# from flask_cors import cross_origin


app = Flask(__name__)
# CORS(app)


@app.route('/', methods = ['GET'])
# @cross_origin()
def monitor():

    return render_template('main.html', **locals())

@app.route('/results', methods = ['POST', 'GET'])
def trace():
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        print(start_date)
        print(end_date)
    return render_template('results.html', **locals())

if __name__ == '__main__' :
    app.run(debug = True)
