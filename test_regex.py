import re

log_pattern = r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<module>\S+) +(?P<level>\w+) +(?P<message>.*)$'

log_entries = [
    '2024-09-15 21:05:23,067 __main__     WARNING  And this, too',
    '2024-09-15 21:05:23,067 __main__     ERROR    And non-ASCII stuff, too, like Øresund and Malmö',
    '2024-09-15 21:05:28,070 __main__     DEBUG    This message should go to the log file',
    '2024-09-15 21:05:28,071 __main__     INFO     So should this',
    '2024-09-15 21:05:28,071 __main__     WARNING  And this, too'
]

for log_entry in log_entries:
    match = re.match(log_pattern, log_entry)
    if match:
        print(match.groupdict())