def set_reminder(reminder_time, message):
    scheduler.enterabs(reminder_time, 1, show_reminder, (message,))
    scheduler.run()
