from flask import Flask, render_template, redirect
from flask_nav import Nav
from flask_nav.elements import *

import generatePayDayWebpage

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#topbar = Navbar('Меню', View('Главная', 'hello'), View('Обеты', 'about'),  View('ЧАВО', 'faq'))
topbar = Navbar('Меню', View('Главная', 'hello'), View('Обеты', 'about'),  View('ЧАВО', 'faq'), View('Немного юмора и мудрости', 'mem'))

nav = Nav()
nav.register_element('left', topbar)
nav.init_app(app)



@app.errorhandler(404)
def page_not_found(error=None):
    return redirect(url_for('hello'))

@app.route('/about')
def about(name=None):
    return render_template('about.html', name=name)

@app.route('/')
def hello(name=None):
    generatePayDayWebpage.generatewebpage()
    return render_template('index.html', name=name)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/mem')
def mem():
    return render_template('memes.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    #app.run()
    app.run(host="0.0.0.0", port=443, ssl_context=('/etc/letsencrypt/live/uposatha.tk/fullchain.pem', '/etc/letsencrypt/live/uposatha.tk/privkey.pem'))



