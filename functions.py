

import pickle, uuid

def get_total_vidoes():
    response = input("\nHow many short videos do you have?: ")
    videos = None
    try:
        # convert response to int
        videos = int(response)
        return videos

    except ValueError:
        return f"\nPlease enter a valid number\n"

def record_running_times(total_videos):
    running_times = dict()
    for video_count in range(total_videos):
        response = input(f"\nHow long is video {video_count + 1}: ")
        try:
            video_length =  int(response)
            running_times.setdefault(f'video_{str(uuid.uuid4())[:6]}', video_length)

        except ValueError:
            print(f"\nPlease enter valid seconds")
            while (not isinstance(response, int)):
                response = input(f"\nHow long is video {video_count + 1}: ")
                try:
                    response = int(response)
                except ValueError:
                    print(f"\nPlease enter valid seconds")

    return running_times

def log_running_times(recorded_times):
    
    current_logs = display_running_times()
    recorded_times.update(current_logs)
    

    with open('video_logs.pickle', 'wb+') as f:

        print("\nSaving video running times ....")
        pickle.dump(recorded_times, f, pickle.HIGHEST_PROTOCOL)
    return "\nDone!\n"

def display_running_times():
    logs = {}
    try:
        with open('video_logs.pickle', 'rb') as f:
            logs = pickle.load(f)
            return logs
    except EOFError:
        return logs
    except FileNotFoundError:
        with open('video_logs.pickle', 'ab+') as f:
            pass
        # print("\nWe created a new file for you\n")

def calc_total_duration(total_records):
    total_duration = sum(total_records.values())
    
    return total_duration
    
        


