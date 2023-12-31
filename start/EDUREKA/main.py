from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):  
    user_data={
        "user":user_id,
        "email":"lakshaykhattar0208@gmail.com",
        "user_name":"name"
    }
    
    extra= request.args.get("extra")
    if extra: 
        user_data["extra"]=extra
        
         
    return jsonify(user_data),200


if __name__=="__main__":     
    app.run(debug=True)