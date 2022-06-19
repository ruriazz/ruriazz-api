from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.api_response import ApiResponse
from utils.decorators.authentication import is_developer

class OAuthView:

    @api_view(['POST'])
    @is_developer
    def main(request: Request) -> Response:
        return ApiResponse()