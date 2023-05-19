'''Making the folder structure of class XII python curriculum'''

import datetime
from datetimerange import DateTimeRange
import os
i = 1

time_range = DateTimeRange("2023-04-12T00:00:00+0900", "2024-01-04T00:00:00+0900")
for value in time_range.range(datetime.timedelta(days=1)):
    value = str(value)
    value = value.split(" ")[0]
    value = value.split("-")
    value = "-".join(list(reversed(value)))
    os.mkdir(f"{i} {value}")
    with open(f"{i} {value}/main.py", "x") as f:
        pass
    with open(f"{i} {value}/notes.md", "x") as f:
        pass
    i += 1
