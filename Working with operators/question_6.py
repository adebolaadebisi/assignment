# admission eligibility
# collect user details
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Is UNILAG your first choice? (yes/no): ").lower()
olevel_passes = int(input("Enter number of o'Level credit passes at one sitting: "))
post_utme_score = int(input("Enter your post_UTME score: "))

#condition check
if age < 16:
    print("Not eligible: you must be at least 16 years old.")
elif utme_score < 200:
    print("Not eligible: UTME score must be 200 or above. ")
elif first_choice != "yes": 
    print("Not eligible: you must choose UNILAG as your first choice.")  
elif olevel_passes < 5:  
    print("Not eligible: you must have at least 5 credit passes in o'Level at one sitting.")
elif post_utme_score < 200:
    print("Not eligible: post_UTME cut_off starts from 200.") 
else:
    print("congratulations! you are eligible for admission consideration.")     