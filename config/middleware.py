from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import geocoder


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        location_info = geocoder.ip("me")

        # Extract the detected location coordinates
        latitude = location_info.latlng[0]
        longitude = location_info.latlng[1]

        # Use timezonefinder to find the timezone based on coordinates
        tz_finder = TimezoneFinder()
        timezone_name = tz_finder.timezone_at(lng=longitude, lat=latitude)

        # Get the current time in the detected timezone
        current_time = datetime.now(pytz.timezone(timezone_name))

        # Format and print the local time
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        print(f"Your current local time: {formatted_time}")
        request.timezone = formatted_time
        response = self.get_response(request)
        return response
