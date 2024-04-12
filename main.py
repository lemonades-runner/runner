import os
import subprocess

# Load environmental variables
ZROK_TOKEN = os.getenv('ZROK_TOKEN')
UPSTREAM_NAME = os.getenv('UPSTREAM_NAME')

# Enable zrok environment
subprocess.run(['zrok', 'enable', ZROK_TOKEN, '-d', UPSTREAM_NAME])

# Reserve a domain name
subprocess.run(['zrok', 'reserve', 'public', 'deployment:8001', '-n', UPSTREAM_NAME])

# Share the upstream
subprocess.run(['zrok', 'share', 'reserved', UPSTREAM_NAME])
