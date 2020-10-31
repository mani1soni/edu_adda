#!/bin/bash

now=$(date +"%d_%m_%Y")

echo "This Script can take backup of specific database and restore it. and also you can restore specific table from database, so choose required option "


sleep 2s
read -p "Enter Database Name here: " database
read -p  "Type 'y' if you want to take backup of  databases otherwise 'n' for next option: " backup

if [ $backup = "y" ]; then
echo "backup of database is started..." && \
sudo -u postgres pg_dump  -Fc $databse > $database.tar && \
echo "backup successfully completed"
exit
fi


read -p  "Type 'y' if you want to restore 'Entire' database otherwise 'n' for next option: " restore

if [ $restore = "y" ]; then
echo "First taking the backup of existing database...." && \
sudo -u postgres pg_dump  -Fc $databse > $database_$now.tar  && \
echo "Backup of old database is completed"
echo " "
echo "Restoring Database......"
sleep 4s
sudo -u postgres pg_restore -Fc -d $database $database.tar && \
echo "Databases is Restored successfully!!!"
exit
fi

read -p "Type 'y' if you want to restore specific tables in databases otherwise 'n' for nothing: " tb_restore

if [ $tb_restore = "y" ]; then
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

for i in "${table_name[@]}"
do
	echo "droping existing table....."
        sudo -u postgres psql -d $database -c "DROP TABLE $i;" && \
        echo " "
        echo "$i dropped successfully!!!" && \
	sudo -u postgres pg_restore -t $i -Fc -d $database $database.tar && \
	echo "$i table restored"
done
echo " "
echo "All Given tables restored successfully!!!"
fi



if [[ $backup != "y" ]] && [[ $restore != "y" ]] && [[ $tb_restore != "y" ]]; then
echo "Nothing to do!!!!"
fi





