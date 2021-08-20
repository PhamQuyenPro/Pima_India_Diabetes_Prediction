# ***Pima_India_Diabetes_Prediction***
***Introduction***
<br>
Diabetes mellitus (DM), commonly known as just diabetes, is a group of metabolic disorders characterized by a high blood sugar level over a prolonged period of time.
Symptoms often include frequent urination, increased thirst and increased appetite.
If left untreated, diabetes can cause many health complications.
Acute complications can include diabetic ketoacidosis, hyperosmolar hyperglycemic state, or death.
Serious long-term complication include cardiovascular disease, stroke, chronic kidney disease, foot ulcers, damage to the nevers, damage to the eyes and cognitive impairment.
<br>
<br>
***Types of Diabetes***
<br>
There are three main types of diabetes: type 1, type 2 and gestational diabetes (diabetes while pregnant)
<br>
**Type 1 Diabetes**
<br>
Type 1 diabetes is thought to be caused by an autoimmune reation (the body attacks ifself by mistake) that stops your body from making insulin.
Approximately 5-10% of the people who have diabetes have type 1.
Symptoms of type 1 diabetes often develop quickly. It's usually diagnosed in children, teens, and yuong adults.
If you have tyoe 1 diabetes, you'll need to take insulin every day to survise.
Currently, no one knows how to prevent type 1 diabetes.
<br>
**Type 2 Diabetes**
<br>
With type 2 diabetes, your body doesn't use insulin well and can't keep blood sugar at normal levels.
About 90-95% of people with diabetes have type 2.
It develops over many years and is usually diagnosed in aadults (but more and more children, teens, and young adults).
You may not notice any symptoms, so it's important to get your blood sugar tested if you're at risk.
Type 2 diabetes can be prevented or delayed with healthy filestyle changes, such as losing weight, eating healthy food, and being active.
<br>
**Gestational Diabetes**
<br>
Gestational diabetes develops in pregnant women who have never had diabetes.
If you have gestional diabetes, your baby could be at higher risk for health problems.
Gestational diabetes usally goes away after your baby is born but increase your risk for type 2 diabetes later in file.
Your baby is more likely to have obesity as a child or teen, and more likely to develop type 2 diabetes later in life too.
<br>
<br>
***About Dataset***
<br>
**Context**
<br>
This dataset is originally from the National Institude of Diabetes and Digestive and Kidney Diseases.
The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.
Several constraints were placed on the selection of these instances from a larger database. 
In particular, all patients here are females at least 21 years old of Pima Indian heritage.
<br>
**Content**
<br>
The datasets consists of several medical predictor variables and one target varaiable, Outcome.
Predictor variables includes the number of pregnancies the patient has had their BMI, insulin level, age and so on.
<br>
**Variable Description**
<br>
*Pregnancies:* Number of times pregnant.
<br>
*Glucose:* Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
<br>
*BloodPressure:* Diastolic blood pressure (mmHg).
<br>
*SkinThickness:* Triceps skin fold thickness (mm).
<br>
*Insulin:* 2-Hour serum insulin (mu U/ml).
>br>
*BMI:* Body mass index (weight in kg/(height in m)^2)
<br>
*DiabetesPedigreeFunction:* Diabetes pedigree function.
<br>
*Age:* Age (years).
<br>
*Outcome:* Class variable (0 or 1) 268 of 768 are 1, the others are 0.
<br>
<br>
***Preprocessing Data***
<br>
Using Nearest neightbor imputation (KNN inpution) and mean, median values in the dataset to fill all the missing values.
<br>
<br>
***Model training**
<br>
Using Random Forest Classifier, Support Vector Classification and Tune Catboost to train the data.
<br>
<br>
***Deployment the trained model 
<br>
Using flask to build webserver on local PC and build a website for users.



