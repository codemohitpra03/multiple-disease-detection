import pickle

import os
parkinsons_model_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','models','parkinsons_model.sav'))
parkinsons_model = pickle.load(open(parkinsons_model_path,'rb'))
# diab_prediction = diabetes_model.predict([[1,103,30,38,83,43.3,0.183,33]])
# print(diab_prediction)

def predict_parkinsons(input_array):
    parkinsons_model_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','models','parkinsons_model.sav'))
    parkinsons_model = pickle.load(open(parkinsons_model_path,'rb'))
    parkinsons_prediction = parkinsons_model.predict([input_array])
    if parkinsons_prediction[0] == 1:
        return True
    
    return False