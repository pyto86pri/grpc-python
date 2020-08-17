from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection

from pb.helloworld_pb2 import DESCRIPTOR
from pb.helloworld_pb2_grpc import add_GreeterServicer_to_server

from app.greeter import GreeterServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(
        GreeterServicer(), server)
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()