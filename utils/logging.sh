#! /bin/bash

logGreen() {
	echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

logRed() {
	echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

logYellow() {
	echo -e "$(tput setaf 3)$1$(tput sgr0)"
}

log() {
	echo $1
}
