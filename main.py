import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        return render_template("Acknowledgement.html", name=filename)

if __name__ == '__main__':
    app.run(debug=True)