from flask import Flask, request, render_template_string
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Flood Prediction</title>
<style>
body{
font-family:Arial;
background:#f2f2f2;
padding:40px;
}
.container{
background:white;
padding:25px;
width:400px;
margin:auto;
border-radius:10px;
box-shadow:0 0 10px gray;
}
input{
width:100%;
padding:8px;
margin:5px 0;
}
button{
padding:10px;
width:100%;
background:#007bff;
color:white;
border:none;
}
h2{
text-align:center;
}
</style>
</head>
<body>

<div class="container">

<h2>Flood Prediction</h2>

<form method="POST">

<input type="number" step="any" name="Temp" placeholder="Temperature" required>

<input type="number" step="any" name="Humidity" placeholder="Humidity" required>

<input type="number" step="any" name="Cloud Cover" placeholder="Cloud Cover" required>

<input type="number" step="any" name="ANNUAL" placeholder="Annual Rainfall" required>

<input type="number" step="any" name="Jan-Feb" placeholder="Jan-Feb" required>

<input type="number" step="any" name="Mar-May" placeholder="Mar-May" required>

<input type="number" step="any" name="Jun-Sep" placeholder="Jun-Sep" required>

<input type="number" step="any" name="Oct-Dec" placeholder="Oct-Dec" required>

<input type="number" step="any" name="avgjune" placeholder="Average June" required>

<input type="number" step="any" name="sub" placeholder="Subdivision Value" required>

<button type="submit">Predict</button>

</form>

{% if prediction %}

<h3 style="text-align:center">{{ prediction }}</h3>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    prediction = ""

    if request.method == "POST":

        data = pd.DataFrame([[
            float(request.form["Temp"]),
            float(request.form["Humidity"]),
            float(request.form["Cloud Cover"]),
            float(request.form["ANNUAL"]),
            float(request.form["Jan-Feb"]),
            float(request.form["Mar-May"]),
            float(request.form["Jun-Sep"]),
            float(request.form["Oct-Dec"]),
            float(request.form["avgjune"]),
            float(request.form["sub"])
        ]], columns=[
            "Temp",
            "Humidity",
            "Cloud Cover",
            "ANNUAL",
            "Jan-Feb",
            "Mar-May",
            "Jun-Sep",
            "Oct-Dec",
            "avgjune",
            "sub"
        ])

        result = model.predict(data)[0]

        if result == 1:
            prediction = "Flood Likely"
        else:
            prediction = "No Flood"

    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)