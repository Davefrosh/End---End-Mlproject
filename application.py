from flask import Flask,request,render_template

import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import Predict_pipeline,New_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = New_data(
            gender = request.form.get('gender'),
            race_ethnicity=request.form.get('race/ethnicity'),
            parental_level_of_education=request.form.get('parental level of education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test preparation course'),
            reading_score=int(request.form.get('reading score')),
            writing_score=int(request.form.get('writing score')))

        pred_df = data.get_as_dataframe()
        
        pipeline = Predict_pipeline()
        results = pipeline.initiate_predict_pipeline(pred_df)
        
        return render_template('home.html',results=results[0])
    
    
if __name__=='__main__':
    app.run(host='0.0.0.0')   