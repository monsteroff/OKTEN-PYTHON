from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):

    def post(self, request):
        return Response('Method POST')

    def get(self, request):
        return Response('Method GET')

    def put(self, request):
        return Response('Method PUT')

    def patch(self, request):
        return Response('Method PATCH')

    def delete(self, request):
        return Response('Method DELETE')


class SecondView(APIView):
    def get(self, *args, **kwargs):
        # localhost:8000/second?name='Cahangir'&age=28
        params = self.request.query_params.dict()
        print(params)
        return Response(params)


class ThirdView(APIView):
    def get(self, *args, **kwargs):
        # localhost:8000/third/Cahangir/28
        params = kwargs
        print(params)
        return Response(params)


class FourthView(APIView):
    def post(self, *args, **kwargs):
        # post eleyirik  # localhost:8000/fourth
        # {"name":"Orxan","age":"28"}
        params = self.request.data
        print(params)
        return Response(params)

