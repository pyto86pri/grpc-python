from pb.helloworld_pb2 import HelloRequest, HelloReply
from pb.helloworld_pb2_grpc import GreeterServicer as IGreeterServicer


class GreeterServicer(IGreeterServicer):

    def SayHello(self, request, context):
        return HelloReply(message=f'Hello, {request.name}!')
