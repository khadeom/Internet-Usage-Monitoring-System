from mainapi.forms import UserForm
from mainapi.models import UserData

import csv
from django.db.models import load_app

load_app('django.contrib.admin')
load_app('mainapi')

with open('user_internet_session_dataset_for_mishipay_hackerearch_hiring_challenge_december_2022.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

for row in rows:
    form = UserForm({
        'username': row[0],
        'mac_address': row[1],
        'start_time': row[2],
        'usage_time': row[3],
        'upload': row[4],
        'download': row[5]
    })
    if form.is_valid():
        form.save()
