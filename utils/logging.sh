#! /bin/bash

#/ Usage: log_red <message>
#/ Logs the supplied parameter in ANSI red.
log_red() {
	echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

#/ Usage: log_yellow <message>
#/ Logs the supplied parameter in ANSI yellow
log_yellow() {
	echo -e "$(tput setaf 3)$1$(tput sgr0)"
}

#/ Usage: log_green <message>
#/ Logs the supplied parameter in ANSI green
log_green() {
	echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

#/ Usage: log <message>
#/ Logs the supplied parameter in ANSI white
log() {
	echo $1
}