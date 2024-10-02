import shutil

TARGET_APP_FILE = "docker/app/.env"
TARGET_APP_TEMP_FILE = "docker/app/.env.example"
TARGET_DB_FILE = "docker/db/.env"
TARGET_DB_TEMP_FILE = "docker/db/.env.example"

shutil.copy(TARGET_APP_TEMP_FILE, TARGET_APP_FILE)
shutil.copy(TARGET_DB_TEMP_FILE, TARGET_DB_FILE)
