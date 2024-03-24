import pickle

import os
# diab_prediction = diabetes_model.predict([[1,103,30,38,83,43.3,0.183,33]])
# print(diab_prediction)

def predict_diabetes(input_array):
    diabetes_model_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','models','diabetes_model.sav'))
    diabetes_model = pickle.load(open(diabetes_model_path,'rb'))
    diab_prediction = diabetes_model.predict([input_array])
    if diab_prediction[0] == 1:
        return True
    
    return False