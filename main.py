import os
import subprocess
import requests
import time

# Load environmental variables
ZROK_TOKEN = os.getenv('ZROK_TOKEN')
UPSTREAM_NAME = os.getenv('UPSTREAM_NAME')
DEPLOYMENT_URL = os.getenv('DEPLOYMENT_URL')


def publication_is_ready(attempts: int = 10):
    """
    Check if the deployment is ready to be published.
    :return: is_ready: bool
    """
    for i in range(attempts):
        try:
            if requests.get(f'{DEPLOYMENT_URL}/healthz').status_code == 200:
                print('Deployment available.')
                return True
        except Exception as e:
            print(e)
        print(f'Deployment unavailable. Attempt: {i + 1}/{attempts}.')
        time.sleep(3)
    print('Deployment unavailable. No more attempts.')
    return False


def publication_setup():
    """
    Enable zrok environment and reserve a domain name.
    :return:
    """
    # Enable zrok environment
    subprocess.run(['zrok', 'enable', ZROK_TOKEN, '-d', UPSTREAM_NAME])
    # Reserve a domain name
    subprocess.run(['zrok', 'reserve', 'public', DEPLOYMENT_URL, '-n', UPSTREAM_NAME])


def publication_publish():
    """
    Publishes the deployment.
    :return:
    """
    # Share the upstream
    subprocess.run(['zrok', 'share', 'reserved', UPSTREAM_NAME])


def main():
    if publication_is_ready():
        publication_setup()
        publication_publish()
        print(f'Publication finished. Access token: {UPSTREAM_NAME}.')
    else:
        print('Publication failed.')


if __name__ == '__main__':
    main()
