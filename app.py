from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    # Extracting form data
    fullname = request.form.get('fullname')
    address = request.form.get('address')
    birthdate = request.form.get('birthdate')
    job_title = request.form.get('job_title')
    employer = request.form.get('employer')
    salary = int(request.form.get('salary', 0))
    other_income = int(request.form.get('other_income', 0))
    existing_debts = int(request.form.get('existing_debts', 0))
    monthly_expenses = int(request.form.get('monthly_expenses', 0))
    race = request.form.get('race')
    gender = request.form.get('gender')
    credit_score = int(request.form.get('credit_score', 0))
    
    # Satirical/Discriminatory fields for 1920 context
    radio_ownership = request.form.get('radio_ownership')
    theatre_attendance = request.form.get('theatre_attendance')

    # Implement your loan calculation logic here based on the 1920 context
    # This is a placeholder for your loan calculation logic
    loan_amount, interest_rate, loan_denied, denial_reason = calculate_loan_conditions_1920(race, gender, credit_score)
    print(race, gender, credit_score)  # Add this in your calculate_loan() route.
    if loan_denied:
        return render_template('loan_denied.html', reason=denial_reason)
    else:
        return render_template('loan_details.html', loan_amount=loan_amount, interest_rate=interest_rate)


def calculate_loan_conditions_1920(race, gender, credit_score):
    # Placeholder for complex discrimination logic based on 1920 context
    loan_denied = race != "White" or gender != "Male"
    denial_reason = "Based on the discriminatory practices of the era, your application has been denied."
    loan_amount = 0 if loan_denied else 100000  # Example loan amount if not denied
    interest_rate = 0.05  # Example interest rate
    return loan_amount, interest_rate, loan_denied, denial_reason
@app.route('/')
@app.route('/index')
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

# You can add a new function specific to the 1930 context.
def calculate_loan_conditions_1930(race, gender, credit_score):
    # Include the specific logic for loan calculation based on the criteria for 1930
    loan_denied = race not in ["White", "Preferred Race"] or gender != "Male"
    denial_reason = "Based on the discriminatory practices of the 1930s, your application has been denied."
    loan_amount = 0 if loan_denied else 50000  # Example loan amount for 1930
    interest_rate = 0.10  # Example interest rate for 1930
    return loan_amount, interest_rate, loan_denied, denial_reason

# Now add the routes specific to the 1930 version
@app.route('/1930/')
def index_1930():
    return render_template('1930/index.html')

@app.route('/1930/about')
def about_1930():
    return render_template('1930/about.html')

@app.route('/1930/loan-application', methods=['GET', 'POST'])
def loan_application_1930():
    if request.method == 'POST':
        # Process the form data for the 1930 context
        return redirect(url_for('calculate_loan_1930'))
    return render_template('1930/loan_application.html')

@app.route('/1930/calculate_loan', methods=['POST'])
def calculate_loan_1930():
    # The form processing is specific to the 1930 context
    fullname = request.form.get('fullname')
    address = request.form.get('address')
    # ... and so on for the other form fields ...
    race = request.form.get('race')
    gender = request.form.get('gender')
    credit_score = int(request.form.get('credit_score', 0))
    
    loan_amount, interest_rate, loan_denied, denial_reason = calculate_loan_conditions_1930(race, gender, credit_score)
    
    if loan_denied:
        return render_template('1930/loan_denied.html', reason=denial_reason)
    else:
        return render_template('1930/loan_details.html', loan_amount=loan_amount, interest_rate=interest_rate)


if __name__ == '__main__':
    app.run(debug=True)
