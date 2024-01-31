
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_wallet.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

class ScreenTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    total_time = db.Column(db.Integer, nullable=False)
    apps = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@app.route('/add_resource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        resource = Resource(name=name, amount=amount)
        db.session.add(resource)
        db.session.commit()
        flash('Resource added successfully.')
        return redirect(url_for('resources'))
    return render_template('add_resource.html')

@app.route('/edit_resource/<int:id>', methods=['GET', 'POST'])
def edit_resource(id):
    resource = Resource.query.get_or_404(id)
    if request.method == 'POST':
        resource.name = request.form['name']
        resource.amount = request.form['amount']
        db.session.commit()
        flash('Resource updated successfully.')
        return redirect(url_for('resources'))
    return render_template('edit_resource.html', resource=resource)

@app.route('/delete_resource/<int:id>')
def delete_resource(id):
    resource = Resource.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    flash('Resource deleted successfully.')
    return redirect(url_for('resources'))

@app.route('/expenses')
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        date = request.form['date']
        expense = Expense(category=category, amount=amount, date=date)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully.')
        return redirect(url_for('expenses'))
    return render_template('add_expense.html')

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.category = request.form['category']
        expense.amount = request.form['amount']
        expense.date = request.form['date']
        db.session.commit()
        flash('Expense updated successfully.')
        return redirect(url_for('expenses'))
    return render_template('edit_expense.html', expense=expense)

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully.')
    return redirect(url_for('expenses'))

@app.route('/screen_time')
def screen_time():
    screen_time = ScreenTime.query.all()
    return render_template('screen_time.html', screen_time=screen_time)

@app.route('/add_screen_time', methods=['GET', 'POST'])
def add_screen_time():
    if request.method == 'POST':
        date = request.form['date']
        total_time = request.form['total_time']
        apps = request.form['apps']
        screen_time = ScreenTime(date=date, total_time=total_time, apps=apps)
        db.session.add(screen_time)
        db.session.commit()
        flash('Screen time added successfully.')
        return redirect(url_for('screen_time'))
    return render_template('add_screen_time.html')

@app.route('/edit_screen_time/<int:id>', methods=['GET', 'POST'])
def edit_screen_time(id):
    screen_time = ScreenTime.query.get_or_404(id)
    if request.method == 'POST':
        screen_time.date = request.form['date']
        screen_time.total_time = request.form['total_time']
        screen_time.apps = request.form['apps']
        db.session.commit()
        flash('Screen time updated successfully.')
        return redirect(url_for('screen_time'))
    return render_template('edit_screen_time.html', screen_time=screen_time)

@app.route('/delete_screen_time/<int:id>')
def delete_screen_time(id):
    screen_time = ScreenTime.query.get_or_404(id)
    db.session.delete(screen_time)
    db.session.commit()
    flash('Screen time deleted successfully.')
    return redirect(url_for('screen_time'))

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
