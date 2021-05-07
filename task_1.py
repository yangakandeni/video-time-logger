from functions import get_total_vidoes, display_running_times, calc_total_duration, record_running_times, log_running_times
from pprint import pprint

def program():
    total_videos = get_total_vidoes()

    try:
        # record running times
        running_times = record_running_times(total_videos)

        # save runnning times to a file
        videos = log_running_times(running_times)
        print(f"\nHERE ARE YOUR VIDEOS\n")
        pprint(videos)
        
    except TypeError:
        print(total_videos)


if __name__ == "__main__":
    program()
