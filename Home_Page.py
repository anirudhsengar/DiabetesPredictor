import pandas as pd  # reading the dataset
import streamlit as st  # for GUI

st.set_page_config(layout="wide", page_title="Gestational Diabetes Predictor")  # page layout

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
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)  # connecting stylesheet

# Header
st.markdown("<h1>Gestational Diabetes Predictor</h1>", unsafe_allow_html=True)
st.write("<h6> By Anirudh Sengar (23001546), Suleiman Altaf (23001666), and Mohammed Abduljalil (23003266)</h6>", unsafe_allow_html=True)
st.header("", divider="rainbow")

# Introduction
st.markdown("<h2> About The Project </h2>", unsafe_allow_html=True)

st.markdown("##### _What is diabetes?_")
st.write("- Diabetes is a chronic health condition that affects how human body turns "
         "food into energy. The human body breaks down most of the food into sugar "
         "(glucose) and releases it into the bloodstream. When blood sugar goes up, it "
         "signals the pancreas to release insulin. Insulin acts like a key to let the blood "
         "sugar into the human body’s cells for use as energy. A diabetic human body does not "
         "make enough insulin or is unable to use it as well as it should. When there is "
         "not enough insulin or cells stop responding to insulin, too much blood sugar stays "
         "in the bloodstream. Over time, that can cause serious health problems, such as heart "
         "diseases, vision loss, and kidney diseases.")

st.markdown("##### _What are the different types of diabetes?_")

st.write("- **Type 1** - Once known as juvenile diabetes or insulin-dependent "
         "diabetes, is a chronic condition. In this condition, the pancreas makes little or no insulin.")

st.write("- **Type 2** - This type of diabetes is a common condition that causes "
         "the level of sugar (glucose) in the blood to become too high. It can cause "
         "symptoms like excessive thirst, irregular urine and tiredness. It also increases "
         "the risk of getting serious problems with one's eyes, heart and nerves.")

st.write("- **Gestational Diabetes** - This type of diabetes is diagnosed for the first "
         "time during pregnancy (gestation). Like other types of diabetes, gestational "
         "diabetes affects how the cells use sugar (glucose). Gestational diabetes causes high "
         "blood sugar that can affect a pregnancy as well as the baby's health.")

st.markdown("##### _What type diabetes have we chosen and why?_")

st.write("In the United States alone, 6 out of every 100 pregnant women develop gestational "
         "diabetes. If not treated at the right time, gestational diabetes can increase the "
         "health risks of pregnancy by causing ***Macrosomia***, ***Shoulder dystocia***, ***Stillbirth***, "
         "and ***Preeclampsia*** among a lot of other dangerous complications.")

st.write("This not only risks the life of an adult woman but also their unborn child. Hence, "
         "we decided to create a Machine Learning Model that trains on existing data from existing "
         "diabetes' patients and uses the report of any user to predict whether they are most likely diabetic or not.")

# About the Data
st.markdown("<h2>Training Data</h2>", unsafe_allow_html=True)

st.markdown("##### _About the data_")

st.write("This dataset is originally from the National Institute of Diabetes and Digestive and Kidney "
         "Diseases. The objective of the dataset is to predict whether or not a patient has diabetes, based "
         "on certain diagnostic measurements included in the dataset. Several constraints were placed on the "
         "selection of these instances from a larger database. In particular, all patients here are females "
         "at least 21 years old of Pima Indian heritage.")

st.write("The dataset consists of several medical predictor variables and one target variable, "
         "***Outcome***. Predictor variables includes the number of pregnancies the patient has had, "
         "their BMI, insulin level, age, and so on. The training data includes reports of ***768*** women.")

# Visual Representation of the Dataframe
df = pd.read_csv("diabetes_dataset.csv")

y = df["Outcome"]  # extracts the outcome variable and assigns it to 'y'
x = df.iloc[:, 0:-1]  # selects all the columns except the last one and assigns them to 'x' which are the variables

st.markdown("##### _Dataframe_ ")
st.dataframe(df, width=1500)
st.markdown("##### _Graphical Representation_ ")
chart1 = st.bar_chart(df)  # bar chart
chart2 = st.scatter_chart(df)  # scatter chart

# Drawbacks that we are currently facing in making the model
st.markdown("##### _Limitations_")

st.markdown("- Glucose levels can vary throughout the day, and a single test may not capture the full picture. "
            "Repeat testing may be necessary for accurate diagnosis.")

st.markdown("- Some women may have insulin resistance that is not adequately reflected in routine glucose "
            "testing, leading to a potential delay in the diagnosis of gestational diabetes.")

st.markdown("- Inadequate follow-up after an initial abnormal screening test can result in missed opportunities "
            "for diagnosis and intervention.")

st.markdown("- Certain populations, such as women with a family history of diabetes or those with obesity, "
            "are at a higher risk. Failure to prioritize screening in these high-risk groups can lead to missed cases.")

st.markdown("- The dataset consists of data of women above the age of 21 years and belonging to the PIMA Indian "
            "heritage. Each demography and ethnicity has its own complexities and applying it to all women may result "
            "in inaccuracies. However, the aim of this model is to create a model where individual hospitals in a "
            "specific demography can include their own dataset.")
