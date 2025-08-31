import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('basic info', 'url')
        return url

    @staticmethod
    def get_username():
        username = config.get('basic info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('basic info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('basic info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_problem_user():
        problem_user = config.get('basic info', 'problem_user')
        return problem_user

    @staticmethod
    def get_performance_glitch_user():
        performance_glitch_user = config.get('basic info', 'performance_glitch_user')
        return performance_glitch_user

    @staticmethod
    def get_error_user():
        error_user = config.get('basic info', 'error_user')
        return error_user

    @staticmethod
    def get_visual_user():
        visual_user = config.get('basic info', 'visual_user')
        return visual_user

    @staticmethod
    def get_locked_out_user():
        locked_out_user = config.get('basic info', 'locked_out_user')
        return locked_out_user
