from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    players_data = []
    for i in info:
        if not i.is_dir():
            with zip_file.open(i) as file:
                try:
                    data_content = file.read().decode('utf-8')
                    if is_correct_json(data_content):
                        players_data.append(json.loads(data_content))
                    else:
                        continue
                except:
                    continue
    for player in sorted(players_data, key=lambda x: (x['first_name'], x['last_name'])):
        if player['team'] == 'Arsenal':
            print(player['first_name'], player['last_name'])
        else:
            continue





