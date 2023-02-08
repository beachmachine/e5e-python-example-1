from __future__ import print_function, unicode_literals

import os
import sys
import subprocess

import requests


def myfunction(event, context):
    print("Print line 1")
    print("Print line 2")
    print("Print line 3")

    try:
        a, b = event['data']['a'], event['data']['b']
    except Exception:
        a, b = 0, 0

    try:
        ip_local = subprocess.Popen('ip addr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    except Exception:
        ip_local = 'ERROR: Cannot call `ip addr`'

    try:
        ip_remote = requests.get('https://ip.anexia.com', headers={
            'user-agent': 'curl/7.68.0',
        }).text
    except Exception:
        ip_remote = 'ERROR: No connection to `https://ip.anexia.com`'

    try:
        resolve = open('/etc/resolv.conf', 'r').read()
    except Exception:
        resolve = 'ERROR: Could not read `/etc/resolv.conf`'

    try:
        hosts = open('/etc/hosts', 'r').read()
    except Exception:
        hosts = 'ERROR: Could not read `/etc/hosts`'

    return {
        'status': 202,
        'response_headers': {
            'x-custom-response-header-1': 'This is a custom response header 1',
            'x-custom-response-header-2': 'This is a custom response header 2',
            'x-custom-response-header-3': 'This is a custom response header 3',
        },
        'data': {
            'sum': a + b,
            'version': sys.version,
            'event': event,
            'context': context,
            'ip_local': ip_local,
            'ip_remote': ip_remote,
            'resolve': resolve,
            'hosts': hosts,
            'environment': dict(os.environ),
        },
    }

