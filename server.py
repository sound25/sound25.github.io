from flask import Flask, render_template,request, redirect
import csv
app=Flask(__name__)
@app.route('/<pagename>')
def page(pagename):
	return render_template(pagename)
@app.route('/')
def index():
	return render_template('index.html')
def write_csv(data):
	with open('database.csv',newline='',mode='a') as datab:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csvwriter=csv.writer(datab,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow([email,subject,message])
@app.route('/submit', methods=['POST','GET'])
def submitt():
	if request.method=='POST':
		data=request.form.to_dict()
		print(data)
		write_csv(data)
		return redirect('thankyou.html')
	else:
		return "Failed to submit the contact form"

