
from mainapi.forms import UserForm
from mainapi.models import UserData
import csv

def run():
    with open('user_internet_session_dataset_for_mishipay_hackerearch_hiring_challenge_december_2022.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        UserData.objects.all().delete()
        c=1
        for row in reader:
            print(row)


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
