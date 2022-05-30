from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/mypage/me')
def about():
    return render_template("me_about.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("me_contact.html")
   elif request.method == 'POST':
       print("We received POST")
       message = request.form['message']
       print(f'Otrzymana wiadomość: {message}')
       return redirect("/mypage/contact")
    