import asyncio
import logging

from grpc.experimental import aio
from grpc_reflection.v1alpha import reflection

from pb.helloworld_pb2 import DESCRIPTOR
from pb.helloworld_pb2_grpc import add_GreeterServicer_to_server

from app.greeter import GreeterServicer


async def serve():
    server = aio.server()
    add_GreeterServicer_to_server(
        GreeterServicer(), server)
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    loop = asyncio.get_event_loop()
    loop.create_task(serve())
    loop.run_forever()