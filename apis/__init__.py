from flask_restx import Api

from .accounts import api as accounts

api = Api(
    title="pucon_apis",
    version="1.0",
    description="All the namespaces having the respective routes to be added in the api",
)

api.add_namespace(accounts)
