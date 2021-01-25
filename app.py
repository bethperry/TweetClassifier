from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():
    
    about_text = """
    Fill in some info about the project here.
    """
    return about_text



if __name__=='__main__':

    app.run(debug=True)
 
