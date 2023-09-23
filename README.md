# habit_tracker
Habit tracker application.

Habit Tracker Application


The Habit Tracker Application is a tool for tracking and managing habits. This README provides instructions for setting up the application and using its features. 
The application includes functionalities for tracking habits, retrieving statistics, and displaying habit data via a web interface.


Installation

 1. Prerequisites
- Python 3.7 or higher installed.
- MongoDB installed and running.
- MongoDB Compass (optional, for graphical management).

 2. Install MongoDB
If you don't have MongoDB installed, you can follow these instructions to install it:

 For Windows:
1. Download the MongoDB Community Server from the official website: [MongoDB Downloads](https://www.mongodb.com/try/download/community).
2. Run the installer and follow the installation steps.
3. By default, MongoDB will be installed as a Windows service. You can start and stop the service from the Windows Services application.

 For macOS:
1. You can use Homebrew to install MongoDB. Open your terminal and run:

   ```bash
   brew tap mongodb/brew
   brew install mongodb-community
   ```
2. Start MongoDB by running:
   ```bash
   brew services start mongodb/brew/mongodb-community
   ```

 For Linux (Ubuntu):
1. You can install MongoDB on Ubuntu using apt-get. Open your terminal and run:

   ```bash
   sudo apt-get update
   sudo apt-get install -y mongodb
   ```
2. Start MongoDB by running:
   ```bash
   sudo systemctl start mongodb
   ```

3. Install MongoDB Compass (Optional)
MongoDB Compass is a graphical user interface for managing MongoDB databases. You can install it to interact with your MongoDB database more easily. Follow these steps to install MongoDB Compass:

For Windows:
Download MongoDB Compass from the official website: MongoDB Compass (https://www.mongodb.com/try/download/compass).
Run the installer and follow the installation steps.

For macOS:
Download MongoDB Compass from the official website: MongoDB Compass (https://www.mongodb.com/try/download/compass).
Open the downloaded .dmg file and drag MongoDB Compass to your Applications folder.

 3. Clone the Repository
Clone the Habit Tracker repository to your local machine:

```bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
```

 4. Install Dependencies
Use `pip` to install the required Python packages:

```bash
pip install Flask pymongo
```

 5. Configure MongoDB

- Make sure MongoDB is installed and running on your local machine or a server.
- Create a MongoDB database for the Habit Tracker application. MongoDB Compass can be used to connect and create database for the tracker, to do it follow the instructions below:
   1. Run application and in connection window type 'mongodb://localhost:27017/   (To connect to mongodb on your local machine, edit if port address is not default)
   2. Near “Databases” press button “+” to create a database.  

 6. Configure Application

Edit the `habit_tracker.py` file to configure the MongoDB connection and other application settings as needed:

```python
 Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']   
collection = db['habits']
```

Replace `'your_database_name'` with the name of your MongoDB database. 


Usage

To use the habit tracker, scroll down to that module in `habit_tracker.py`:
# 
# #  Using functionality
# 

Read committed text to choose function what you want to use. Uncommit and run all the code.
Longest Series of Habits and Total Number of Habits functions will be shown in simple API.





Arkadiy Kimiashov
OBJECT ORIENTED AND FUNCTIONAL PROGRAMMING WITH PYTHON
