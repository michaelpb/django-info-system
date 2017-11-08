#!/bin/bash

. "`dirname \"$0\"`/functions.sh"

cd $MY_PATH
cd ../..


if [[ "no" == $(ask_yes_or_no "Delete migration code and wipe DB?") ]]
then
    echo "Skipped."
    exit 0
fi

echo "--- Deleting ALL migration code..."
rm -r ./person/migrations
rm -r ./plist/migrations

echo "--- Backing up default.sqlite3.db..."
mv db.sqlite3 db.sqlite3.backup

echo "--- Rebuilding migrations..."
# python manage.py makemigrations accounts discussion gallery moderation newsletter notifications project release team users wiki
python manage.py makemigrations person plist

echo "--- Syncing DB..."
python manage.py migrate

