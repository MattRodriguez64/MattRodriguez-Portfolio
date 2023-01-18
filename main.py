#!/usr/bin/env python
from flask import Flask, render_template
from json import loads

app = Flask(__name__)

@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/about", methods=['GET'])
def about():
    with open ('./data/personal_data.json', 'r') as tempData:
        tempPersonalData = tempData.read()

    personal_data = loads(tempPersonalData)

    with open ('./data/skills_data.json', 'r') as tempData:
        tempSkillsData = tempData.read()

    skills_data = loads(tempSkillsData)

    with open ('./data/degree_data.json', 'r') as tempData:
        tempDegreeData = tempData.read()

    degree_data = loads(tempDegreeData)

    return render_template('about.html', personal_data=personal_data, skills_data=skills_data, degree_data=degree_data)

@app.route("/services", methods=['GET'])
def services():
    return render_template('services.html')

@app.route("/portfolio", methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route("/blog", methods=['GET'])
def blog():
    return render_template('blog.html')

@app.route("/contact", methods=['GET'])
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def err_not_found(e):
    return render_template('error_404.html')


if __name__ == "__main__":
    app.run(debug=True)