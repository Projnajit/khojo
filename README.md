# Khojo House Rental App (Django)

Welcome to the Khojo House Rental App! This repository contains the source code for a web application built using Django framework. The Khojo House Rental App allows users to search and rent houses in their desired location.

## Features

- User Registration and Authentication: Users can create accounts and authenticate themselves to access the features of the application.
- House Search: Users can search for available houses based on their desired location, budget, and other preferences.
- House Listings: House owners can list their properties, including details such as location, price, amenities, and contact information.
- House Rental Requests: Users can submit rental requests for houses they are interested in, which are then sent to the house owners.
- Notifications: Users receive notifications regarding the status of their rental requests, such as approval, rejection, or updates.
- User Dashboard: Users have a personalized dashboard where they can manage their profile, view their rental history, and track the status of their requests.

## Installation

To run the Khojo House Rental App locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Projnajit/khojo.git
   ```

2. Navigate to the project directory:

   ```
   cd khojo-
   ```

3. Create a virtual environment:

   ```
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source env/bin/activate
     ```

5. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Access the application by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser.

Note: Make sure you have Python and Django installed on your machine before proceeding with the installation.

## Usage

Once you have the application up and running, you can perform the following tasks:

- Create a new account or log in with an existing account.
- Search for available houses by specifying location, budget, and other preferences.
- View detailed information about a specific house, including its amenities and contact information.
- Submit rental requests for houses you are interested in.
- Manage your profile and update your contact information.
- Track the status of your rental requests in your personalized dashboard.
- House owners can list their properties by providing all the necessary details.
