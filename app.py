from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# Charger les projets depuis un fichier JSON
def load_projects():
    if os.path.exists('projets.json'):
        with open('projets.json', 'r') as f:
            return json.load(f)
    return []

# Sauvegarder les projets
def save_project(project):
    projects = load_projects()
    projects.append(project)
    with open('projets.json', 'w') as f:
        json.dump(projects, f, indent=4)

@app.route('/')
def index():
    projects = load_projects()
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        project = {
            'title': request.form['title'],
            'description': request.form['description']
        }
        save_project(project)
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
