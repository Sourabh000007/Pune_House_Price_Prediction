import pandas as pd
import numpy as np
import json
import pickle
import warnings
warnings.filterwarnings("ignore")
import config


class Housing_Price(): 
                      
    def __init__(self,total_sqft,bath,balcony,site_location,area_type,Availability,BHK):
        self.total_sqft     = total_sqft
        self.bath           = bath
        self.balcony        = balcony
        self.site_location  = site_location
        self.area_type      = "area_type_" + area_type
        self.Availability   = Availability
        self.BHK            = BHK

    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.load_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.load_json = json.load(f)

    def check(self):

        if self.Availability == "Ready To Move":
            test = "Availability_Ready_To_Move" 
            return list(self.load_json["columns"]).index(test)
            
        elif self.Availability == "Immediate Possession":
                
            test = "Availability_Immediate_Possession"
            return list(self.load_json["columns"]).index(test)
        else:
             return 0

    def get_predicted_price(self):

        self.load_models()

        area_type_index = list(self.load_json["columns"]).index(self.area_type)

        test_array = np.zeros(len(self.load_json["columns"]))

        avail_result = self.check()

        old = 0 if avail_result > 0 else self.load_json["Availability"]["Availability_Month"][self.Availability]

        new = 1 if avail_result > 0 else self.total_sqft

        test_array[0]                   = self.total_sqft
        test_array[1]                   = self.bath
        test_array[2]                   = self.balcony
        test_array[3]                   = self.load_json["site_location"][self.site_location]
        test_array[area_type_index]     = 1
        test_array[avail_result]        = new
        test_array[-2]                  = old
        test_array[-1]                  = self.BHK


  

        price = round(self.load_model.predict([test_array])[0])

        return price



    
if __name__== "__main__":

    total_sqft    = 1000
    bath          = 4
    balcony       = 2
    site_location = "Dhayari Phata"
    area_type     = "Super built-up  Area"
    Availability  = "Aug"
    BHK           = 4

    area_type     = "area_type_" + area_type                      


    hous_pr = Housing_Price(total_sqft,bath,balcony,site_location,area_type,Availability,BHK)
    price = hous_pr.get_predicted_price()
    print(price)
    