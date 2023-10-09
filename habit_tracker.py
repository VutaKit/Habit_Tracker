# Habit tracker backend application

from pymongo import MongoClient
from datetime import datetime, timedelta

#
# Connection and definition main function for interaction with MongoDB
#

# Connection to MongoDB
mongoUri = (
    "mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true"
)
client = MongoClient(mongoUri)


# Specify the database name
dbName = "habit_tracker"
db = client[dbName]

# Specify the collection within the database
collection = db["habit_list"]

# For predifined tasks
Day = 1
Week = 7
Month = 30
Year = 365


#
# Functions for creating and completing tasks
#


# Function create a task
def create_habit(name, task, periodicity, deadline_days):
    if name is None:
        print("Write a name!")
        return None
    elif task is None:
        print("Write a task!")
        return None

    # Calculate the deadline based on the current date and the specified periodicity
    deadline = datetime.now() + timedelta(days=deadline_days)

    habit = {
        "name": name,
        "task": task,
        "periodicity": periodicity,
        "streak": 0,
        "last_completed": None,
        "deadline": deadline,
    }

    return habit


# Function to complete a habit
def complete_habit(habit_name):
    # Find the habit document
    habit = collection.find_one({"name": habit_name})

    if habit:
        # Check if the habit is completed within the deadline
        if habit["deadline"] >= datetime.now():
            # Check if there is a streak required to establish a series
            if habit["streak"] > 0:
                # Check if the habit is completed consecutively
                if (
                    habit["last_completed"]
                    and (datetime.now() - habit["last_completed"]).days
                    <= habit["periodicity"]
                ):
                    habit["streak"] += 1
                else:
                    habit["streak"] = 0

                # Check if the streak has been established
                if habit["streak"] >= habit["streak_required"]:
                    print(
                        f'Habit "{habit_name}" has established a streak of {habit["streak"]} periods!'
                    )
            else:
                habit["streak"] += 1

            # Set the last_completed field to the current date and time
            habit["last_completed"] = datetime.now()

            # Update the habit document in the collection
            collection.update_one({"_id": habit["_id"]}, {"$set": habit})

            print(f'Habit "{habit_name}" completed within the deadline!')
        else:
            print(
                f'Habit "{habit_name}" was not completed within the deadline and is considered canceled!'
            )
    else:
        print(f'Habit "{habit_name}" not found!')


#
# Analytics module what will allow user to see longest series, total number of habits and analyse completion frequency
#


# Total number of habits
def get_total_number_of_habits():
    # Count the total number of habits in the collection
    total_habits = collection.count_documents({})

    return total_habits


def get_longest_series():
    # Find all habits
    habits = collection.find()

    longest_series = 0

    for habit in habits:
        # Extract relevant data (e.g., habit streak)
        streak = habit.get("streak", 0)

        # Update longest_series if needed
        if streak > longest_series:
            longest_series = streak

    return longest_series


# Return longest streak for a given habit
def get_longest_streak_for_habit(habit_name):
    # Find the habit in the collection
    habit = collection.find_one({"name": habit_name})

    if habit:
        # Retrieve the habit's streak
        streak = habit.get("streak", 0)
        return streak
    else:
        return "Habit not found"


def get_longest_streak_among_all_habits():
    # Find all habits in the collection
    habits = collection.find()

    longest_streak = 0

    for habit in habits:
        # Retrieve the habit's streak
        streak = habit.get("streak", 0)

        # Update longest_streak if needed
        if streak > longest_streak:
            longest_streak = streak

    return longest_streak


