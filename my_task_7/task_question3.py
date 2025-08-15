# task3
days = ("Monday", "Tuesday", "Thursday")
activities = []
for day in days:
    activity = input(f"Enter an activity for {day}: ")
    activities.append(activity)
    schedule = {day: activity for day, activity in zip(days, activities)}

    print("\n--- Days & Activities ---")
    print(schedule)
