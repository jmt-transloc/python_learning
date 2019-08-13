# Chain Maps
from collections import ChainMap

default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}

conn = ChainMap(connection, default_connection)

conn['port']
conn['host']
