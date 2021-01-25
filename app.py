from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():

    # if request has args (?tweet=some_tweet)
    if request.args:

        # get the value of the arg
        tweet = request.args.get('tweet')   
        
        return tweet

    return 'Hello World!'

@app.route('/about')
def about():
    
    about_text = """
    Fill in some info about the project here.
    """
    return about_text



if __name__=='__main__':

    app.run(debug=True)
 
