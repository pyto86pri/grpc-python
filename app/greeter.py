from pb.helloworld_pb2 import HelloReply
from pb.helloworld_pb2_grpc import GreeterServicer as IGreeterServicer


class GreeterServicer(IGreeterServicer):
    def SayHello(self, request, context):  # type: ignore
        return HelloReply(message=f"Hello, {request.name}!")
