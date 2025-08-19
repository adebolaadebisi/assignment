name = input ("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))
 #citizenship
citizenship = input("Enter your citizenship: ").lower()
#enrollement
enrollment = input("Are you enrolled in a nigeria university? (yes/no):").lower()
#other_scholarship
other_scholarship = input("Are you receiving any other scholarship? (yes/no):").lower()
distinction = int(input("How many distinctions (A/B) do you have in WAEC/WASSCE?: "))
 #Eligiblity
is_nigerian =(citizenship == "nigerian")
is_enrolled = (enrollment == "yes")
no_other_scholarship = (other_scholarship == "no")
has_required_distinction = (distinction >= 5)
eligibility = is_nigerian and is_enrolled and no_other_scholarship and has_required_distinction
print(f"\n{name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
print(f"\n{name}, your scholarship eligibility is: {eligibility}")