import pandas as pd  # Reading the data and preparing it for analysis
from sklearn.linear_model import LinearRegression  # Training a linear regression model
import tabula
import csv
import streamlit as st  # Using Streamlit to create a simple web app to display results

st.set_page_config(layout="wide", page_title="Gestational Diabetes Predictor")

# CSS code for removing the default streamlit buttons on the GUI
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# connecting stylesheet
with open("main.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.header("Manual prediction using four common metrics")


def not_detected():
    """This is the default message that will be displayed when diabetes is not detected."""
    st.write("Congratulations, and though you may be safe it doesn't mean that you can ignore your health.")

    st.markdown("1) _Cut sugar and refined carbohydrates from your diet._")
    st.write("Eating foods high in refined carbohydrates and sugar increases blood sugar "
             "and insulin levels, which may lead to diabetes over time. Examples of refined "
             "carbohydrates include white bread, potatoes and many breakfast cereals. Instead, "
             "limit sugar and choose complex carbohydrates such as vegetables, oatmeal and whole grains.")

    st.markdown("2) _Quit smoking._")
    st.write("if you are a current tobacco user, smoking can contribute to insulin resistance, "
             "which can lead to Type 2 diabetes. Quitting has been shown to reduce this risk "
             "of Type 2 diabetes over time.")

    st.markdown("3) _Watch your portions._")
    st.write("Avoiding large portion sizes can help reduce insulin and blood sugar levels "
             "and decrease the risk of diabetes. Eating too much food at one time has been shown "
             "to cause higher blood sugar and insulin levels in people at risk of diabetes.")

    st.markdown("4) _Aim for 30 mins of exercise daily._")
    st.write("Try to be intentionally active by taking a walk, dancing, lifting weights or swimming "
             "for 30 minutes, five days per week. If you get no or very little physical activity "
             "then you lead a sedentary lifestyle, and it's time to get moving!")

    st.markdown("5) _Drink water._")
    st.write("Drinking water instead of other beverages may help control blood sugar and insulin levels, "
             "thereby reducing the risk of diabetes. Sticking with water most of the time helps you "
             "avoid beverages that are high in sugar, preservatives and other unneeded ingredients.")

    st.markdown("6) _Eat Fiber._")
    st.write("Getting plenty of fiber is beneficial for gut health and weight management. Having a good "
             "fiber source at each meal can help prevent spikes in blood sugar and insulin levels, which may "
             "help in reducing your risk of developing diabetes.")


def detected():
    """This is the default message that will be displayed when diabetes is detected."""
    st.subheader("Here are a few necessary precautions to take before you visit your doctor:")

    st.markdown("1) _Reduce your total carb intake._")
    st.write("Eating foods high in refined carbs and sugar increase blood sugar and insulin levels, "
             "which may eventually lead to diabetes. Limiting total carbohydrate intake and choosing options "
             "that don’t cause blood sugar spikes may help reduce your risk.")

    st.markdown("2) _Exercise regularly_")
    st.write("People with pre-diabetes often have reduced insulin sensitivity, also known as insulin resistance. "
             "In this state, your pancreas has to make more insulin to get sugar out of your blood and into cells. "
             "Exercise increases the insulin sensitivity of your cells, meaning that you need less insulin to manage "
             "your blood sugar levels.")

    st.markdown("3) _Make water as your primary beverage._")
    st.write("Drinking water instead of sugary beverages may help manage blood sugar and insulin levels, "
             "thereby reducing your risk of diabetes.")

    st.markdown("4) _Try to lose excess weight._")
    st.write("Modest weight loss may significantly reduce your risk of diabetes, particularly if you have "
             "excess abdominal weight.")

    st.markdown("5) _Quit smoking._")
    st.write("Smoking, especially heavy smoking, is strongly linked to diabetes risk. Quitting has been shown "
             "to reduce this risk over time.")

    st.markdown("6) _Reduce your portion sizes._")
    st.write("Avoiding large portion sizes may help reduce insulin and blood sugar levels, promote weight "
             "loss, and decrease your risk of diabetes.")


def prediction(pred):
    """Function that classifies the patient into the following 4 categories:
            1) Most Likely Diabetic
            2) Likely Diabetic
            3) At risk of Diabetes
            4) Unlikely to be Diabetic"""
    if pred >= 0.8:
        st.write("# :red[Most Likely Diabetic]")
        detected()
    elif 0.8 > pred >= 0.5:
        st.write("# :orange[Likely Diabetic]")
        detected()
    elif 0.5 > pred > 0.3:
        st.write("# :grey[At risk of Diabetes]")
        not_detected()
    else:
        st.write("# :green[Unlikely to be Diabetic]")
        not_detected()


def prediction_manual():
    """This functions takes 5 key factors into account and predicts whether the user is likely to be diabetic or not"""
    df1 = pd.read_csv("diabetes_dataset.csv")
    f = open("diabetes_manual.csv", "w")
    a = csv.writer(f)

    # split the data
    y1 = df1["Outcome"]
    x1 = df1[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]]

    # fit the model
    clf1 = LinearRegression()
    clf1.fit(x1, y1)

    # take the input
    pregnancies = st.number_input("Please enter the ***number of pregnancies***.", min_value=0, max_value=15)
    glucose = st.number_input("Please enter your ***glucose level***. (Normal: 80-100, "
                              "Impaired Glucose: 101-125, Diabetic: 126+)", min_value=0, max_value=200)
    blood_pressure = st.number_input("Please enter your ***diastolic blood pressure***. "
                                     "(Normal: <80, High: 80+)", min_value=0, max_value=200)
    bmi = st.number_input("Please enter your ***BMI***. (Underweight: <18.5, Normal: 18.5-24.9, "
                          "Overweight: 25.0-29.9, Obese: 30.0+)", min_value=0, max_value=100)
    age = st.number_input("Please enter your ***age***.", min_value=21, max_value=100)

    information = [pregnancies, glucose, blood_pressure, bmi, age]
    a.writerow(information)
    f.flush()
    cols = ["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]

    data1 = pd.read_csv("diabetes_manual.csv", names=cols, header=None)
    st.write("*Your Data:*")
    st.dataframe(data1, width=1500)

    count = 0

    # condition to check if the user input any data or not
    for i in information[1:]:
        if i == 0:
            count += 1

    # if the user did input data, then the program will put in the data in the Linear Regression model
    if count == 0:
        pred = clf1.predict(data1)
        prediction(pred)

# calling the main prediction function
prediction_manual()
