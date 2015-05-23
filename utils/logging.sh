#! /bin/bash

# Logs the supplied parameter in ANSI green
logGreen() {
	echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI red
logRed() {
	echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI yellow
logYellow() {
	echo -e "$(tput setaf 3)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI white
log() {
	echo $1
}
