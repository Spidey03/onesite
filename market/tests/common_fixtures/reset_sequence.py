def reset():
    reset_model_factories()
    reset_dto_factories()


def reset_model_factories():
    from market.tests.common_fixtures.model_factories import UserModelFactory
    from market.tests.common_fixtures.model_factories import SiteModelFactory

    UserModelFactory.reset_sequence(0)
    SiteModelFactory.reset_sequence(0)


def reset_dto_factories():
    from market.tests.common_fixtures.factories import UserDetailsDTOFactory
    from market.tests.common_fixtures.factories import SiteDTOFactory

    UserDetailsDTOFactory.reset_sequence(0)
    SiteDTOFactory.reset_sequence(0)
