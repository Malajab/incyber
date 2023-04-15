import win32evtlog
import win32evtlogutil
import winerror
import datetime
import xlsxwriter

# Open the System event log
logtype = 'System'
hand = win32evtlog.OpenEventLog(None, logtype)

# Set the flags to read all events in the log
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ

# Get all the events
events = win32evtlog.ReadEventLog(hand, flags, 0)

# Extract all event logs
logs = []
for event in events:
    time_str = event.TimeGenerated.Format('%m/%d/%y %H:%M:%S')
    time = datetime.datetime.strptime(time_str, '%m/%d/%y %H:%M:%S')
    log = {
        'Time': time,
        'Source': event.SourceName,
        'Event ID': event.EventID,
        'Description': win32evtlogutil.SafeFormatMessage(event, logtype),
    }
    logs.append(log)

# Write the event logs to an XLS file
workbook = xlsxwriter.Workbook('all_logs.xlsx')
worksheet = workbook.add_worksheet()

# Write the headers
headers = ['Time', 'Source', 'Event ID', 'Description']
for i, header in enumerate(headers):
    worksheet.write(0, i, header)

# Write the logs
for i, log in enumerate(logs):
    worksheet.write(i+1, 0, log['Time'])
    worksheet.write(i+1, 1, log['Source'])
    worksheet.write(i+1, 2, log['Event ID'])
    worksheet.write(i+1, 3, log['Description'])

# Close the workbook
workbook.close()
