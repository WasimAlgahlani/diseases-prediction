import pandas
import datetime as dt

try:
    diseases_symptoms = pandas.read_csv("data/Dataset.csv")
    data = diseases_symptoms.to_dict()

except FileNotFoundError:
    print("There is no dataset.")
    exit()

name = input("Enter patient's name: ").title()

sym_num = int(input("How many symptoms is the patient suffering from? "))
print()
if sym_num >= 3:
    symptoms = []
    diseases = []
    for i in range(sym_num):
        symptoms.append(input(f"Enter symptom number {i + 1}: ").lower())
        flag = 0
        for j in range(len(data["symptom"])):
            if data["symptom"][j] == symptoms[i]:
                flag += 1
                break
        if flag == 0:
            print("There is no such symptom name in the dataset.")
            exit()
        diseases.append(diseases_symptoms[diseases_symptoms["symptom"] == symptoms[i]]["disease"].values)

    diseases2 = []
    diseases3 = []
    for c in range(sym_num):
        for col in diseases[c]:
            if col not in diseases2:
                diseases2.append(col)
            else:
                diseases3.append(col)

    suspected_diseases = []
    for column in diseases3:
        if column not in suspected_diseases:
            suspected_diseases.append(column)

    print(f"\nPatient's name is : {name}.\npossible disease(s):\n{suspected_diseases}")

    date = dt.date.today()

    with open(f"patients-data/{name.title()}-{date}.txt", "w") as patient:
        diseases_for_patient = ""
        for di in suspected_diseases:
            diseases_for_patient += f"{di}.\n"
        patient.write(f"Patient's name is : {name}.\n\npossible disease(s):\n{diseases_for_patient}")

else:
    print("Sorry, patient have to got at least 3 symptoms to be diagnosed.")
