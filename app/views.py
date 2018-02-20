from flask import render_template
from app import app
import sysinfo
@app.route('/')
def index():
 returnDict = {}
 returnDict['user'] = sysinfo.getplatforminfo()  #Linda Smith
 returnDict['title'] = 'Home'
 returnDict['name'] = 'Linda Smith'
 return render_template("index.html", **returnDict
)
