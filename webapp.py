from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    era = request.args['era']
    genre = request.args['genre'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if era == '2010':
        reply = "That era brings me good memories! I listened to pop, specifically Ariana Grande."
        if genre == 'pop':
        		reply = "I appreciate Ariana Grande's Yours Truly Album"
    else:
        	reply = "My favorite era is 2010 and genre is pop. I really like Ariana Grande's Yours Truly Album."
        	
        	
    return render_template('response.html', response = reply)
    
@app.route("/responsetwo")
def render_responsetwo():
    yes = request.args['yes'] 
    
    if yes == 'yes':
    	reply = "Okay! here's a link to her Spotify profile https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR?si=j9UrN3yoTkmXHzWRV_sDDw"
    else:
    	reply = "That's okay! You can listen to her on your own time!"
    
    return render_template('responsetwo.html', response = reply)
if __name__=="__main__":
    app.run(debug=True, port=54321)
