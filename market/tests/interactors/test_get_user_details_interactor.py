from unittest.mock import create_autospec

import pytest

USER_ID = "d32b2f96-93f5-4e2f-842d-d590783dcfed"


class TestGetUserDetailsInteractor:

    @pytest.fixture
    def storage(self):
        from market.interactors.storages.user_storages_interface import UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def user_details_dto(self):
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory
        from market.tests.common_fixtures.reset_sequence import reset

        reset()
        return UserDetailsDTOFactory(id=USER_ID)

    @pytest.fixture
    def expected_response(self):
        return

    def test_user_not_found(self, storage, presenter):
        # Arrange
        from market.exceptions.exceptions import UserNotFoundException

        presenter_expected_response = {
            'res_status': 'USER_NOT_FOUND_EXCEPTION',
            'response': f'User not found with id: {USER_ID}',
            'status_code': 400
        }
        storage.get_user.side_effect = UserNotFoundException
        presenter.get_user_not_found_response.return_value = presenter_expected_response

        from market.interactors.get_user_details import GetUserDetailsInteractor
        interactor = GetUserDetailsInteractor(
            storage=storage
        )

        # Act
        response = interactor.get_user_details_wrapper(
            user_id=USER_ID,
            presenter=presenter
        )

        # Assert
        assert response == presenter_expected_response

    def test_get_user_details(self, storage, presenter, user_details_dto):
        # Arrange

        presenter_expected_response = {
            'user_id': 'd32b2f96-93f5-4e2f-842d-d590783dcfed',
            'first_name': 'Robert',
            'middle_name': '',
            'last_name': '',
            'email': 'robert321@gmail.com',
            'mobile_number': '9676767209',
            'joined_at': '2022-03-04 00:00:00',
        }
        storage.get_user.return_value = user_details_dto
        presenter.get_user_details.return_value = presenter_expected_response

        from market.interactors.get_user_details import GetUserDetailsInteractor
        interactor = GetUserDetailsInteractor(
            storage=storage
        )

        # Act
        response = interactor.get_user_details_wrapper(
            user_id=USER_ID,
            presenter=presenter
        )

        # Assert
        assert response == presenter_expected_response