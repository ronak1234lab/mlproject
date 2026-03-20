from flask import Flask, request, render_template
import pandas as pd

from src.pipeline.predict_pipeline import PredictPipeline

app = Flask(__name__)

# Landing Page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    else:
        data = {
            "gender": request.form.get('gender'),
            "race_ethnicity": request.form.get('race_ethnicity'),
            "parental_level_of_education": request.form.get('parental_level_of_education'),
            "lunch": request.form.get('lunch'),
            "test_preparation_course": request.form.get('test_preparation_course'),
            "reading_score": float(request.form.get('reading_score')),
            "writing_score": float(request.form.get('writing_score'))
        }

        print("FORM DATA:", data)

        pred_df = pd.DataFrame([data])

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=round(results[0], 2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)