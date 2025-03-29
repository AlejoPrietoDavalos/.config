#!/bin/bash

PACMAN_FILE="packages_pacman.txt"
YAY_FILE="packages_yay.txt"
SNAP_FILE="packages_snap.txt"


PACKAGES_PACMAN=$(cat "$PACMAN_FILE")
PACKAGES_YAY=$(cat "$YAY_FILE")
PACKAGES_SNAP=$(cat "$SNAP_FILE")



# Intala yay si no estuviera ya instalado.
if ! command -v yay &> /dev/null; then
    echo "--> Instalando yay..."
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm base-devel git
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    rm -rf yay
    yay --version
else
    echo "--> yay ya está instalado, no es necesario instalarlo."
fi



# Instala snap si no estuviera ya instalado.
if ! command -v snap &> /dev/null; then
    echo "--> Instalando snap..."
    git clone https://aur.archlinux.org/snapd.git
    cd snapd
    makepkg -si --noconfirm
    sudo systemctl enable --now snapd.socket
    sudo systemctl enable --now snapd.apparmor.service
    sudo ln -s /var/lib/snapd/snap /snap
    cd ..
    rm -rf snapd
    snap version
else
    echo "--> snap ya está instalado, no es necesario instalarlo."
fi



# Instalar paquetes de pacman si hay paquetes listados
if [[ -z "$PACKAGES_PACMAN" ]]; then
    echo "--> No hay paquetes en $PACMAN_FILE."
else
    echo "--> Instalando paquetes de pacman: $PACKAGES_PACMAN"
    sudo pacman -S --needed --noconfirm $PACKAGES_PACMAN
fi


# Instalar paquetes de yay si hay paquetes listados
if [[ -z "$PACKAGES_YAY" ]]; then
    echo "--> No hay paquetes en $YAY_FILE."
else
    echo "--> Instalando paquetes de yay: $PACKAGES_YAY"
    yay -S --needed --noconfirm $PACKAGES_YAY
fi


# Instalar paquetes de snap si hay paquetes listados
if [[ -z "$PACKAGES_SNAP" ]]; then
    echo "--> No hay paquetes en $SNAP_FILE."
else
    echo "--> Instalando paquetes de snap: $PACKAGES_SNAP"
    sudo snap install $PACKAGES_SNAP
fi

#----> Activo cosas.
pulseaudio --start


echo "--> Instalación completada."
