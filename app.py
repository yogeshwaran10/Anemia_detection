from flask import Flask, render_template, request
import numpy as np
import joblib
from flask import jsonify 
app = Flask(__name__)

# Load pre-trained model
print("Loading model...")
model = joblib.load('model/random_forest_classifier.pkl')
print("Model loaded successfully.")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        print("POST request received.")
        try:
            # Debugging: Check form values
            print("Form data:", request.form)

            hemoglobin = float(request.form['hemoglobin'])
            mcv = float(request.form['mcv'])
            mch = float(request.form['mch'])
            mchc = float(request.form['mchc'])
            gender = request.form['gender']

            # Convert gender to binary (0 for Female, 1 for Male)
            gender_binary = 1 if gender.lower() == 'male' else 0
            print(f"Parsed inputs: Hemoglobin={hemoglobin}, MCV={mcv}, MCH={mch}, MCHC={mchc}, Gender={gender} (Binary={gender_binary})")

            # Prepare the input features
            features = np.array([[gender_binary, hemoglobin, mch, mchc, mcv]])
            print("Prepared features:", features)

            # Predict the result
            prediction = model.predict(features)[0]
            print("Model prediction:", prediction)

            result = 'Anemic' if prediction == 1 else 'Not Anemic'
            print("Result:", result)

        except Exception as e:
            print("Error occurred:", str(e))
            result = f"Error: {e}"

    # Debugging: Check final result before rendering
        print("Final result to render:", result)
        return jsonify({"result": result})
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
