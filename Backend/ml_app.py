import pandas as pd
import pickle
from sklearn.preprocessing import FunctionTransformer
import re
import string
import uvicorn
from pydantic import BaseModel
import json
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
# Initializing the fast API server
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Defining the model input types
class model_input(BaseModel):
    title: str
    text: str
    subject: str
    date: str
    
# custom function for prediction

def output_lable(n):
    if n == 0:
        return " Fake News"
    elif n == 1:
        return " Not A Fake News"

def word_drop(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def check(news, word_drop):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_x_test = new_def_test["text"].apply(word_drop)
    model_NB = pickle.load(open("model/MultiNomialNB_Classifier_new_version.pkl", "rb"))
    model_svc = pickle.load(open("model/SVC_scikit_1.3.0.pkl", "rb"))
    model_rfc= joblib.load("model/RandomForestClassifier_model.joblib")
    pred_NB = model_NB.predict(new_x_test)
    pred_svc = model_svc.predict(new_x_test)
    pred_rfc=model_rfc.predict(new_x_test)
    output_prediction = {
            "NB": output_lable(pred_NB[0]),
            "SVC":  output_lable(pred_svc[0]),
            "RFC": output_lable(pred_rfc[0])
    }
    return output_prediction

def news_prediction(input_parameters):
    text = input_parameters
    f = open("output/sample.txt", "a+")
    f.write("-*OM\n")
    f.close()
    res = check(text, word_drop)
    out_json = json.dumps(res)
    return out_json

# Setting up the home route
@app.get("/")
def read_root():
    return {"data": "Welcome to online Imitation_News_Observation_For_Social_Media_Using_Different_Machine_learning_Mode prediction model"}

# Setting up the prediction route
@app.post("/predict/")
async def predict_news(input_parameters: model_input):
    text = input_parameters.text
    return news_prediction(text)

# Configuring the server host and port
if __name__=="__main__":
    uvicorn.run(app,"0.0.0.0","10000")