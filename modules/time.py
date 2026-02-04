from datetime import datetime, timedelta

def SetCooldown():
    return datetime.now() + timedelta(seconds=30)

def CheckCooldown(future_time):
    if not isinstance(future_time, datetime):
        raise TypeError("future_time must be a datetime object")

    return datetime.now() >= future_time

# Example usage
if __name__ == "__main__":
    # Start cooldown
    cooldown_end = start_cooldown()
    print("Cooldown ends at:", cooldown_end.strftime("%H:%M:%S"))

    # Simulate checking
    import time
    for i in range(35):  # Check every second for 35 seconds
        time.sleep(1)
        if check_cooldown(cooldown_end):
            print(f"[{i+1}s] Cooldown complete!")
            break
        else:
            print(f"[{i+1}s] Cooldown still active...")
