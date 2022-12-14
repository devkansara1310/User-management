from drf_yasg import openapi

class RegistrationSchema:
    auto_schema = {
        "operation_id": "registration",
        "responses": {
            "200": openapi.Response(
                description="User Registration API.",
                examples={
                    "application/json": [
                        {
                            "code":"1",
                            "data": {
                                "username":"dev_kansara",
                                "email":"dev@gmail.com",
                                "name":"Dev Kansara",
                                "image":"/media/media/profile/profile_1.jpg",
                                "is_blocked":'false'
                            }
                        },
                        {"code": '0',"data": {'username':'A user with that username already exists.'}},
                        {"code": '0',"data": {'username':'A user with that username already exists.'}},
                        {"code": '0',"data": {'username':'A user with that username already exists.'}},
                    ]
                },
            )
        },
        "manual_parameters": [openapi.Parameter("image", openapi.TYPE_OBJECT, type=openapi.TYPE_FILE, required=True)],
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="User name"),
                "email": openapi.Schema(type=openapi.FORMAT_EMAIL, description="Email ID"),
                "password": openapi.Schema(type=openapi.FORMAT_PASSWORD, description="Password"),
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Full Name"),
            },
            required=["username", "password","email"],
        ),
        "tags": ["Registration"],
    }

class LoginSchema:
    auto_schema = {
        "operation_id": "authentication",
        "responses": {
            "200": openapi.Response(
                description="Login API.",
                examples={
                    "application/json": [
                        {
                            "code": 1,
                            "data": {"token":"d3fwef4w5efe444fdsf1s3e53555695dsegsdcxss6532"}
                        },
                    ]
                },
            )
        },
        "manual_parameters": [],
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=[openapi.TYPE_STRING, '|',openapi.FORMAT_EMAIL], description="User name or Email id."),
                "password": openapi.Schema(type=openapi.FORMAT_PASSWORD, description="Password"),
            },
            required=["username", "password"],
        ),
        "tags": ["Authentication"],
    }

class LogoutSchema:
    auto_schema = {
        "operation_id": "signout",
        "responses": {
            "200": openapi.Response(
                description="Logout API.",
                examples={
                    "application/json": [
                        {
                            "code": 1,
                            "data": {"token":"d3fwef4w5efe444fdsf1s3e53555695dsegsdcxss6532"}
                        },
                    ]
                },
            )
        },
        "manual_parameters": [],
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={},
            required=[],
        ),
        "tags": ["Authentication"],
    }

class UsersSchema:
    auto_schema = {
        "operation_id": "Users",
        "responses": {
            "200": openapi.Response(
                description="Listing of all users API.",
                examples={
                    "application/json": [
                        {
                            "code": 1,
                            "data": [
                                {
                                    "username": "admin",
                                    "email": "admin@gmail.com",
                                    "name": "Admin",
                                    "image": "media/profile/profile_1.jpg",
                                    "is_blocked": False,
                                },
                                {
                                    "username": "dev_kansara",
                                    "email": "dev@gmail.com",
                                    "name": "Dev Kansara",
                                    "image": "media/profile/profile_1.jpg",
                                    "is_blocked": False,
                                },
                                {
                                    "username": "test_user",
                                    "email": "test@gmail.com",
                                    "name": "Test User",
                                    "image": "media/profile/profile_1.jpg",
                                    "is_blocked": False,
                                },
                            ]
                        },
                    ]
                },
            )
        },
        "manual_parameters": [openapi.Parameter("key", openapi.IN_HEADER, type=openapi.TYPE_STRING, required=True)],
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={},
            required=[],
        ),
        "tags": ["Users"],
    }

class UpdateUserProfileSchema:
    auto_schema = {
        "operation_id": "update user-profile",
        "responses": {
            "200": openapi.Response(
                description="Update user profile API.",
                examples={
                    "application/json": [
                        {
                            "code":"1",
                            "data": {
                                "username":"dev_kansara",
                                "email":"dev@gmail.com",
                                "name":"Dev Kansara",
                                "image":"/media/media/profile/profile_1.jpg",
                                "is_blocked":'false'
                            }
                        },
                        {"code": '0',"data": {'username':["A user with that username already exists."]}},
                        {"code": '0',"data": {"email": ["This field must be unique."]}},
                    ]
                },
            )
        },
        "manual_parameters": [openapi.Parameter("image", openapi.TYPE_OBJECT, type=openapi.TYPE_FILE, required=True)],
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="User name"),
                "email": openapi.Schema(type=openapi.FORMAT_EMAIL, description="Email id"),
                "password": openapi.Schema(type=openapi.FORMAT_PASSWORD, description="Password"),
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Name"),
            },
            required=[],
        ),
        "tags": ["Users"],
    }
