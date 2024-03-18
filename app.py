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
    credit_score = request.form.get('credit_category')  # This replaces credit_score
    
    total_income = salary + (other_income * 12)  # Assuming other income is monthly

    
    # Satirical/Discriminatory fields for 1920 context
    radio_ownership = request.form.get('radio_ownership')
    theatre_attendance = request.form.get('theatre_attendance')

    # Implement your loan calculation logic here based on the 1920 context
    # This is a placeholder for your loan calculation logic
    loan_amount, interest_rate, loan_denied, denial_reason = calculate_loan_conditions_1920(
        race, gender, job_title, total_income, address, credit_score)  # Add this in your calculate_loan() route.
    if loan_denied: 
        return render_template('loan_denied.html', reason=denial_reason)
    else:
        return render_template('loan_details.html', loan_amount=loan_amount, interest_rate=interest_rate)


def calculate_loan_conditions_1920(race, gender, job_title, total_income, address, credit_score):
    # Simulated logic for discrimination based on multiple factors in 1920
    
    # Assuming job_title categories are 'Professional', 'Industrial', etc.
    
    # Assuming address categories could be inferred as 'Urban', 'Rural', etc.
    location_risk = 'Rural' in address or 'Redlined District' in address
    
    # Discrimination logic
    loan_denied = False
    denial_reasons = []
    
    if race != "White":
        denial_reasons.append("Race")
    if gender != "Male":
        denial_reasons.append("Gender")
    if total_income < 5000:  # Assuming $5,000 is a significant income threshold in 1920
        denial_reasons.append("Income Level")
    if location_risk:
        denial_reasons.append("Geographical Location")
    
    loan_denied = len(denial_reasons) > 0
    
    denial_reason = "Based on the discriminatory practices of the era and your {} status, your application has been denied.".format(", ".join(denial_reasons)) if loan_denied else ""
    
    loan_amount = 0 if loan_denied else 100000  # Example loan amount if not denied
    interest_rate = 0.07 if gender != "Male" else 0.05  # Adjusting interest rate for gender
    
    return loan_amount, interest_rate, loan_denied, denial_reason

def calculate_loan_amount(salary, other_income, monthly_expenses, credit_score):
    # Example calculation based on financial information and credit score
    # You can adjust the logic to better fit the loan amount calculation criteria
    return (salary + other_income * 12) - monthly_expenses * 12

def calculate_interest_rate(credit_score):
    # Example interest rate determination based on credit score
    if credit_score >= 740:
        return 0.05
    elif credit_score >= 680:
        return 0.06
    elif credit_score >= 620:
        return 0.07
    else:
        return 0.08
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

# You can add a new function specific to the 2008 context.
def calculate_loan_conditions_2008(fullname, address, birthdate, job_title, employer, 
                                   salary, other_income, existing_debts, monthly_expenses, 
                                   race, gender, credit_category):
    # Simulated logic for discrimination in 2008
    
    # Potential factors that could indirectly reflect discriminatory practices
    # or systemic biases. These should not explicitly include race or gender.
    high_risk_job = job_title in ['Construction Worker', 'Factory Worker', 'Retail']
    unstable_employment = employer in ['Lehman Brothers', 'Blockbuster', 'Circuit City']
    high_debt_to_income_ratio = (existing_debts / max((salary + other_income), 1)) > 0.4
    poor_credit_category = credit_category == 'Low'
    
    # The denial of the loan should not explicitly mention race or gender.
    loan_denied = False
    denial_reasons = []
    
    if high_risk_job or unstable_employment:
        denial_reasons.append("Employment Risk Factors")
    if high_debt_to_income_ratio:
        denial_reasons.append("Debt-to-Income Ratio")
    if poor_credit_category:
        denial_reasons.append("Credit Category")
    
    loan_denied = len(denial_reasons) > 0
    
    denial_reason = "Based on an assessment of multiple risk factors, your application has been denied." if loan_denied else ""
    
    loan_amount = 0 if loan_denied else calculate_loan_amount(salary, other_income, monthly_expenses)
    interest_rate = calculate_interest_rate(credit_category, denial_reasons)

    return loan_amount, interest_rate, loan_denied, denial_reason


# Now add the routes specific to the 2008 version
@app.route('/2008/')
def index_2008():
    return render_template('2008/index.html')
@app.route('/2008/map_view')
def map_view_2008():
    return render_template('2008/map_view.html')

@app.route('/2008/about')
def about_2008():
    return render_template('2008/about.html')
@app.route('/2008/testimonials')
def testimonials_2008():
    return render_template('2008/testimonials.html')

@app.route('/2008/loan-application', methods=['GET', 'POST'])
def loan_application_2008():
    if request.method == 'POST':
        # Process the form data for the 2008 context
        return redirect(url_for('calculate_loan_2008'))
    return render_template('2008/loan_application.html')

@app.route('/2008/calculate_loan', methods=['POST'])
def calculate_loan_2008():
    # Extract form data specific to the 2008 context
    fullname = request.form.get('fullname')
    address = request.form.get('address')
    birthdate = request.form.get('birthdate')
    job_title = request.form.get('job_title')
    employer = request.form.get('employer')
    salary = int(request.form.get('salary', 0))
    other_income = int(request.form.get('other_income', 0)) * 12  # Assuming this is monthly other income
    existing_debts = int(request.form.get('existing_debts', 0))
    monthly_expenses = int(request.form.get('monthly_expenses', 0))
    credit_score = int(request.form.get('credit_score', 0))
    
    loan_amount, interest_rate, loan_denied, denial_reason = calculate_loan_conditions_2008(
        fullname, address, birthdate, job_title, employer, salary, other_income,
        existing_debts, monthly_expenses, credit_score)
    
    if loan_denied:
        return render_template('2008/loan_denied.html', reason=denial_reason)
    else:
        return render_template('2008/loan_details.html', loan_amount=loan_amount, interest_rate=interest_rate)


if __name__ == '__main__':
    app.run(debug=True)
