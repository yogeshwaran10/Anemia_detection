from flask import Flask, render_template, request, redirect, url_for
from forms import AnemiaForm
import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load the pre-trained model
model_path = 'model/random_forest_classifier.pkl'
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)
    model = None


gender_mapping = {'Male': 0, 'Female': 1}

@app.route('/', methods=['GET', 'POST'])
def home():
    form = AnemiaForm()
    if form.validate_on_submit() and model is not None:
        # Collect form data
        hemoglobin = float(form.hemoglobin.data) 
        gender = gender_mapping[form.gender.data] 
        mcv = float(form.mcv.data)  
        mch = float(form.mch.data)  
        mchc = float(form.mchc.data)  
        
        
        input_data = np.array([[gender,hemoglobin,mch, mchc,mcv]])
        
     
        prediction = model.predict(input_data)[0]
        
        return redirect(url_for('result', prediction=prediction))
    return render_template('home.html', form=form)

@app.route('/result/<prediction>')
def result(prediction):
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
