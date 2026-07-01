from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Create Label Encoder
encoder = LabelEncoder()
encoder.fit(df["label"])

# Load trained model
with open("../2_Model_Development/logistic_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        sample = [[N, P, K, temperature, humidity, ph, rainfall]]

        prediction = model.predict(sample)

        crop = encoder.inverse_transform(prediction)

        return render_template(
            "index.html",
            prediction_text=f"🌾 Recommended Crop: {crop[0].capitalize()}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)