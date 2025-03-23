import pandas as pd  # Reading the data and preparing it for analysis
from sklearn.linear_model import LinearRegression  # Training a linear regression model
import tabula
import csv
import streamlit as st  # Using Streamlit to create a simple web app to display results

# setting page layout
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

with open("main.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True) #connecting stylesheet

# Loading the data and fitting it in the Linear Regression Algorithm
df = pd.read_csv("diabetes_dataset.csv")

# setting the dependent and independent variables
y = df["Outcome"]  # dependent variable is the field with the name 'Outcome'
x = df.iloc[:, 0:-1]  # all columns except the last one are taken as independent variables

# creating line-of-best-fit
clf = LinearRegression()  # initiates the model
clf.fit(x, y)  # line-of-best-fit between x and y which were assigned earlier

st.header("Automatic Prediction Using Patient Medical Report")


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

    st.markdown("4) _Aim for 30 minutes of exercise daily._")
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


def prediction_automatic(pdf_file):
    """Function that reads the PDF medical report from the patient as input and returns the predicted value"""
    f = open("diabetes.csv", "w")
    a = csv.writer(f)

    tables = tabula.read_pdf(pdf_file, pages=1, multiple_tables=False)

    df = tables[0]["XYZ HOSPITAL, UAE"]

    cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age"]

    # adding row in data frame
    a.writerow(df)

    # clears buffer to immediately update the dataset
    f.flush()

    # read file
    data = pd.read_csv("diabetes.csv", names=cols, header=None)

    # display the data
    st.write("*Your Data:*")
    st.dataframe(data, width=1500)

    # make a prediction based on the data provided
    pred = clf.predict(data)
    prediction(pred)

# handling exceptions such as uploading the wrong file format or a non-medical report.
with st.form("upload-form", clear_on_submit=True):
    pdf_file = st.file_uploader("Enter your Medical Report here", type=["pdf"], accept_multiple_files=False)
    submitted = st.form_submit_button("Upload")
    if pdf_file and submitted is not None:
        try:
            prediction_automatic(pdf_file)  # runs the prediction_automatic function if pdf file is true and has data
        except:
            st.write("Please enter a valid PDF medical report.")  # raises exception
    else:
        st.write("Please enter your PDF medical report.")  # requests for report input

st.markdown("<h2>Help us train our model with your data!</h2>", unsafe_allow_html=True)


def add_data():
    """This section allows the user to give us their actual values so that we can improve our model"""
    pregnancies = st.number_input("Please enter the ***number of pregnancies***.", min_value=0)
    glucose = st.number_input("Please enter the ***glucose level***.", min_value=0)
    blood_pressure = st.number_input("Please enter the ***diastolic blood pressure***.", min_value=0)
    skin_thickness = st.number_input("Please enter the ***skin thickness***.", min_value=0)
    insulin = st.number_input("Please enter the ***insulin***.", min_value=0)
    bmi = st.number_input("Please enter the ***BMI***.", min_value=0)
    diabetes_pedigree_function = st.number_input("Please enter the ***diabetes pedigree function***.", min_value=0)
    age = st.number_input("Please enter the ***age***.", min_value=21)
    outcome = st.number_input("Please enter the ***outcome***. (0 - Non-Diabetic & 1 - Diabetic)", min_value=0, max_value=1)

    data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age, outcome]
    return data


data = add_data() # adds the new data to the model

# We first write the data in a temporary file and then append it to the actual dataset.
f = open("diabetes_automatic.csv", "w")
a = csv.writer(f)

# adding data in the dataset to improve model
f1 = open("diabetes_dataset.csv", "a")
a1 = csv.writer(f1)

submit = st.button("Submit")

if submit:  # upon clicking of submit button
    a.writerow(data)  # new data row is added
    f.flush()  # immediately clears buffer to update dataset
    cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age", "Outcome"]  # variables

    data1 = pd.read_csv("diabetes_automatic.csv", names=cols, header=None) # reads PDF file
    st.write("*Dataset Added:*")
    st.dataframe(data1,width=1500)  # displays new data

    st.write("Thank you for your data!")
