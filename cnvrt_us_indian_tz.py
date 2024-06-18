from datetime import datetime
import pytz

def convert_us_to_indian_time(us_datetime_str, us_timezone):
    try:
        # Define the Indian timezone
        india_tz = pytz.timezone('Asia/Kolkata')

        # Define the US timezone
        us_tz = pytz.timezone(us_timezone)

        # Parse the user-provided datetime string
        us_datetime_naive = datetime.strptime(us_datetime_str, "%m/%d/%Y %H:%M:%S")

        # Localize the naive datetime to the US timezone
        us_datetime = us_tz.localize(us_datetime_naive)

        # Convert the US time to Indian time
        india_time = us_datetime.astimezone(india_tz)
        print("Indian Time:", india_time.strftime("%m/%d/%Y, %H:%M:%S"))
    except pytz.UnknownTimeZoneError:
        print(f"Unknown timezone: {us_timezone}. Please provide a valid US timezone.")
    except ValueError:
        print(f"Invalid datetime format: {us_datetime_str}. Please provide a valid datetime in the format 'MM/DD/YYYY HH:MM:SS'.")

# List of valid US timezones for reference
us_timezones = [
    'America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles',
    'America/Anchorage', 'America/Phoenix', 'America/Indianapolis', 'America/Honolulu'
]

print("Valid US timezones are:", us_timezones)

# User input for the US datetime and timezone
user_input_datetime = input("Enter the US datetime (MM/DD/YYYY HH:MM:SS): ")
user_input_timezone = input("Enter the US timezone: ")

# Convert the time
convert_us_to_indian_time(user_input_datetime, user_input_timezone)
