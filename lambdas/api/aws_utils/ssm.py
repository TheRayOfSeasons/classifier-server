import boto3


SSM_CLIENT = boto3.client('ssm')


def get_ssm_parameter(name, decryption=True):
    """
    A generic function that will get a parameter on Amazon Systems
    Manager Agent(SSM) based on parameter name.

    How to use:
    value = get_parameter_from_ssm(name='/value/staging')
    """
    try:
        parameter = SSM_CLIENT.get_parameter(
            Name=str(name),
            WithDecryption=decryption
        )
        return parameter['Parameter']['Value']
    except Exception as e:
        logging.error('Failed to get the parameter from SSM.')
        raise e
