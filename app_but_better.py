from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
a=0
class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(40), nullable=False, default="Аноним")
    colour = db.Column(db.String(30), nullable=False, default="white")

    def __repr__(self):

        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']

        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)


    else:

        tasks = Todo.query.order_by(Todo.date_created).all()

        return render_template('index.html', tasks=tasks)




@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404()

    if request.method == 'POST':
        task.colour = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:

        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port="8888")
