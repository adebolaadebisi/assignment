
from pathlib import Path
import file_ops
def localpath():
    folder = Path('participant_pkg')
    return folder / 'participants.csv'
def participant():
    dic = {}
    try:
        name = input("Enter participant's name here: ").strip()
        age = input("Enter participant's age here: ").strip()
        phone = input("Enter participant's phone here: ").strip()
        track = input("Enter participant's track here: ").strip()
        # VALIDATIONS
        if not name:
            raise ValueError("Name cannot be left empty")
        if not age.isdigit() or int(age) <= 0:
            raise ValueError("Age must be a positive number")
        if len(phone) != 11 or not phone.isdigit():
            raise ValueError("Phone number must be 11 digits")
        if not track:
            raise ValueError("Track cannot be left empty")
        dic['name'] = name
        dic['age'] = int(age)
        dic['phone'] = phone
        dic['track'] = track
    except ValueError as e:
        print("Error:", e)
        return None  # skip invalid participant
    return dic
def participant_list(n):
    path = localpath()
    for i in range(n):
        participant_dic = participant()
        if participant_dic:  # only save valid participant
            file_ops.save_participant(path, participant_dic)
def show_summary():
    path = localpath()
    participants = file_ops.load_participants(path)
    if participants:
        print("\nSummary of Participants:")
        for p in participants:
            print(p)
        
    else:
        print("No participants found.")
# --- RUN EXAMPLE ---
num = int(input("How many participants do you want to add? "))
participant_list(num)
show_summary()
          
           




 




