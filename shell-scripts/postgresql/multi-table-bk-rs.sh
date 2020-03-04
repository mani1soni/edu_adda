#!/bin/bash

now=$(date +"%d_%m_%Y")

echo "################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&############################"
echo "This script takes backups and restore multiple database tables. please provide appropriate options"
sleep 2s


read -p "Enter Database Name: " database


declare -a table_name
echo "How many tables you want to enter below?"
read table_count
echo "enter $table_count table-names below: "

for(( c = 0 ; c < $table_count ; c++))
do
  read abc_elements

  table_name[$c]="$abc_elements"
done
echo -e "${table_name[@]}"



read -p  "Type 'y' if you want to take backup of tables  otherwise 'n': " backup

if [ $backup = "y" ]; then


echo "backup of all tables is started..." && \

for i in "${table_name[@]}"
do
	sudo -u postgres pg_dump -d $database -t $i > $i.tar
done
echo "###########################&&&&&&&&&&&&&&&&&&&&&&&&&&&&################################"
echo " "
echo "table backup successfully completed"
exit
fi

read -p  "Type 'y' if you want to restore table otherwise 'n': " restore

if [ $restore = "y" ]; then
echo "First taking the backup of existing tables...." && \

for i in "${table_name[@]}"
do
        sudo -u postgres pg_dump -d $database -t $i > $i-$now.tar
done

echo "Backup of old table is completed"
echo " "
echo "Restoring of  tables started......"
sleep 4s

for i in "${table_name[@]}"
do
	echo "droping existing table....."
	sudo -u postgres psql -d $database -c "DROP TABLE $i;"  
	echo " "
	echo "dropped successfully!!!"
	echo " "
	echo "Now restoring....."
	sleep 1s
	sudo -u postgres psql $database < $i.tar 
done
echo "##########################&&&&&&&&&&&&&&&&&&&&##########################"
echo " "
echo "All tables are Restored successfully!!!"
fi

if [[ $backup != "y" ]] && [[ $restore != "y" ]]; then
echo "No Useful instruction are given!!!!"
fi





