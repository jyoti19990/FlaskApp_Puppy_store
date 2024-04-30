from flask import Flask, render_template
from main_project.myproject import app
@app.route('/')
def index():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

