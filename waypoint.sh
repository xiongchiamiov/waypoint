function waypoint {
	python ~/Documents/waypoint/waypoint.py $@ &&
	source ~/.config/waypoint/scratch.sh
	echo /dev/null > ~/.config/waypoint/scratch.sh
}

# create the waypoint directory, if it doesn't exist
mkdir -p ~/.config/waypoint
