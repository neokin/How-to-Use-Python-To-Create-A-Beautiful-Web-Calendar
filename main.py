from flask import Flask, render_template, redirect
from flask_nav import Nav
from flask_nav.elements import *

import generatePayDayWebpage

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

topbar = Navbar('Меню', View('Главная', 'hello'), View('Обеты', 'about'),)
nav = Nav()
nav.register_element('left', topbar)
nav.init_app(app)



@app.errorhandler(404)
def page_not_found(error=None):
    print("404 WASROUT")
    return redirect(url_for('hello'))

@app.route('/about')
def about(name=None):
    print("WASROUT")
#    generatePayDayWebpage.generatewebpage()
    return render_template('about.html', name=name)

@app.route('/')
def hello(name=None):
    print("WASROUT")
    generatePayDayWebpage.generatewebpage()
    return render_template('index.html', name=name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #app.run()



