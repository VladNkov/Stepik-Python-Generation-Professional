import json

weekdays = {i: day for i, day in enumerate(['Sunday', 'Monday', 'Tuesday'])}

weekdays_json = json.dumps(weekdays, separators=('; ', '-'))

print(weekdays_json)