from employ.grpc.protoc import connector_pb2_grpc
from employ.grpc.servicers import ConnectorServicer


def connector_hook(server):
    connector_pb2_grpc.add_ConnectorServicer_to_server(ConnectorServicer(), server)
