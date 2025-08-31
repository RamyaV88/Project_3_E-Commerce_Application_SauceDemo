import pytest

from utilities.ReadConfigurations import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    problem_user = ReadConfig.get_problem_user()
    performance_glitch_user = ReadConfig.get_performance_glitch_user()
    locked_out_user = ReadConfig.get_locked_out_user()
    visual_user = ReadConfig.get_visual_user()
    error_user = ReadConfig.get_error_user()
    logger = LogGen.loggen()
