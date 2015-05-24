#! /bin/bash

# Logs the supplied parameter in ANSI red
log_red() {
	echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI yellow
log_yellow() {
	echo -e "$(tput setaf 3)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI green
log_green() {
	echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

# Logs the supplied parameter in ANSI white
log() {
	echo $1
}
