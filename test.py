from utilities.function import Room, Usertime, generate_code
import threading
import pprint
import time

user_time = Usertime()


def loop_function():
    while True:
        user_time.user_timer_up()
        print(user_time.time)
        time.sleep(1)


def later_add():
    time.sleep(3)
    user_time.add_user(generate_code())


user_time.add_user('GamerVerse')
threading.Thread(target=loop_function).start()
threading.Thread(target=later_add).start()
