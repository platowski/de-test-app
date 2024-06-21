import abc

from ports.into.users import UserDTO


class UsersPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_users(self) -> list[UserDTO]:
        pass
