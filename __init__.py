from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)    

                                                                                                
@app.route('/')
def hello_world():
    return render_template('hello.html')   #com2
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def mongraphique2():
    return render_template("graphique2.html")

@app.route('/commits/')
def count_commits():
    url = 'https://api.github.com/repos/Nanaaicha23/5MCSI_Metriques/commits'
    response = requests.get(url)
    commits_data = response.json()

    commits_per_minute = {}
    for commit in commits_data:
        date = commit['commit']['author']['date']
        minute = date.split(':')[1]  # Extraire la minute de l'heure
        commits_per_minute[minute] = commits_per_minute.get(minute, 0) + 1

    return jsonify(commits_per_minute)

if __name__ == '__main__':
    app.run(debug=True)


   
      
                                       
@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
   
if __name__ == "__main__":
  app.run(debug=True)
