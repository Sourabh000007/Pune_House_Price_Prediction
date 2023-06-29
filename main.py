from flask import Flask,jsonify,render_template,request

from project_app.utils import Housing_Price

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("test.html")

@app.route("/predict_price", methods = ["POST","GET"])

def get_Housing_charges():
    if request.method == "GET":


        total_sqft      =  eval(request.args.get("total_sqft"))           
        bath            =  int(request.args.get("bath"))           
        balcony         =  int(request.args.get("balcony"))       
        site_location   =  request.args.get("site_location")         
        area_type       =  request.args.get("area_type")
        Availability    =  (request.args.get("Availability"))
        BHK             =  int(request.args.get("BHK"))

        print(total_sqft)
        print(bath)
        print(balcony)
        print(site_location)
        print(area_type)
        print(Availability)
        print(BHK)
               
        hous_pr = Housing_Price(total_sqft,bath,balcony,site_location,area_type,Availability,BHK)
        price = hous_pr.get_predicted_price()

        return render_template("test.html",prediction = price)
    
if __name__ == "__main__":
    app.run()