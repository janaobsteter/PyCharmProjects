from flask import Flask

#use Flask to define app
#creating Flask application

app = Flask(__name__) #__name__ esentially is a built in variable, private variable in python
#it contain '__main__' - if we are running application directly
#it is something that python determines for us - it determines whether we are running tha app directly (from terminal) or not

#create API endpoints
@app.route('/') #www.mysite.com/api/ - this is the end point

#define a method that will execute when we access the endpoint
def hello_method():
    return("Hello, world!") #when our browser reaches the site, this method runs

if __name__ == '__main__':
    app.run(port=5000) #if we are running the app and expect it to run from zero, this will run the app
    #if the app is running the app as the part of another process, this will not run the app and
    # will leave it to the other process to run the app
    #if your port 5000 is busy, just specify another port (e.g.4995)

#structure blogs, posts and users - these are the modules we need
#they are going to be based on database class