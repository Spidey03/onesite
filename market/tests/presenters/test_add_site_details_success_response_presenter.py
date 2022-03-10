import pytest

from market.tests.common_fixtures.reset_sequence import reset

SITE_ID = "d32b2f96-93f5-4e2f-842d-d590783dd001"


class TestAddSiteResponsePresenter:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    def test_add_site_success_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'SITE_ADDED_SUCCESSFULLY',
             'response': 'Site added successfully',
             'status_code': 201
        }

        # Act
        response = presenter.add_site_details_success_response()

        # Arrange
        assert response == expected_response
