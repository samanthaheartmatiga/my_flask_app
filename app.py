from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def work():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def calculate_circle_area():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', ''))
            area = 3.14159 * radius * radius  # Calculate the area of the circle
            result = f"The area of the circle with a radius of {radius} is {area:.2f} square units."
        except ValueError:
            result = "Invalid input. Please enter a valid number for the radius."
    return render_template('circle.html', result=result)

@app.route('/triangle', methods=['GET', 'POST'])
def calculate_triangle_area():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', ''))
            height = float(request.form.get('height', ''))
            area = 0.5 * base * height  # Calculate the area of the triangle
            result = f"The area of the triangle with a base of {base} and height of {height} is {area:.2f} square units."
        except ValueError:
            result = "Invalid input. Please enter valid numbers for the base and height."
    return render_template('triangle.html', result=result)

@app.route('/contact')
def contact_page():
    return render_template('contacts.html', contact=contact_page)

@app.route('/gmail')
def redirect_to_gmail():
    gmail_url = 'mailto:matigasamanthaheart@gmail.com'
    return redirect(gmail_url)

@app.route('/facebook')
def redirect_to_facebook():
    facebook_url = 'https://www.facebook.com/antHARTT'
    return redirect(facebook_url)

@app.route('/instagram')
def redirect_to_instagram():
    instagram_url = 'https://instagram.com/smnthrt'
    return redirect(instagram_url)

@app.route('/twitter')
def redirect_to_twitter():
    twitter_url = 'https://x.com/loveykumee'
    return redirect(twitter_url)

@app.route('/tiktok')
def redirect_to_tiktok():
    tiktok_url = 'https://www.tiktok.com/@sunsunkies_'
    return redirect(tiktok_url)

if __name__ == "__main__":
    app.run(debug=True)