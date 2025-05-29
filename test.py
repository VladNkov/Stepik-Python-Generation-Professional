from collections import namedtuple

App = namedtuple('App', ['name', 'apptype', 'size'])

app = App._make('Discord messenger 200'.split())

print(app)
