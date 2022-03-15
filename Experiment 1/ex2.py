from datetime import *

if __name__ == '__main__':
    try:
        time_raw = input('Please input the time(HH:MM:SS):')
        time = datetime.strptime(time_raw, '%H:%M:%S')
        time += timedelta(seconds=1)
        print(time.strftime('%H:%M:%S'))
    except:
        print("Invalid input")