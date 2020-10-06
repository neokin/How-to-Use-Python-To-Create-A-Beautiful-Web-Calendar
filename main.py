import generatePayDayWebpage
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error=None):
    print("404 WASROUT")
    return redirect(url_for('hello'))


@app.route('/')
def hello(name=None):
    print("WASROUT")
    generatePayDayWebpage.generatewebpage()
    return render_template('index.html', name=name)



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run()



