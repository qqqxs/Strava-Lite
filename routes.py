from flask_restful import Api
from constants import *
from api import *

BASE_ROUTE = "/user"
USER_ID_ROUTE = f"{BASE_ROUTE}/<string:user_id>"
FOLLOW_ID_ROUTE = "/follow-list/<string:user_id>"

ROUTES = {
    REGISTER_USER: BASE_ROUTE,
    GET_USER: USER_ID_ROUTE,
    REMOVE_USER: USER_ID_ROUTE,
    LIST_USERS: "/users",
    ADD_WORKOUT: "/workouts/<string:user_id>",
    LIST_WORKOUTS: "/workouts/<string:user_id>",
    FOLLOW_FRIEND: FOLLOW_ID_ROUTE,
    SHOW_FRIEND_WORKOUTS: f"{FOLLOW_ID_ROUTE}/<string:follow_id>"
}

METHODS = {
    REGISTER_USER: "POST",
    GET_USER: "GET",
    REMOVE_USER: "DELETE",
    LIST_USERS: "GET",
    ADD_WORKOUT: "PUT",
    LIST_WORKOUTS: "GET",
    FOLLOW_FRIEND: "PUT",
    SHOW_FRIEND_WORKOUTS: "GET"
}

RESOURCES = {
    REGISTER_USER: RegisterUser,
    GET_USER: GetUser,
    REMOVE_USER: RemoveUser,
    LIST_USERS: ListUsers,
    ADD_WORKOUT: AddWorkout,
    LIST_WORKOUTS: ListWorkouts,
    FOLLOW_FRIEND: FollowFriend,
    SHOW_FRIEND_WORKOUTS: ShowFriendWorkouts
}


def init_routes(api: Api) -> None:
    for [api_name, resource] in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])
