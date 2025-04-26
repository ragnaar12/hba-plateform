from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Exemple de liste des projets
projects = [] 

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        projects.append({'title': title, 'description': description})
        return redirect('/')
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

