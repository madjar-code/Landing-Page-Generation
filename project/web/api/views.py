from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_something(request):
    return Response(data={'msg': 'some message'})