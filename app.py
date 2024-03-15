from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Assuming 'calculate_loan_conditions_1930' is a function that contains the loan calculation logic for 1930.
# This should be defined elsewhere in your code and imported or included in this file.

@app.route('/1930/')
def index_1930():
    # Render the main page for the 1930 version of the app
    return render_template('1930/index.html')

@app.route('/1930/about')
def about_1930():
    # Render the about page for the 1930 version of the app
    return render_template('1930/about.html')

@app.route('/1930/loan-application', methods=['GET', 'POST'])
def loan_application_1930():
    if request.method == 'POST':
        # Process the form data and redirect to the loan calculation results
        return redirect(url_for('calculate_loan_1930'))
    # Render the loan application form
    return render_template('1930/loan_application.html')

@app.route('/1930/calculate_loan', methods=['POST'])
def calculate_loan_1930():
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
    loan_amount, interest_rate, loan_denied, denial_reason = calculate_loan_conditions_1930(race, gender, credit_score)
    print(race, gender, credit_score)  # Add this in your calculate_loan() route.
    if loan_denied:
        return render_template('loan_denied.html', reason=denial_reason)
    else:
        return render_template('loan_details.html', loan_amount=loan_amount, interest_rate=interest_rate)

# Define the 'calculate_loan_conditions_1930' function with your business logic
def calculate_loan_conditions_1930(race, gender, credit_score):
    # Here, include the specific logic for loan calculation based on the criteria for 1930
    # This is a placeholder; you'll need to replace it with the actual calculation logic
    loan_denied = race != "White" or gender != "Male"  # Example based on historical context
    denial_reason = "Based on the discriminatory practices of the era, your application has been denied."
    loan_amount = 0 if loan_denied else 100000  # Example loan amount if not denied
    interest_rate = 0.05  # Example interest rate
    return loan_amount, interest_rate, loan_denied, denial_reason

# More routes for the 1930 app...

if __name__ == '__main__':
    # Don't use app.run() since you are running the app with gunicorn
    pass
