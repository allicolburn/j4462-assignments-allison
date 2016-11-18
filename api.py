import json, requests

#url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&subject=Environmental'

r = requests.get('http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&subject=Environmental')

response_data = r.content

data = json.loads(response_data)

for item in data: 
    url_id = ['id']
    r2 = requests.get('http://openstates.org/api/v1/bills/' + 'url_id')
    response_data2 = r2.content
    data2 = json.loads(response_data2)

for item in data:
    print item ['bill_id']
    print item ['title']

for item in data2:
    if actions in ['actions'] is item ['action_dates']['last']:
        print item ['actions']['action']
