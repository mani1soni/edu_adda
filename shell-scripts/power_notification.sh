#!/bin/sh

text=acpi | grep -w '[0-9][0-9]'
status=acpi | grep Discharging
dis="Discharging"
a=15

echo "$status"
while [ $text -lt$a ] && [ "$status" = "" ] 
do
	zenity --warning --title "Low Battery" --width 270 --height 100 --text="Please Connect to the Charger"
	sleep 5s
done
