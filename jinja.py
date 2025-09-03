from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

## Variable rule

'''@jinja.route('/success/<score>')
def success(score):
    return f'Your score is:'+score'''

# “This is a variable rule, where I specify that the parameter must be an int.
#  The + str() is added because otherwise it will throw an error.”

###Example:
# Visiting /success/75 → score = 75
# Visiting /success/abc → ❌ Error (because abc is not an integer)

'''@app.route('/success/<int:score>')
def success(score):
    return f'Your score is:' +str(score)'''

#http://127.0.0.1:5000/success/75-->passed

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"

    return render_template('results.html', results=res)


'''@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')'''

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}

    return render_template('results1.html',results=exp)

## if confition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('results.html',results=score)                                                                                                 

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))
            
        



if __name__=="__main__":
    app.run(debug=True)