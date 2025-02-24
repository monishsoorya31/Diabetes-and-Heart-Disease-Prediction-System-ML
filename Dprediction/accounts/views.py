from django.shortcuts import render ,redirect
from diabetes.models import persons
from django.contrib import messages
import pickle 
import numpy as np
import pandas as pd


with open("Model//Path", "rb") as file:
    model = pickle.load(file)


def register(request):

    if request.method == 'POST':

        name = request.POST['name']
        pregnancies = request.POST.get('pregnancies', 0)
        glucose = request.POST.get('glucose', 0)
        bp = request.POST.get('bp', 0) 
        skin = request.POST.get('skin', 0)
        insulin = request.POST.get('insulin', 0)
        bmi = request.POST.get('bmi', 0)
        Diabetes = request.POST.get('Diabetes', 0)
        age = request.POST.get('age', 0)
        gender = request.POST.get('gender', 0)


        if persons.objects.filter(name=name).exists():
            messages.info(request,"user name taken")

        
        else:

            
            user = persons.objects.create(name=name, pregnancies=pregnancies, glucose=glucose,
            bp=bp, skin=skin, insulin=insulin, bmi=bmi,
            Diabetes=Diabetes, age=age, gender=gender)
            user.save()
            messages.info(request,"User Created")   

        column_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
        input_data = pd.DataFrame([[pregnancies, glucose, bp, skin, insulin, bmi, Diabetes, age]], columns=column_names)


        prediction = model.predict(input_data)

        if prediction == 1:
            
            pre = "True"

        else:

            pre = "False"



        patients = persons.objects.all()  # Fetch all records from the database

        return render(request, "details.html", {"patients": patients, 'prediction':pre})


    




