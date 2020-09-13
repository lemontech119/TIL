from datetime import datetime, timedelta


def solution(play_time, adv_time, logs):
    all_time = 0
    adv_time = list(map(int, adv_time.split(":")))
    play_time_list = list(map(int, play_time.split(":")))
    play_time_second = timedelta(hours=play_time_list[0], minutes=play_time_list[1], seconds=play_time_list[2])
    for log in logs:
        log = log.split('-')
        start_time = list(map(int, log[0].split(":")))
        end_time = list(map(int, log[0].split(":")))

        adv_start_time = timedelta(hours=start_time[0], minutes=start_time[1], seconds=start_time[2])
        adv_end_time = timedelta(hours=end_time[0], minutes=end_time[1], seconds=end_time[2]) + timedelta(hours=adv_time[0], minutes=adv_time[1], seconds=adv_time[2])
        case_time = 0
        if adv_end_time < play_time_second:

            for chk in logs:
                chk = chk.split('-')
                start_time_list = list(map(int, chk[0].split(":")))
                end_time_list = list(map(int, chk[1].split(":")))
                play_start_time = timedelta(hours=start_time_list[0], minutes=start_time_list[1], seconds=start_time_list[2])
                play_end_time = timedelta(hours=end_time_list[0], minutes=end_time_list[1], seconds=end_time_list[2])

                viewing_start_time = adv_start_time
                viewing_end_time = adv_end_time
                if play_end_time < adv_start_time:
                    continue
                if play_start_time > adv_end_time:
                    continue
                if adv_start_time <= play_start_time:
                    viewing_start_time = play_start_time
                if adv_end_time >= play_end_time:
                    viewing_end_time = play_end_time

                viewing_time = viewing_end_time - viewing_start_time
                viewing_time = int(timedelta.total_seconds(viewing_time))
                case_time += viewing_time
            if all_time < case_time:
                all_time = case_time
    if all_time == 0:
        answer = "00:00:00"
    else:
        answer = str(timedelta(seconds=all_time))

    return answer


print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))