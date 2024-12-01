# Strava Lite
Author: Xiaoyu Sun

Email: xsun43@stevens.edu

Github repository link: https://github.com/qqqxs/Strava-Lite

## Introduction

Strava Lite is a basic server designed to help users track their runs. This project implements several APIs for user management, workout tracking, and basic social features.

## Features Overview

Strava Lite provides the following core functionalities:

1. **User Management**  
   - Register new users.
   - Retrieve user details.
   - Remove users.
   - List all users.

2. **Workout Management**  
   - Add workouts for users.
   - List all workouts for a specific user.

3. **Social Features**  
   - Follow other users.
   - View the workouts of friends being followed.


## API Documentation

### 1. **RegisterUser**
Registers a new user in the system.

- **Method**: `POST`  
- **Route**: `/user`  
- **Request Body**:
    ```json
    {
      "name": "string",
      "age": 0
    }
    ```
    - **`name`**: Required, string.
    - **`age`**: Optional, integer.
- **Response**:
    ```json
    {
      "id": "string",
      "name": "string",
      "age": 0
    }
    ```
  - `id` is a UUID generated on behalf of the user.

### 2. **GetUser**
Retrieves a user's details by their unique ID.

- **Method**: `GET`  
- **Route**: `/user/<user_id>`  
- **Request Body**: `{}`  
- **Response**:
    ```json
    {
      "id": "string",
      "name": "string",
      "age": 0
    }
    ```

### 3. **RemoveUser**
Removes a user by their ID.

- **Method**: `DELETE`  
- **Route**: `/user/<user_id>`  
- **Request Body**: `{}`  
- **Response**: `{}`

### 4. **ListUsers**
Lists all registered users.

- **Method**: `GET`  
- **Route**: `/users`  
- **Request Body**: `{}`  
- **Response**:
    ```json
    {
      "users": [
        {
          "id": "string",
          "name": "string",
          "age": 0
        }
      ]
    }
    ```

### 5. **AddWorkout**
Adds a workout for a user.

- **Method**: `PUT`  
- **Route**: `/workouts/<user_id>`  
- **Request Body**:
    ```json
    {
      "date": "string",
      "time": "string",
      "distance": "string"
    }
    ```
- **Response**:
    ```json
    {
      "date": "string",
      "time": "string",
      "distance": "string"
    }
    ```
    - **`date`**: Required, string.
    - **`time`**: Required, string.
    - **`distance`**: Required, string.

### 6. **ListWorkouts**
Lists all workouts for a specific user.

- **Method**: `GET`  
- **Route**: `/workouts/<user_id>`  
- **Request Body**: `{}`  
- **Response**:
    ```json
    {
      "workouts": [
        {
          "date": "string",
          "time": "string",
          "distance": "string"
        }
      ]
    }
    ```

### 7. **FollowFriend**
Allows users to follow other users.

- **Method**: `PUT`  
- **Route**: `/follow-list/<user_id>`  
- **Request Body**:
    ```json
    {
      "follow_id": "string"
    }
    ```
  - **`follow_id`**: Required, string, which is the ID of the user to follow.
- **Response**:
    ```json
    {
      "following": ["string"]
    }
    ```
  - Returns the list of IDs the user is following.

### 8. **ShowFriendWorkouts**
Lists the workouts of a friend, only if the user is following them.

- **Method**: `GET`  
- **Route**: `/follow-list/<user_id>/<follow_id>`  
- **Request Body**: `{}`  
- **Response**:
    ```json
    {
      "workouts": [
        {
          "date": "string",
          "time": "string",
          "distance": "string"
        }
      ]
    }
    ```
  - If the user is not following the friend, returns a status code `403`.


## Error Handling

- **400 Bad Request**: Missing required fields in the request body.
- **404 Not Found**: User or resource does not exist.
- **403 Forbidden**: Attempt to view friend workouts without following them.


## Deployment Environment

The following versions were used for environment setup in this project:

- **Python**: 3.8
- **Flask**: 3.0.3
- **Flask-RESTful**: 0.3.10
- **requests**: 2.32.3

## Setup and Execution

1. **Clone the repository**:
   Clone the project repository and navigate to the project directory:
   ```bash
   git clone https://github.com/qqqxs/Strava-Lite.git
   cd Strava-Lite
   ```

2. **Start the server**
   Run the app.py file to activate the server:
   ```bash
   python app.py
   ```

3. **Make requests to the server**
   You can use tools like Postman, curl, or even browser-based tools for GET requests. Below are some examples using curl to interact with the APIs.
- Register a new user
   ```bash
   curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30}'
   ```
- Get a user's information
   ```bash
   curl -X GET http://127.0.0.1:5000/user/<user_id>
   ```
- List all users
   ```bash
   curl -X GET http://127.0.0.1:5000/users
   ``` 
- Add a workout for a user
   ```bash
   curl -X PUT http://127.0.0.1:5000/workouts/<user_id> -H "Content-Type: application/json" -d '{"date": "2024-11-30", "time": "30:00", "distance": "5km"}'
   ``` 
- List all workouts for a user
   ```bash
   curl -X GET http://127.0.0.1:5000/workouts/<user_id>
   ```
- Follow another user
   ```bash
   curl -X PUT http://127.0.0.1:5000/follow-list/<user_id> -H "Content-Type: application/json" -d '{"follow_id": "<friend_id>"}'
   ```
- View a friend's workouts
   ```bash
   curl -X GET http://127.0.0.1:5000/follow-list/<user_id>/<friend_id>
   ```

   Once the server is running, you can execute the test.py script to automatically make requests and see the results of the APIs:
   ```bash
   python test.py
   ```

## Bugs and Issues
When implementing each API, it is essential to ensure that the output format strictly adheres to the specified requirements. Special attention should be given to handling cases where required parameters are missing, which should result in an appropriate error response. Additionally, while implementing the follower list, consideration must be given to whether the `set` data type is iterable.

## Resolved Issues
The output format was repeatedly refined to match the specified requirements, such as for `workout` and `user` responses. Furthermore, `try-except` blocks were added to handle scenarios where required parameters are not provided, ensuring the API returns an appropriate error. Finally, the follower list was converted from a `set` to a `list` to meet the iteration requirements.
