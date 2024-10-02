from django.core.management.utils import get_random_secret_key

TARGET_APP_FILE = "docker/app/.env"
TARGET_WORD = "[DjangoSecretKey]"
SECRET_KEY = get_random_secret_key()

with open(TARGET_APP_FILE, 'r') as file:
  filedata = file.read()

filedata = filedata.replace(TARGET_WORD, SECRET_KEY)

with open(TARGET_APP_FILE, 'w') as file:
  file.write(filedata)

print("Initialize successfully!")
