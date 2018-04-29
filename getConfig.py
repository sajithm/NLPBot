import utils
c = utils.get_config()
for param in c['Sqlite']:
    print(param, ':', c['Sqlite'][param])