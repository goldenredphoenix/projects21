from datetime import datetime, timedelta




def get_list_timestamps_for_schedule(start_time, end_time, step):

    date_format = "%H:%M"
    step = int(step)
    dt_obj_start = datetime.strptime(start_time, date_format)
    dt_obj_end = datetime.strptime(end_time, date_format)

    step = timedelta(minutes=step)

    str_time = []
    temp_time = dt_obj_start


    while temp_time <= dt_obj_end: 
        t = temp_time.strftime(date_format)
        str_time.append(t)
        temp_time = temp_time+step

    return str_time


time_first = input("Enter the time of the first appointment (08:00): ")
time_last = input("Enter the time of the last appointment (13:30): ")
duration = input("Enter the duration of one appointment in minutes (15): ")

schedule = get_list_timestamps_for_schedule(time_first, time_last, duration)
print(schedule)
