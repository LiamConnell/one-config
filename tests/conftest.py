import one_config


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    one_config.build_config().from_yaml('configs/test.yaml')
    print()