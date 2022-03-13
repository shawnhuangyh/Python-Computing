from datetime import datetime, timedelta

if __name__ == '__main__':
    time_raw = input('Please input the time(HH:MM:SS):')
    time = datetime.strptime(time_raw, '%H:%M:%S')
    time += timedelta(seconds=1)
    print(time.strftime('%H:%M:%S'))