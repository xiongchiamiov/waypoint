# Put these two lines in your .bash_profile or .zprofile
# (with the appropriate directory, of course)
#WAYPOINT_DIRECTORY=~/Documents/waypoint
#source "$WAYPOINT_DIRECTORY"/waypoint.sh

function waypoint {
	python "$WAYPOINT_DIRECTORY"/waypoint.py $@ &&
	source ~/.config/waypoint/scratch.sh
	echo /dev/null > ~/.config/waypoint/scratch.sh
}

# create the waypoint directory, if it doesn't exist
mkdir -p ~/.config/waypoint
