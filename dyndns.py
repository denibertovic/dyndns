import urllib2
import sys
import logging
from linode import api

CACHE_FILE = 'ip.cache'

logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', filename='dyndns.log', level=logging.INFO)

try:
    from config import LINODE_API_KEY, DOMAIN_ID, RESOURCE_ID, IP_SERVICE
except ImportError as e:
    logging.error(e)
    print 'MISSING CONFIG! Please see config.py.example for how to configure this script.'
    sys.exit(1)

linode = api.Api(LINODE_API_KEY)

ip = urllib2.urlopen(IP_SERVICE).read()

try:
    with open(CACHE_FILE) as f:
        old_ip = f.readline().strip().split('=')[1]
        if ip == old_ip:
            print 'IP did not change. Exiting!'
            sys.exit(0)
        else:
            f.write('IP={}'.format(ip))
except IOError:
    with open(CACHE_FILE, 'w') as f:
        f.write('IP={}'.format(ip))

try:
    ret = linode.domain_resource_update(DomainID=DOMAIN_ID, ResourceID=RESOURCE_ID, Target=ip)
    logging.info(ret)
    print 'Done.'
except api.ApiError as e:
    logging.error(e)
    print 'Ooops! Something went wrong. Please see logfile.'
