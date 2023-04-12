import http

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializer import serialize_data
from api.utils.operation_bd import update_bd as update


# Create your views here.
#
# {
#     "user_email": "test",
#     "categories_cards": [
#         {
#             "name": "categoriesOne",
#             "serverCategoryId":0,
#             "createdAt":0,
#             "modifiedAt":0,
#             "cards": [
#                 {
#                     "name": "cardsOne"
#                     "serverCardId": 0,
#                     "categoryId": 0,
#                     "colorStart": 0,
#                     "colorEnd": 0,
#                     "countOpen": 0,
#                     "cardBaseInfo": "",
#                     "cardSecondInfo": "",
#                     "typeBase": 0,
#                     "valueBase": 0,
#                     "existSecondary": false,
#                     "typeSecondary": 0,
#                     "valueSecondary": 0,
#                     "createdAt":0,
#                     "modifiedAt":0,
#                 }
#             ]
#         },
#         {
#             "name": "categoriestwo",
#             "serverCategoryId":0,
#             "createdAt":0,
#             "modifiedAt":0,
#             "cards": [
#                 {
#                     "name": "cardsTwo"
#                     "serverCardId": 0,
#                     "categoryId": 0,
#                     "colorStart": 0,
#                     "colorEnd": 0,
#                     "countOpen": 0,
#                     "cardBaseInfo": "",
#                     "cardSecondInfo": "",
#                     "typeBase": 0,
#                     "valueBase": 0,
#                     "existSecondary": false,
#                     "typeSecondary": 0,
#                     "valueSecondary": 0,
#                     "createdAt":0,
#                     "modifiedAt":0,
#                 }
#             ]
#         }
#     ]
# }
# http://127.0.0.1:8000/api/update_bd
@api_view(['POST', ])
def update_bd(request):
    if request.method == "POST":
        user_app = request.data['user_email']
        categories_client = serialize_data(request.data['categories_cards'])
        data = update(categories_client, user_app)

        return create_response(status_code=status.HTTP_200_OK,
                               message="BD is update")


def create_response(status_code, message='', result=None):
    """
    function  to create default Response
        :param result: data
        :param status_code: int - status code Response
        :param message: string - information
        :return: default response
    """
    _status = ''
    _status = http.HTTPStatus(status_code)

    if result is None:
        result = []
    response_result = {
        "message": message,
        "data": result
    }

    del result,
    return Response(response_result, status=_status)
