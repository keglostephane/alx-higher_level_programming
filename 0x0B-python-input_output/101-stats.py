#!/usr/bin/python3
"""101-stats

Read stdin line by line and compute metric.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
              <status code> <file size>

Each 10 lines and after a keyboard interruption, prints those statistics:

File size: <total size>
``total size``: the sum of all previous file size

<status code>: <number>
possible ``status code``: 200, 301, 400, 401, 403, 404, 405, 500
``number``: number of line by status code
"""
import sys

tsize = 0
tline = 0
status = {}

for line in sys.stdin:
    tline += 1
    data = line.rstrip('\n').split()[-2:]
    status_code, filesize = data

    if status_code not in status.keys():
        status[status_code] = 1
    else:
        status[status_code] += 1
    tsize += int(filesize)

    if tline == 10:
        print(f"File size: {tsize}")
        for key in sorted(status.keys()):
            print(f"{key}: {status[key]:d}")
        tline = 0
