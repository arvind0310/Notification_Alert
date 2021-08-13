import time
from plyer import notification
if __name__ == '__main__':
    while True:
         notification.notify(
             title= "Assignment Due",
             message= "Hii Arvind you have a deadline to submit your assignment.",
             app_icon= "C:\\Users\Arvind\PycharmProjects\Myproject\\bookicon.ico",
             timeout=2

         )
         time.sleep(120*60)
