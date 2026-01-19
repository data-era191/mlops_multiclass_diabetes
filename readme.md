## Introduction
create this project about predict diabetes type and existance 
## Tools and Technology
- xgboost==3.0.5
- scikit-learn==1.7.1
- tensorflow==2.20.0
- pydantic==2.11.7
- pandas==2.3.2
- lightgbm==4.6.0
- keras==3.11.3
- joblib==1.5.2
- fastapi==0.116.1
- docker
- uvicorn
## Run project
1) entry to the place where main.py exist 
```shell
    cd multiclass_diabetes/machine_learning
```
2) launch app using docker
```shell
docker build -t diabetes .

docker run -p 8000:8000 diabetes
```
## test project 
1) postman
```json
{
    "Gender":0,
    "AGE":20,
    "Urea":2.0,
    "Cr":50,
    "HbA1c":3.2,
    "Chol":3.4,
    "TG":0.5,
    "HDL":1.0,
    "LDL":0.2,
    "VLDL":0.7,
    "BMI":22.0
}
```

