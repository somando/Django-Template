import os
import shutil

from django.core.management.utils import get_random_secret_key

TARGET_APP_FILE = "docker/app/.env"
TARGET_APP_TEMP_FILE = "docker/app/.env.example"
TARGET_DB_FILE = "docker/db/.env"
TARGET_DB_TEMP_FILE = "docker/db/.env.example"
TARGET_TEST_FILE = "docker/test/.env"
TARGET_TEST_TEMP_FILE = "docker/test/.env.example"
TARGET_WORD = "[DjangoSecretKey]"
SECRET_KEY = get_random_secret_key()

shutil.copy(TARGET_APP_TEMP_FILE, TARGET_APP_FILE)
shutil.copy(TARGET_DB_TEMP_FILE, TARGET_DB_FILE)
shutil.copy(TARGET_TEST_TEMP_FILE, TARGET_TEST_FILE)

with open(TARGET_APP_FILE, "r") as file:
    filedata = file.read()

filedata = filedata.replace(TARGET_WORD, SECRET_KEY)

with open(TARGET_APP_FILE, "w") as file:
    file.write(filedata)

shutil.rmtree("docker/setup")
os.remove("project_setup.py")
