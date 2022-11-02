from flask import Flask, render_template, request

# html is all configured in the video and explained there

app = Flask(__name__)

# if they go to "/", they get served the home app, which should return the html in this case
@app.route("/")
def home():
    print("Get request string")
    # render expects a "template" folder, wont work otherwise
    return render_template("index.html")


# Set up the homepage to process post requests
# HTTP requests have lots of different types, eg get,post,put,connect etc
# get requests request data from a source
# post requests are when we send data to the server
# So in this case python is the server, so when we load the url, we're doing a get request
# When we enter data into configurable boxes, we're giving it data and so is a post request
@app.route("/", methods=["POST"])
def home_post():
    print("Get post request string")
    #print(request.form) # This stores inputs from the web app, corresponding to form in the html
    dim1 = request.form['first_dim']
    dim2 = request.form['second_dim']
    dim3 = request.form['third_dim']
    volume = float(dim1) + float(dim2) + float(dim3)
    # output we want to go into the <p> tags on html, where {output} is on html
    # utilise input and value{{}} tags here, with whats being put into dim_1 being sent to it - same for other dim_*
    return render_template("index.html", output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)


# to get the CSS you just google for desirable CSS and paste it in, CSS just enhances html to look more modern


#app.run()
app.run(host="0.0.0.0")


