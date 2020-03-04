#!/bin/bash


echo "This Script can Create Database, Database Role-Password and Grant all privilages to the Role on Database.... "

sleep 1s

#Collect user inputs
read -p "Enter Property Name: " property
read -p "Enter DB Username: " username
read -p "Enter DB Name: " dbname
read -p "Enter DB Password: " password


sudo -u postgres createuser $username               # Creating users by postgres user...
sudo -u postgres createdb ${dbname}_${property}     # appending property name with dbname for uniqueness

sudo -u postgres psql <<EOF
alter user $username with encrypted password '$password-$property';
grant all privileges on database  ${dbname}_${property} to $username;
EOF

echo "#############################################################################################"
echo " "
echo " "

echo "User '$username' with all privileges on Database '${dbname}_${property}' with password '$password-$property' has been Created"



