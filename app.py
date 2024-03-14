from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    # Extract form data
    race = request.form.get('race')
    area = request.form.get('area')
    credit_score = int(request.form.get('credit_score', 0))
    
    # Implement your loan calculation logic here
    interest_rate = 0.05  # Default interest rate
    if race == "race1" and area == "area1":
        interest_rate += 0.02  # Example adjustment based on race and area
    
    # Define loan_amount and loan_denied based on your logic
    loan_amount = 100000  # Example value
    loan_denied = False   # Example value

    # Render a template with the results or redirect as appropriate
    return render_template('results.html', interest_rate=interest_rate, loan_amount=loan_amount, loan_denied=loan_denied)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loan-application', methods=['GET', 'POST'])
def loan_application():
    if request.method == 'POST':
        # Process the form data
        return redirect(url_for('calculate_loan'))
    return render_template('loan_application.html')


@app.route('/map_view')
def map_view():
    return render_template('map_view.html')

@app.route('/results')
def results():
    # This route could handle displaying results after form submission
    # For now, it's set up to simply render a template
    return render_template('results.html')
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


if __name__ == '__main__':
    app.run(debug=True)
