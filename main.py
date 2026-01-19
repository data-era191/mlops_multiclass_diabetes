from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd 
import joblib
import uvicorn

app = FastAPI()

class Diabetes (BaseModel):
    Gender:float
    AGE:float
    Urea:float
    Cr:float
    HbA1c:float
    Chol:float
    TG:float
    HDL:float
    LDL:float
    VLDL:float
    BMI:float
    
@app.post("/add")
def add (dib:Diabetes):
    
    model=joblib.load("model.pkl")
    
    ss=StandardScaler()
    
    x = pd.DataFrame([{
                "Gender":dib.Gender,
                "AGE":dib.AGE,
                "Urea":dib.Urea,
                "Cr":dib.Cr,
                "HbA1c":dib.HbA1c,
                "Chol":dib.Chol,
                "TG":dib.TG,
                "HDL":dib.HDL,
                "LDL":dib.LDL,
                "VLDL":dib.VLDL,
                "BMI":dib.BMI,
        }])
                    
    y_pred=model.predict(ss.fit_transform(x))
        
    return {"y_pred": int(y_pred[0])}

