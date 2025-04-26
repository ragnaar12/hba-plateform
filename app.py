from flask import Flask, render_template

app = Flask(__name__)

# Exemple de projets
projects = [
    {"title": "Plateforme IA", "description": "Projet d'intelligence artificielle avancée."},
    {"title": "Application Mobile", "description": "Développement d'une application pour étudiants."},
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/add')
def add_project():
    return "<h2>Page pour ajouter un projet (à faire)</h2>"

if __name__ == "__main__":
    app.run(debug=True)

