from datetime import datetime, timedelta
import time

from datetime import datetime, timedelta

def SetCooldown():
    cooldown_until = datetime.now() + timedelta(seconds=30)
    print("Cooldown set until:", cooldown_until)
    return cooldown_until.isoformat()

def CheckCooldown(future_time):
    cooldown = datetime.fromisoformat(future_time)
    if not isinstance(cooldown, datetime):
        return False
    return datetime.now() > cooldown

# Example usage
if __name__ == "__main__":
    echo = SetCooldown()

    if CheckCooldown(echo) == "true":
        print("Cooldown expired")
    else:
        print("Still in cooldown")
    time.sleep(31);

    if CheckCooldown(echo) == "true":
        print("Cooldown expired")
    else:
        print("Still in cooldown")


