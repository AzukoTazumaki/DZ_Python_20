from flask import Flask, request, render_template
from exercises import Exercises
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
ex = Exercises()


@app.route('/', methods=['GET', 'POST'])
def index():
    result_ex_1 = ex.ex_1()
    result_ex_2 = ex.ex_2()
    result_ex_3 = ex.ex_3()
    if request.method == 'POST':
        return render_template('main/exercises_answer.html',
                               result_ex_1=result_ex_1,
                               result_ex_2=result_ex_2,
                               result_ex_3=result_ex_3)
    return render_template('main/exercises_content.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template('errors/bad_request.html'), 400


if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
