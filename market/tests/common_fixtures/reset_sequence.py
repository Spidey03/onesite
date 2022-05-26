def reset():
    reset_model_factories()
    reset_dto_factories()


def reset_model_factories():
    from market.tests.common_fixtures.model_factories import (
        UserModelFactory,
        SiteModelFactory,
    )

    UserModelFactory.reset_sequence(0)
    SiteModelFactory.reset_sequence(0)


def reset_dto_factories():
    from market.tests.common_fixtures.factories import (
        UserDTOFactory,
        UserDetailsDTOFactory,
        AddUserDetailsDTOFactory,
        SiteDTOFactory,
        LoginUserDTOFactory,
    )

    UserDTOFactory.reset_sequence(0)
    UserDetailsDTOFactory.reset_sequence(0, force=True)
    AddUserDetailsDTOFactory.reset_sequence(0, force=True)
    SiteDTOFactory.reset_sequence(0)
    LoginUserDTOFactory.reset_sequence(0)
