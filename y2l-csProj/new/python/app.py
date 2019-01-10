# Flask-related imports
# Add functions you need from databases.py to the next line!
from databases import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
# from flask.ext.session import Session
from forgotpass import send_mail
# Starting the flask app

app = Flask(__name__)
app.secret_key = "VERY SECRET." 

############################################ HOME ############################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/<string:if_post>' ,methods= ['GET','POST'])
def home(if_post="false"):
    if('username' in login_session):
        log = "true"
    else:
        log = "false"

    if request.method == 'GET':
        if if_post == "true":
            return render_template('home.html', if_post = "true",log=log)
        else:
            return render_template('home.html', if_post = "false", log=log)
    else:
        return redirect(url_for('display_result'))

############################################ SIGN-UP ##########################################

@app.route('/signup.html',methods= ['GET','POST'])
def SignUp ():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        try:
            name = request.form['name']
            lastName = request.form['familyName']
            user = request.form['user']
            password = request.form['password']
            mail = request.form['mail']
            loc = request.form['loc']
        except:
            return render_template("signup.html", error="u r bad")
        add_student(user,password,mail,name,lastName,loc)
        return redirect(url_for('home'))


############################################ LOGIN ############################################

@app.route('/login.html',methods= ['GET','POST'])
def Login():
    log = 0
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    print(log)
    if request.method == 'GET':
        return render_template('login.html',log=log)
    else:
        user = request.form['username']
        password = request.form['password']
        if check_account(user,password):
            login_session['logged_in'] = True
            login_session['username'] = request.form['username']

            # return redirect(url_for('show_prof',username=user))
            return redirect(url_for('home',log=log))

        else:
            return render_template('login.html', error = "username or password are not correct!")

@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))
############################################ CATEGORIES #######################################

@app.route('/categories.html')
def Show():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('Categories.html',log=log)
    pass

############################################ REQUEST ############################################

@app.route('/request.html',methods= ['GET','POST'])
def Add():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if login_session.get("username") == None:
        return redirect(url_for("Login"))
    if request.method == 'GET':
        return render_template('post_request.html',log=log)
    else:
        cat = request.form['cat'].strip()
        text = request.form['text'].strip()
        add_post(cat,text)
        return redirect(url_for("home",if_post="true"))


############################################ PROFILE ############################################

@app.route('/<string:username>/profile.html')
def show_prof(username):
    # user = query_by_username(login_session['username'])
    user = query_by_username(username)
    return render_template('profile.html',user=user)

############################################ HOME ############################################

@app.route('/forgotpass',methods= ['GET','POST'])
def frgt_pwd():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'GET':
        return render_template('forgotpwd.html',log=log)
    else:
        email = request.form['email']
        if if_account_exist(email):
            send_mail(email)
            return redirect(url_for("home",log=log))
        else:
            return render_template('forgotpwd.html',log=log)

@app.route('/searchResult',methods= ['GET','POST'])
def display_result():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'POST':
        result = request.form['data']        
        matches = search(result)
        if len(matches) == 0:

            flash('No matching results for: '+result)
            return redirect(url_for('home'))
            return render_template('searchResult.html',matches=matches,log=log)
        else:
            no_matches = False
        return render_template('searchResult.html',matches=matches, no_matches=no_matches,log=log)
    else:
        return redirect(url_for('home'))

##############################################################################################
@app.route('/jobs')
def jobs_page():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('Jobs.html',jobs_posts=query_by_cat('jobs'),log=log)

##########################################################################################
@app.route('/sales')
def sales_page():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('Sales.html',sales_posts=query_by_cat('sales'),log=log)

##########################################################################################
@app.route('/lostandfound')
def lost_and_found_page():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('lost_and_found.html',lost_posts=query_by_cat('l&f'),log=log)

##########################################################################################
@app.route('/news')
def news_page():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('news.html',news_posts=query_by_cat('news'),log=log)

##########################################################################################
@app.route('/others')
def others_page():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('others.html',others_posts=query_by_cat('others'),log=log)
##########################################################################################
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

##############################################################################################