# Habit Frequency: Analyze and display how frequently each habit is completed on average.
def habit_frequency_stats():
    # Find all habits
    habits = collection.find()

    habit_stats = {}  # Dictionary to store habit names and their frequencies

    for habit in habits:
        habit_name = habit["name"]
        completion_date = habit["last_completed"]

        if habit_name not in habit_stats:
            habit_stats[habit_name] = {"count": 0, "total_days": 0}

        if completion_date:  # Check if habit has been completed at least once
            habit_stats[habit_name]["count"] += 1
            habit_stats[habit_name]["total_days"] += 1

    # Calculate the average frequency for each habit
    for habit_name, stats in habit_stats.items():
        if stats["count"] > 0:
            stats["average_frequency"] = stats["total_days"] / stats["count"]
        else:
            stats["average_frequency"] = 0

    return habit_stats


#
# Graphical representation of user's progress
#

import matplotlib.pyplot as plt

# habit streaks plot
def get_habit_streaks():
    # Find all habits
    habits = collection.find()

    streaks = {}  # Dictionary to store habit names and their streaks

    for habit in habits:
        # Extract relevant data (e.g., habit name, streak)
        habit_name = habit["name"]
        streak = habit.get("streak", 0)

        # Update the streaks dictionary
        streaks[habit_name] = streak

    return streaks


#
# Simple interface
#

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Habit Tracking App")

# Create and configure widgets (labels and buttons)
label_longest_series = tk.Label(root, text="Longest Series of Habits:")
label_total_habits = tk.Label(root, text="Total Number of Habits:")
result_longest_series = tk.Label(root, text=get_longest_series())
result_total_habits = tk.Label(root, text=get_total_number_of_habits())

# Place widgets on the window
label_longest_series.grid(row=0, column=0)
result_longest_series.grid(row=0, column=1)
label_total_habits.grid(row=1, column=0)
result_total_habits.grid(row=1, column=1)

# Start the GUI event loop
root.mainloop()


#
# #  Using functionality
#

# Creating new habit

new_habit_exercises = create_habit("Exercises", "Go for a run", Day, 2)
new_habit_musics = create_habit("Musics", "Meeting with music teacher", Week, 8)
new_habit_reads = create_habit("Reads", "30 pages", Day, 1)
new_habit_wash_car = create_habit("Wash the car", "Keeping car clean", Month, 31 )
new_habit_complete_homework = create_habit("Homework", "Complete school and house work", Day, 2)

# Inserting new habits into DB
inserted_document = collection.insert_many(
    [new_habit_exercises, new_habit_musics, new_habit_reads, new_habit_wash_car, new_habit_complete_homework]
)


# Complete a habit
complete_habit("Exercises")
complete_habit("Wash the car")
complete_habit("Homework")


# Call the function to get the total number of habits

total_habits = get_total_number_of_habits()
# Print or use the total_habits as needed
print(f"Total number of habits: {total_habits}")


# Call the function to get the longest series of habits

longest_series = get_longest_series()
# Print or use the longest_series as needed
print(f"Longest series of habits: {longest_series}")

# Get longest streak for a habit
habit_name = "Exercises"  # Replace with the actual habit name
longest_streak = get_longest_streak_for_habit(habit_name)
print(f"Longest streak for '{habit_name}': {longest_streak}")

# Get longest streak among all habits

longest_streak = get_longest_streak_among_all_habits()
print(f"Longest run streak among all habits: {longest_streak}")


# Get habit completion frequency

habit_frequency_data = habit_frequency_stats()
# Print the habit frequency statistics
for habit_name, stats in habit_frequency_data.items():
    print(f'Habit: {habit_name}')
    print(f'Average Frequency: {stats["average_frequency"]:.2f} days')


# Draw a graph for habit completion streaks

habit_streaks = get_habit_streaks()

# Extract habit names and streaks
habit_names = list(habit_streaks.keys())
streaks = list(habit_streaks.values())

# Create a bar chart to visualize the habit streaks
plt.figure(figsize=(10, 6))
plt.bar(habit_names, streaks, color='b')
plt.title('Habit Streaks for All Habits')
plt.xlabel('Habit Name')
plt.ylabel('Streak')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')
plt.tight_layout()

# Show the chart
plt.show()


# # Close the MongoDB connection
# client.close()
