from flask import Flask, render_template,request, redirect, url_for
app=Flask(__name__)
ledger=[]
@app.route('/')
def main_page():
    #return "Hello World!"
    return render_template('main.html')
@app.route('/aboutme')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/ledger_add', methods=['GET', 'POST'])
def ledger_add():
    if request.method == 'POST':
        trip = {
            'place': request.form['place'],
            'trip_start_date': request.form['trip_start_date'],
            'trip_end_date': request.form['trip_end_date'],
            'places_visited': request.form['places_visited'],
            'total_cost': request.form['total_cost'],
            'opinion': request.form['opinion']
        }
        ledger.append(trip)  # Append to the "ledger" list
        # Redirect to ledger_view route after adding trip
        #return redirect(url_for('ledger_view'))
    return render_template('ledger_add.html')



@app.route('/ledger_view')
def ledger_view():
    return render_template('ledger_view.html', trips=ledger)  # Pass trips stored in the ledger list to the template
if __name__=="__main__":
    app.run(debug=True,port=7000)