import psutil
from plyer import notification
def check_battery_status(battery,plugged):
    if plugged:
        percent=battery.percent
        if percent<=80:
              notification.notify(
                  title="charger plugged in",
                  message="to get battery life charge untill 80%",
                  timeout=8
               )
        elif percent==100:
            notification.notify(
                title="charger plugged in",
                message="battery fully charged",
                timeout=8
            )
        else:
               notification.notify(
                   title="charger plugged in",
                   message="remove charger ,for better battery life only charge upto 80%",
                   timeout=8
               )
    else:
          percent=battery.percent
          if percent<=20:
              notification.notify (
                  title="Battery remainder",
                  message="plug in your pc",
                  timeout=2
              )
          elif percent<=50:
              notification.notify(
                  title="Battery remainder",
                  message=f"Battery is{percent}",
                  timeout=8

              )
          else:
              notification.notify(
                  title="Battery Remainder",
                  message=f"Battery is  {percent}",
                  timeout=8
             )
battery=psutil.sensors_battery()
plugged=battery.power_plugged
print(check_battery_status(battery,plugged))
