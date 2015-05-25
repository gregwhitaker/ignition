#! /bin/bash

#/ Usage: ignition [--install]
#/ Installs Ignition and starts the configuration wizard.

source ./utils/environment.sh
source ./utils/logging.sh

while [[ $# > 0 ]]
do
key="$1"

case $key in
    -i|--install)
    INSTALL="YES"
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done

if [ "$INSTALL" = "YES" ]; then
	log_green "Installing Ignition..."
	sudo pip install -r ./setup/requirements.txt
	log_green "Installation Complete!"
else
	python ./setup/setup.py
fi
