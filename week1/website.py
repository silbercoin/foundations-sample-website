from flask import Flask
from flask import render_template, url_for,request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('base.html',page_title="Foundation Class")


@app.route('/first-page')
def first_page():
    return render_template('first-page.html', page_title="First Template")


@app.route('/second-page')
def second_page():
    return render_template('second-page.html', page_title="Second Template")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
