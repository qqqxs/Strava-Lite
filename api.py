from flask_restful import Resource, reqparse
from uuid import uuid4 as generateId

users = {}

create_user_parser = (reqparse.RequestParser()
                      .add_argument("name", type=str, required=True, help="Name is required and must be a string.")
                      .add_argument("age", type=int, required=False, help="Age is required and must be an integer."))


# Register User
class RegisterUser(Resource):
    def post(self):
        try:
            name, age = create_user_parser.parse_args().values()
        except Exception as e:
            return {"message": "Invalid request: required fields are missing or invalid."}, 400

        id = str(generateId())
        users[id] = {
            "id": id,
            "name": name,
            "age": age,
            "workouts": [],
            "following": set()
        }

        response_data = {key: users[id][key] for key in ("id", "name", "age")}
        return response_data, 200


# GET USER
class GetUser(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"message": "No user found"}, 404

        response_data = {key: user[key] for key in ("id", "name", "age")}
        return response_data, 200


# Remove User
class RemoveUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {}, 200
        return {"message": "No user found"}, 404


# List Users
class ListUsers(Resource):
    def get(self):
        response_data = {
            "users": [
                {key: user[key] for key in ("id", "name", "age")} for user in users.values()
            ]
        }
        return response_data, 200


add_workout_parser = (reqparse.RequestParser()
                      .add_argument("date", type=str, required=True, help="Date is required and must be a string.")
                      .add_argument("distance", type=str, required=True, help="Distance is required and must be a string.")
                      .add_argument("time", type=str, required=True, help="Time is required and must be a string."))


# Add Workout
class AddWorkout(Resource):
    def put(self, user_id):
        try:
            date, time, distance = add_workout_parser.parse_args().values()
        except Exception as e:
            return {"message": "Invalid request: required fields are missing or invalid."}, 400

        user = users.get(user_id)
        if user is None:
            return {"message": "No user found"}, 404

        workout = {"date": date, "distance": distance, "time": time}
        user["workouts"].append(workout)

        return workout, 200


# List Workouts
class ListWorkouts(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"message": "No user found"}, 404

        response_data = {"workouts": user["workouts"]}
        return response_data, 200


add_follow_friend_parser = (reqparse.RequestParser()
                            .add_argument("follow_id", type=str, required=True,
                                          help="Follow_id is required and must be a string."))


# Follow Friend
class FollowFriend(Resource):
    def put(self, user_id):
        try:
            args = add_follow_friend_parser.parse_args()
            follow_id = args.get("follow_id")
        except Exception as e:
            return {"message": "Invalid request: required fields are missing or invalid."}, 400

        user = users.get(user_id)
        follower = users.get(follow_id)
        # if user is None or following is None:
        #     return {"message": "No user found"}, 404
        if user_id == follow_id:
            return {"message": "Do not follow yourself"}, 404
        elif user is None or follower is None:
            return {"message": "User not found"}, 404

        user['following'].add(follower['id'])
        response_data = {"following": list(user["following"])}
        return response_data, 200


# Show Friend Workouts
class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        user = users.get(user_id)
        follower = users.get(follow_id)
        if user is None or follower is None:
            return {"message": "User not found"}, 404

        if follow_id not in user['following']:
            return {"message": "You are not currently following this user."}, 403

        response_data = {"workouts": follower["workouts"]}
        return response_data, 200
