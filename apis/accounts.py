from flask_restx import Namespace, Resource

api = Namespace(
    name="accounts",
    description="Operations related to account management like login and signup",
)


@api.route("/signup")
class Signup(Resource):
    def post(self):
        pass


@api.route("/login")
class Login(Resource):
    def post(self):
        pass
