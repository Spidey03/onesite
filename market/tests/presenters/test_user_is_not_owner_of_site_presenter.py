import pytest

SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'
USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd002'


class TestUserIsNotOwnerOfSiteResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_user_is_not_owner_of_site(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_NOT_OWNER',
            'response': f'User {USER_ID} is not the owner of the site {SITE_ID}',
            'status_code': 400,
        }

        # Act
        response = presenter.user_is_not_owner_of_site(site_id=SITE_ID, user_id=USER_ID)

        # Arrange
        assert response == expected_response
