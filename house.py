from flask import Flask, render_template, request, redirect
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("house_price_model.pkl")

@app.route("/", methods=['GET', 'POST'])
def predictions():
    prediction = None
    if request.method == "POST":
        area = float(request.form.get("area"))
        bedrooms = float(request.form.get("bedrooms"))
        bathrooms = float(request.form.get("bathrooms"))
        age = float(request.form.get("age"))

        if not area or not bedrooms or not bathrooms or not age:
            print("please fill all fields")
            return redirect("/")

        our_data = [[area, bedrooms, bathrooms, age]]
        prediction = model.predict(our_data)[0]
        prediction = round(prediction, 2)

        return render_template("house_price_pred.html", prediction=prediction)
    return render_template("house_price_pred.html", prediction=prediction)


@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")


@app.route("/about-model")
def about_model():
    return render_template("about_model.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')