# project title: contact saver
# case: you are running a short tech workshop and need a simple program to collect participant details:
# name, age, phone, and track. These details should be saved into a csv file so organizers can follow up later.


import csv
from pathlib import Path
def save_participant(path: Path, participant_dic: dict):
    path.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
    file_exists = path.exists()
    with open(path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'phone', 'track'])
        if not file_exists:
            writer.writeheader()
        writer.writerow(participant_dic)
def load_participants(path: Path):
    participants = []
    if path.exists():
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                participants.append(row)
    return participants