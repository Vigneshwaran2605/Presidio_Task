# Flight Ticket Booking(AEROBOOK)

This project is developed by using Django as backend and HTML as frontend. Django files are stored in backend/users/ and HTML files are stored in the backend/users/templates. My output is recorded and uploaded in https://drive.google.com/drive/folders/1bgGXO0WhqrNsTdHHkuB46pixG0xhVLQE?usp=sharing

# To run this project in local server, follow the given steps:-

1. Download the project by using command "git clone https://github.com/Vigneshwaran2605/Presidio_Task.git".
2. Install Django by using the command "pip install django".
3. Run the Django server with 'python manage.py runserver' command from the Project1\backend folder.
4. The project runs on http://127.0.0.1:8000/ in your browser.

# Problem Statement:-

# Console-Based Flight Ticket Booking Application

Optional: Database: MySQL or any other of your choice
Types of Users: User and Admin

1. User Use Cases:
- Login: Users should be able to log in, and the application should check credentials with the database or local storage (list or array).
- Signup: Implement a signup feature to add new users to the database or an array.
- Search Flight: Users should be able to search for flights using Flight name/ Date/ Flight Number
- Book Tickets: Allow users to book tickets based on availability, assuming the default seat count is 60 for all flights.

2.Admin Use Cases:
- Login: Admins should be able to log in.
- Add Flights: Admins should have the ability to add new flights to the system.
- View Bookings: Admins should be able to view bookings with the option to filter based on: Flight ID/Flight Name/ Date

# Features of the Flight Ticket Booking(AEROBOOK):-

1. Login Page -> Enter username and password for sigin and there is seperate login for admin.
2. Signup Page -> Enter details to register account.
3. Logout -> Signout from the account.

## User Side

1. Search Flight -> Search the flight by date and time
2. Book Flight -> Book the flight by search with date and time and check if there is availability of seats
3. My Bookings -> Show the list of all bookings made by user.
4. Show Flight -> Show the list of all available flights.
5. Cancel Flight -> Cancel the booked ticket by entering booking ID.

## Admin Side

1. Add Flight -> Add Flight by entering date,time and seat availability.
2. Remove Flight -> Remove Flight by entering Flight ID.
3. View Bookings -> View all the bookings made to the specific Flight ID , it list as the username and seats booked.
4. Show Flight -> Show the list of all the flights.

## Updated
1. Multiple Ticket Booking
2. Search by From & To locations.

# OUTPUT IMAGES

## Home Page
![HomePage](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/d438537e-7f8a-4944-9646-84a49468ef51)
![Register Login](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/11ede541-60e7-4fa9-895c-c2fd0e35c478)

## User Home
![User_home](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/0733f89b-80bc-4135-8125-409f1cfe65f0)
## User Functions
![User_function](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/ca84eddc-1429-4183-b567-0c2802196512)

## Admin Home
![Admin_Home](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/0d211816-da05-497a-b483-33388ff74cf8)
## Admin Functions
![Admin_function](https://github.com/Vigneshwaran2605/Presidio_Task/assets/91144302/76162339-9096-4883-9fd0-99bb063a90cd)



