from market.exceptions.exceptions import UserNotFoundException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class DeleteUserInteractor(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def delete_user_wrapper(
            self,
            user_id: str,
            presenter: PresenterInterface
    ):
        try:
            self._delete_user(user_id=user_id)
            return presenter.user_deleted_successfully_response()
        except UserNotFoundException:
            return presenter.get_user_not_found_response(user_id=user_id)

    def _delete_user(self, user_id: str):
        if not self.user_storage.check_user_exists(user_id=user_id):
            raise UserNotFoundException()
        self.user_storage.delete_user(user_id=user_id)
