from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html',my_args='Banana!') #return the html file under templates foldertemplate('index.html')

@app.route('/about')
def about():
    
    about_text = """
    Fill in some info about the project here.
    """
    return about_text



if __name__=='__main__':

    app.run(debug=True)
 
