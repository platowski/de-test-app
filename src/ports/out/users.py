import abc

from ports.into.users import GetUsersPageDTO, UsersPageDTO


class UsersPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_users(self, dto: GetUsersPageDTO) -> UsersPageDTO:
        pass
