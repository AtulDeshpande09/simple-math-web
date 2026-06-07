from flask import Flask , request , render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


def linear_eq_in_2(x ,y , z):

    D = np.linalg.det(np.transpose(np.array([x,y])))
    Dx= np.linalg.det(np.transpose(np.array([z,y])))
    Dy= np.linalg.det(np.transpose(np.array([x,z])))

    try :
        a = round(Dx/D)
        b = round(Dy/D)
        return [a ,b]
    except ZeroDivisionError:
        print("Zero Division Error Occured!!!")
        return ["NA", "NA"]

def quadratic(a,b,c):
    try :
        x1 = (-b + (b**2-4*a*c)**(1/2))/(2*a)
        x2 = (-b - (b**2-4*a*c)**(1/2))/(2*a)

        return [x1 , x2]
    except ZeroDivisionError:
        print("Zero Division Error Occured!!!")
        return ["NA", "NA"]


@app.route("/lin" ,methods = ["POST" , "GET"])
def solve_lin():

    if request.method == 'POST':

        x1 = int(request.form['x1'])
        y1 = int(request.form['y1'])
        z1 = int(request.form['z1'])
 
        x2 = int(request.form['x2'])
        y2 = int(request.form['y2'])
        z2 = int(request.form['z2'])
        
        x = [x1 , x2]
        y = [y1 , y2]
        z = [z1 , z2]


        sol = linear_eq_in_2(x,y,z)
        print("sol" ,sol)
        return render_template("lin.html",sol=sol)

    return render_template("lin.html")


@app.route("/quad" ,methods = ["POST" , "GET"])
def solve_quad():

    if request.method == 'POST':

        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        
        sol = quadratic(a,b,c)

        print("Solution ",sol)
        return render_template("quad.html",sol=sol)

    return render_template("quad.html")



if __name__ == '__main__':
    app.run(debug=True)
    
