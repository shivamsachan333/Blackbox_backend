
from django.middleware.common import CommonMiddleware

class AllowAnyOriginMiddleware(CommonMiddleware):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        return super().process_response(request, response)