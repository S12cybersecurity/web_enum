import re
import json
import time
import random
import warnings
import requests

import src.config

warnings.filterwarnings('ignore') # Disable SSL related warnings

def requester(url, data, headers, GET, delay):
    if src.config.globalVariables['jsonData']:
        data = json.dumps(data)
    if src.config.globalVariables['stable']:
        delay = random.choice(range(6, 12))
    time.sleep(delay)
    headers['Host'] = re.search(r'https?://([^/]+)', url).group(1)
    if GET:
        response = requests.get(url, params=data, headers=headers, verify=False)
    elif src.config.globalVariables['jsonData']:
        response = requests.post(url, json=data, headers=headers, verify=False)
    else:
        response = requests.post(url, data=data, headers=headers, verify=False)
    return response
