#!/bin/bash

echo "This script takes Backups and Restores All databases. please provide appropriate options"
echo "#################################################################################"
sleep 2s

read -p  "Type 'y' if you want to take Backup of all databases otherwise 'n' for Next Option: " backup

if [ $backup = "y" ]; then
echo "backup of all database is started..." && \
sudo -u postgres pg_dumpall > pg_backup.tar && \
echo "backup successfully completed"
exit
fi


read -p  "Type 'y' if you want to Restore all databases otherwise 'n' for Nothing: " restore

if [ $restore = "y" ]; then
echo "First taking the backup of existing database...." && \
sudo -u postgres pg_dumpall > pg_backup-old.tar && \
echo "Backup of old database is completed"
echo " "
echo "Restoring Database......"
sleep 4s
sudo -u postgres  psql  -f pg_backup.tar postgres && \
echo "All databases are Restored successfully!!!"
exit
fi

if [[ $backup != "y" ]] && [[ $restore != "y" ]]; then
echo "Nothing to do!!!!"
fi





