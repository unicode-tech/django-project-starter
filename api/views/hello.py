from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView


class HelloView(APIView):

    def get(self, request, *args, **kwargs):

        return Response(
            {
                'hello': 'world'
            },
            status=HTTPStatus.OK
        )