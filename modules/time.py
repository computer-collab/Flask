from datetime import datetime, timedelta
import time


def SetCooldown():
    cooldown_until = time.time() + 30  # 30 seconds from now
    print("Cooldown set until:", cooldown_until)
    return cooldown_until


def CheckCooldown(future_time):
    if not isinstance(future_time, (int, float)):
        raise TypeError("future_time must be a timestamp (int or float)")

    return time.time() >= future_time


# Example usage
if __name__ == "__main__":
    echo = SetCooldown()

    if CheckCooldown(echo):
        print("Cooldown expired")
    else:
        print("Still in cooldown")
