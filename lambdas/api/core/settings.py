import os

from aws_utils.ssm import get_ssm_parameter


APP_NAME = 'classifier'

ENVIRONMENT = os.getenv('environment')

DATABASE = {
    'NAME': get_ssm_parameter(f'/{APP_NAME}/{ENVIRONMENT}/DATABASE_NAME/'),
    'USER': get_ssm_parameter(f'/{APP_NAME}/{ENVIRONMENT}/DATABASE_USER/'),
    'PASSWORD': get_ssm_parameter(f'{APP_NAME}/{ENVIRONMENT}/DATABASE_PASSWORD/'),
    'HOST': get_ssm_parameter(f'/{APP_NAME}/{ENVIRONMENT}/DATABASE_HOST/'),
    'PORT': get_ssm_parameter(f'/{APP_NAME}/{ENVIRONMENT}/DATABASE_PORT/')
}
