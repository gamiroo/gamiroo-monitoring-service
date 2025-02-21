def get_current_utc_time():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)
