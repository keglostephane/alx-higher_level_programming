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

count = 0
tline = 0
tsize = []
status = []
tstatus = {"200": [],
           "301": [],
           "400": [],
           "401": [],
           "403": [],
           "404": [],
           "405": [],
           "300": []}

try:
    for line in sys.stdin:
        tline += 1
        data = line.rstrip('\n').split()[-2:]
        status_code, filesize = data
        status.append(status_code)
        count += int(filesize)

        if (tline % 10 == 0):
            tsize.append(count if not tsize else count + tsize[-1])
            count = 0
            for key in tstatus.keys():
                if key not in status:
                    tstatus[key].append(0)
                else:
                    for code in status:
                        if key == code:
                            count += 1
                    tstatus[key].append(count if not tstatus[key]
                                        else count + tstatus[key][-1])
                    count = 0
except KeyboardInterrupt:
    pass
finally:
    for i in range(len(tsize)):
        print(f"File size: {tsize[i]}")
        for key in tstatus.keys():
            if tstatus[key][i]:
                print(f"{key}: {tstatus[key][i]:d}")

    print(tsize)
    print(tstatus)
