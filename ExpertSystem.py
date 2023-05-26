illnesses = {
"cold" : ["headache", "running nose", "sneezing", "sore throat"],
"influenza" : ["sore throat", "chills", "body ache", "fever", "headache"],
"typhoid" : ["headache", "abdominal pain", "poor appetite", "fever"],
"chicken pox" : ["rash", "body ache", "fever"],
"malaria" : ["fever", "headache", "nausea", "vommiting", "diarrhea", "sweating"]
}

treatments = {
    "cold" : ["Panadol", "Tylenol", "Nasal Spray"],
"influenza" : ["Panadol", "Tamiflu", "Zanamivir"],
"typhoid" : ["Chloramphenicol", "Amoxicilin", "Ciprofloxacin", "Azithromycin"],
"chicken pox" : ["Varicella vaccine", "Immunoglobulin", "Acetomenaphin", "Acyclovir"],
"malaria" : ["Artalen", "Qualaquin", "Plaquenil", "Mefloquin"]
}

advice = {
    "cold" : "Please do wear warm clothes because",
"influenza" : "Please take a warm bath and do salt gargling because ",
"typhoid" : "Please do have bed rest and take a soft diet because ",
"chicken pox" : "Please do have oatmeal and stay at home because ",
"malaria" : "Please do not sleep in open air and cover your full skin because "
}

# print("Please enter your symptoms seperated by commas: ")
# symptoms = input().split(" , ")

# illness = None
# for i in illnesses.keys():
#     if set(symptoms).issuperset(set(illnesses[i])):
#         illness = i
#         break

# if illness is None:
#     print("We are sorry we couldn't determine your illness. Please consult a Doctor for more information.")
# else:
#     print("You may have " + illness + ". Here are our reccomendations: ")

#     print("Treatments : ")

#     for t in treatments[illness]:
#         print(" - " + t)
#     print("Advice : ")
#     print(advice[illness])



print("Enter the symptoms : ")
symptoms = input().split(" , ")

illness = None
for i in illnesses.keys():
    if(set(symptoms).issuperset(set(illnesses[i]))):
        illness = i
        break

if illness == None:
    print("Sorry, we couldn't identify the disease")

else:
    print("You are suffering from " + illness)
    print("Treatments : ")

    for t in treatments[illness]:
        print("- ", t)
    print()

    print("Advice")
    print(advice[illness])