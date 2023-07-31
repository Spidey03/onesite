import pytest

SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'


class TestUpdateSiteVisibilityResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_update_site_visibility_success_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'SITE_VISIBILITY_UPDATED_SUCCESSFULLY',
            'response': 'Site visibility updated successfully',
            'status_code': 200,
        }

        # Act
        response = presenter.update_site_visibility_success_response()

        # Arrange
        assert response == expected_response
