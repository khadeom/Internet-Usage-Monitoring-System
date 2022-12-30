from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserDataSerializer,InternetUsageSerializer
from .models import UserData
from django.core.paginator import Paginator
from dateutil.parser import parse
from datetime import timedelta

class TopUsersView(APIView):
    def get(self, request, date):
        # Parse the input date into a datetime object
        input_date = parse(date)
        today = input_date.date()

        # Calculate start and end times for the desired time periods
        last_day = today - timedelta(days=1)
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)
        print("firstprint:",last_day, last_week, last_month)
        # Filter the internet usage data for the desired time periods
        usage_1day = UserData.objects.filter(start_time__gte=last_day)
        usage_7days = UserData.objects.filter(start_time__gte=last_week)
        usage_30days = UserData.objects.filter(start_time__gte=last_month)

        print("usge_1da",usage_1day,usage_7days,usage_30days)
        # Calculate the total usage for each user in each time period
        usage_by_user_1day = {}
        usage_by_user_7days = {}
        usage_by_user_30days = {}
        for usage in usage_1day:
            if usage.username in usage_by_user_1day:
                usage_by_user_1day[usage.username] += usage.usage_time
            else:
                usage_by_user_1day[usage.username] = usage.usage_time
        for usage in usage_7days:
            if usage.username in usage_by_user_7days:
                usage_by_user_7days[usage.username] += usage.usage_time
            else:
                usage_by_user_7days[usage.username] = usage.usage_time
        for usage in usage_30days:
            if usage.username in usage_by_user_30days:
                usage_by_user_30days[usage.username] += usage.usage_time
            else:
                usage_by_user_30days[usage.username] = usage.usage_time




        # Create a list of dictionaries with the total usage data for each user
        usage_data = []
        for username, usage in usage_by_user_1day.items():
            data = {
                'username': username,
                'usage_1day': usage,
                'usage_7days': usage_by_user_7days.get(username, 0),
                'usage_30days': usage_by_user_30days.get(username, 0)
            }
            usage_data.append(data)
        print(usage_data)

        # Paginate the results
        paginator = Paginator(usage_data, 10)
        page = request.GET.get('page')
        usage_data_page = paginator.get_page(page)

        # Serialize the results and return them to the client
        serializer = InternetUsageSerializer(usage_data_page, many=True)
        return Response(serializer.data)
















