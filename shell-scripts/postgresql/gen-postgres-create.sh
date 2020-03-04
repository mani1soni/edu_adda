#!/bin/bash

#Requiers 3 sys args from user, Format--> username, database-name, password 
echo "#####################################################################"
read -p "Enter Property name: " property

sudo -u postgres createuser $1

sudo -u postgres createdb $2_$property

sudo -u postgres psql <<EOF
alter user $1 with encrypted password '$3-$property';
grant all privileges on database $2_$property to $1;
EOF
echo "####################################################################"
echo " "
echo " "

echo "User $1, Database $2_$property with passed password $3-$property successfully created"



