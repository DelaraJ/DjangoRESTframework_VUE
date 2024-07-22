# Project Documentation

## Project Overview

### Project Name

**Personal Information Manager**

### Description

This Personal Information Manager is a web application designed to collect and manage personal data using Django Rest Framework as the backend and Vue.js for the frontend interface. The application allows users to enter their name, surname, contact number, age, and gender through a form, storing this data in a database. Users can view all surname entries and edit only the most recent entry.

### Technologies Used

- **Backend**: Django Rest Framework
- **Frontend**: Vue.js
- **Environment**: Python Virtual Environment

## Installation and Setup

### Prerequisites

- Python 3.x
    - we need pip too but pip is usually included automatically when installing Python on Windows.
- Virtualenv
- Django REST framework
- Django CORS headers
    - This package provides a way to configure your Django application to allow requests from different origins.
- Node.js and npm
- Axois
    - This will be used to communicate with the backend.
- Bulma
    - This is the CSS framework I used to make it easier to create a nice interface

### Backend Setup

1. **Create a virtual environment and activate it:**
    
    ```bash
    virtualenv vueango_3_10_7 #The numbers represent the version of Python that we are using
    vueango_3_10_7\Scripts\activate
    ```
    
2. **Install backend dependencies:**
    
    ```bash
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
    ```
    
3. **Create the Django Project**
    
    ```bash
     django-admin startproject vueango
    ```
    
4. **Create a superuser for the admin interface**
    
    ```bash
    cd vueango
    python mnage.py createsuperuser
    ```
    
5. **Run database migrations:**
    
    ```bash
    python manage.py migrate
    ```
    
6. **Start the Django server:**
    
    ```bash
    python manage.py runserver
    ```
    

### Frontend Setup

1. **Navigate to the frontend directory:**
    
    ```bash
    cd Vue
    ```
    
2. **Install frontend dependencies:**
    
    ```bash
    npm install
    npm install axios
    npm install bulma
    ```
    
3. **Create the Vue Project**
    
    ```bash
    vue create vueango
    ```
    
4. **Compile and hot-reload for development:**
    
    ```bash
    npm run serve
    ```
    

## Application Features

- **Data Collection**: Users can input their name, surname, contact number, age, and gender through a form.
- **Data Storage**: Information is stored in a relational database managed by Django.
- **View Entries**: Users can view all the surnames that have been entered.
- **Edit Functionality**: Users can only edit the information of the most recently added entry that they have submitted.

## Project Structure

```ruby
project-root/
├── backend/
│   ├── manage.py
│   ├── <app_name>/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   └── ...
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   └── App.vue
│   └── ...
└── README.md

```

## API Endpoints

### Get All Entries

- **Endpoint**: `/members/`
- **Method**: GET
- **Description**: Retrieve a list of all entries, including name, surname, contact number, age, and gender.
    - The application will display all information at the local server URL: [http://127.0.0.1:8000/members/](http://127.0.0.1:8000/members/), which allows for API access. In contrast, the front-end application will present only the surnames at [http://localhost:8080/](http://localhost:8080/).

### Add New Entry

- **Endpoint**: `/members/`
- **Method**: POST
- **Description**: Add a new entry to the database with fields for name, surname, contact number, age, and gender.

### Edit The Entries

- **Endpoint**: `/members/{member_id}/`
- **Method**: PUT
- **Description**: Edit the entry in the database.

## Frontend Components

- **Form Component**: A Vue.js component that handles user input and form submission.
- **Entry List Component**: Displays all surname entries, highlighting the most recent entry.
- **Edit Form Component**: Allows users to edit the latest entry that they have submitted.

## Deployment

Instructions for deploying the application will be provided based on the chosen hosting environment.

## Contact

For any inquiries, please contact me, Delara Jalali, at delara.jalali.382@gmail.com.
