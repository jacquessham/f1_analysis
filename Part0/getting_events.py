import pandas as pd
import fastf1


schedule = fastf1.get_event_schedule(2021)
print(schedule['OfficialEventName'])