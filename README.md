
tutorial link
https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/
---
Chatgpt link
https://chat.openai.com/share/deec3a19-b710-4968-a0c4-352258f86a04

Rewrite the following python flask code to save in uploaded file to uploads folder 
@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		return render_template("Acknowledgement.html", name = f.filename)"# flask_practice" 
"# flask_practice" 
