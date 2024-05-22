from django.conf import settings
from employ.grpc.protoc import connector_pb2, connector_pb2_grpc
import json
import traceback
import grpc

CHUNK_SIZE = 1024 * 1024  # 1MB


class ConnectorClient:
    def __init__(self, endpoint=None, channel=None, **kwargs):
        if channel is not None:
            self.channel = channel
        else:
            self.channel = grpc.insecure_channel(endpoint)
        self.stub = connector_pb2_grpc.ConnectorStub(self.channel)

    def execute(self, request_method, endpoint, payload=None, headers=None):
        try:
            response = self.stub.getResponse(
                self.__prepare_grpc_request(
                    request_method=request_method,
                    endpoint=endpoint,
                    payload=payload,
                    headers=headers,
                )
            )
            return response
        except Exception as e:
            traceback.print_exc()
            return None

    def __prepare_grpc_request(self, request_method, endpoint, payload, headers):
        return connector_pb2.GenericRequest(
            endpoint=endpoint,
            request_method=request_method,
            payload=json.dumps(payload) if payload is not None else None,
            headers=json.dumps(headers) if headers is not None else None,
        )
