from flask import Flask,request,jsonify

app=Flask(__name__)

#root route
@app.route('/')

def home():
    return jsonify(page="Home",message="You are viewing root route")

#POST & GET    
@app.route('/flaask',methods=["POST","GET","PUT","PATCH","DELETE"])

def flaask():
    if request.method=="POST":
        return jsonify(request="POST",message="You are viewing flaask route")
    elif request.method=="GET":
        return jsonify(request="GET",message="You are viewing flaask route")    
    elif request.method=="PUT":
        return jsonify(request="PUT",message="You are viewing flaask route")
    elif request.method=="PATCH":
        return jsonify(request="PATCH",message="You are viewing flaask route")
    else:
        return jsonify(request="DELETE",message="You are viewing flaask route")        

#GET/id
@app.route('/sample/<page_id>')    

def sample(page_id):
    return f"<h1>{page_id}</h1>"




      

if __name__=='main':
    app.run()    