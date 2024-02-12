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
    # Récupérer les données sur les commits depuis l'API GitHub
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'
    response = requests.get(url)
    commits_data = response.json()
    
    # Compter le nombre de commits par minute
    commits_per_minute = {}
    for commit in commits_data:
        commit_date = commit['commit']['author']['date']
        minute = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ').minute
        if minute in commits_per_minute:
            commits_per_minute[minute] += 1
        else:
            commits_per_minute[minute] = 1
    
    # Convertir les données en format adapté pour Google Charts
    data_for_chart = [['Minute', 'Nombre de Commits']]
    for minute, count in commits_per_minute.items():
        data_for_chart.append([minute, count])
    
  
                                       
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
