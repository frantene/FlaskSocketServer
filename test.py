from utilities.function import Room, Usertime
import threading
import pprint
import time

user_time = Usertime()


def loop_function():
    while user_time.user_timer_overlimit('GamerVerse') is False:
        user_time.user_timer_up()
        print(user_time.time)
        time.sleep(1)


def later_add():
    time.sleep(3)
    user_time.add_user('Money')


user_time.add_user('GamerVerse')

# Correct the threading target function calls, remove the parentheses ()
threading.Thread(target=loop_function).start()
threading.Thread(target=later_add()).start()

# time.sleep(9)

print(user_time.user_timer_overlimit('GamerVerse'), user_time.user_timer_overlimit('Money'))