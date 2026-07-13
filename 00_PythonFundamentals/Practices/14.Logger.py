# Exercise 1: INFO Level-এর একটি Logger তৈরি করো।
# Exercise 2: সব ধরনের Logging Level ব্যবহার করো। DEBUG, INFO, WARNING, ERROR, CRITICAL
# import logging

# logging.basicConfig(level=logging.INFO)

# logging.debug("Debugging")
# logging.info("Application started.")
# logging.warning("Low disk space.")
# logging.error("somethin went wrong.")
# logging.critical("Critical Error")

# --------------------------------------------------
# --------------------------------------------------
# Exercise 3: Log File তৈরি করো। logs/app.log এ Log Save হবে।
# Exercise 4: Exception Handle করে logging.exception() ব্যবহার করো।
# import os
# import logging

# os.makedirs("logs", exist_ok=True)

# logging.basicConfig(
#     filename="logs/app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Application started")
# logging.warning("This is a warning")
# logging.error("something went wrong.")

# try:
#     result = 10/0
# except Exception:
#     logging.exception("An exception occurred")
# --------------------------------------------------
# --------------------------------------------------
# Exercise 5: Timestamp, Level এবং Message সহ Custom Formatter তৈরি করো।

import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Application started.")
logging.warning("Low disk space.")
logging.error("Something went wrong.")