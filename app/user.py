"""
UserServiceServicer の実装．
"""
from pb.user_pb2 import User as UserResponse
from pb.user_pb2_grpc import UserServiceServicer as IUserServiceServicer
from ..domain.model.user.user import UserId, User
from ..domain.model.user.user_repository import IUserRepository


class UserServiceServicer(IUserServiceServicer):
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def GetUser(self, request, context):
        user = self._repository.get(UserId(request.id))
        return UserResponse(id=user.id_, name=user.name)

    def CreateUser(self, request, context):
        user = User(
            self._repository.nextId(),
            request.name
        )
        self._repository.save(user)
        return UserResponse(id=user.id_, name=user.name)

    def UpdateUser(self, request, context):
        user = self._repository.get(UserId(request.id))
        user.updateName(request.name)
        self._repository.save(user)
        return UserResponse(id=user.id_, name=user.name)

    def DeleteUser(self, request, context):
        user = self._repository.delete(UserId(request.id))
        return UserResponse(id=user.id_, name=user.name)

    def ListUsers(self, request, context):
        for user in self._repository.list_():
            yield UserResponse(id=user.id_, name=user.name)
