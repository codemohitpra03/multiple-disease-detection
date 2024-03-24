import pickle

import os


def predict_heart_disease(input_array):
    heart_disease_model_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','models','heart_disease_model.sav'))
    heart_disease_model = pickle.load(open(heart_disease_model_path,'rb'))
    heart_prediction = heart_disease_model.predict([input_array])
    if heart_prediction[0] == 1:
        return True
    
    return False