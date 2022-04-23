from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/customer_insert', methods = ['GET','POST'])
def customer_insert():
    
    return render_template('customer_insert.html')

@app.route('/customer_update', methods = ['GET','POST'])
def customer_update():
    return render_template('customer_update.html')

@app.route('/customer_delete', methods = ['GET','POST'])
def customer_delete():
    if request.method == 'POST':
        state_name = request.form['state_name']
        print("Delete record for : " ,state_name)
    return render_template('customer_delete.html')

@app.route('/customer_view', methods = ['GET','POST'])
def customer_view():
    return render_template('customer_view.html')

@app.route('/customer_search', methods = ['GET','POST'])
def customer_search():
    if request.method == 'POST':
        state_name = request.form['state_name']
        print("Search customers in : " ,state_name)
    return render_template('customer_search.html')

@app.route('/customer_success', methods = ['GET','POST'])
def customer_success():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        phone_number = request.form['phone_number']
        state_name = request.form['state']
        print("customer_name is: " ,customer_name , "phone_number is : " ,phone_number, "state is : " ,state_name)
        return render_template('customer_success.html')

# @app.route('/static/style', methods = ['GET','POST'])
# def style():
#     return render_template('style.css')