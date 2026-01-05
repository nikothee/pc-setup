#!/usr/bin/env bash

if (($EUID == 0)); then
    echo "Don't run as root"
    exit
fi

################################################################################
### get git credentials

if [ -z "$GIT_NAME" ]; then
    if ! GIT_NAME=$(zenity --entry --title "git User Name" --text "Please enter your name:" --entry-text "Firstname Lastname"); then
        notify-send -i dialog-error "Aborting..." "Please enter your Name to continue"
        exit
    fi
    export GIT_NAME
fi

if [ -z "$GIT_EMAIL" ]; then
    if ! GIT_EMAIL=$(zenity --entry --title "git User Email" --text "Please enter your Email adress:" --entry-text "nobody@example.com"); then
        notify-send -i dialog-error "Aborting..." "Please enter your Email to continue"
        exit
    fi
    export GIT_EMAIL
fi

################################################################################
### run ansible playbook

notify-send -i dialog-information "Starting installation…" "Running Ansible Playbook…"

ansible-galaxy collection install community.general
# sudo echo performs a sudo login which solves the issue of ansible silently waiting for fingerprint sensor input and stalling
sudo echo "Enter your password to start the ansible playbook"
ansible-playbook site.yml --inventory inventory --ask-become-pass

################################################################################

notify-send -i dialog-information "Installation finished!" "Please reboot to apply all changes.\nAfterwards consult the todos.md file in your home directory for further steps"
