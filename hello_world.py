from flask import Flask, render_template
import datetime
from os import environ

app = Flask(__name__)

@app.route("/")
def say_hi():
    return render_template('template.html', my_string="Hello World!",
                          current_time=datetime.datetime.now())
    
@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template2.html', my_string=name.title(),
                          current_time=datetime.datetime.now())
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
    return render_template('template3.html', last=lastname[0:3].title(), first=firstname[0:2])
    
@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(format)
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))

        