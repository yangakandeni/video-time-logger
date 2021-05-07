from functions import get_total_vidoes, display_running_times, calc_total_duration, record_running_times, log_running_times, display_running_times


def program():
    # read running times from file
    running_times = display_running_times()

    # display running times
    print(f"\nCurrent logs from file:\n\n{running_times}")

    # print total records
    total = calc_total_duration(running_times)
    print(f"\nTotal duration: {total} seconds\n")

if __name__ == "__main__":
    program()
