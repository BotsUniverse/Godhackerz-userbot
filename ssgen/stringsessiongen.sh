#!/bin/bash
clear
echo "
 #######  #######  #######		$     $	  #######   $$$$$$$		#    #	$$$$$$$   #########   ########
 #		  #		#  #	 #		$     $   #		#	$			#	#	$		  #	      #        #
 #	      #     #  #     #		$	  $   #		#	$			#  #	$		  #       #		 #
 #  ##### #		#  #     # 		$$$$$$$   #######	$			###		$$$$$$$   #	#######    #
 #		# #     #  #     #		$     $   #     #	$			#  #	$         #  #		 #
 ######## #######  #######		$     $   #     #	$$$$$$$		#   #	$$$$$$$   #    #     ##########
"
# Termux session string generator for TeleBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://github.com/rohithaditya/Godhackerz-userbot/blob/main/ssgen/setup.py
pip install telethon
python setup.py
