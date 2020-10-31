#!/bin/bash

now=$(date +"%d_%m_%Y")


#Collect user inputs  

#pg_dump -d asus_mobile -t account > asus.tar


#psql asus_mobile < asus.tar


echo "This script can take backups and restore specific database  table. please provide appropriate options"
sleep 2s

read -p "Enter Database Name: " database
read -p "Enter table name: " table
read -p  "Type 'y' if you want to take backup of table  otherwise 'n' for Next option: " backup

if [ $backup = "y" ]; then
echo "backup of all database is started..." && \
sudo -u postgres pg_dump -d $database -t $table > $table.tar  && \
echo "table backup successfully completed"
exit
fi

read -p  "Type 'y' if you want to restore table otherwise 'n' for Nothing: " restore

if [ $restore = "y" ]; then
echo "First taking the backup of existing database...." && \
sudo -u postgres pg_dump -d $database -t $table > $table-old_$now.tar  && \
echo "Backup of old database is completed"
echo " "
echo "Restoring Database......"
sleep 4s
sudo -u postgres psql -d $database -c "DROP TABLE $table;" &&\
sudo -u postgres psql $database < $table.tar && \
echo "All databases are Restored successfully!!!"
exit
fi

if [[ $backup != "y" ]] && [[ $restore != "y" ]]; then
echo "Nothing to do!!!!"
fi





