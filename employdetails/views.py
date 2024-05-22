import json
from rest_framework import viewsets
from .models import MyModel
from rest_framework.response import Response
from rest_framework import status
from employ.grpc.client import ConnectorClient
from rest_framework.views import APIView
from django.conf import settings
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer



class DemoListView(APIView):
    def get(self, request):
        auth_grpc_connector_client = ConnectorClient(
                    channel=settings.PF_AUTH_GRPC_CHANNEL
                )
        introspect_endpoint = f'/apis/v1.0.0/mymodels/'
        validator_response = auth_grpc_connector_client.execute(
            request_method="GET",
            endpoint=introspect_endpoint,
            # headers={
            #     "Authorization": f"Bearer {self.context.get('request')._auth}"
            # },
        )
        return Response({'data': json.loads(validator_response.data)}, status=validator_response.status_code)

