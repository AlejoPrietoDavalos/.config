#!/bin/bash

PACMAN_FILE="packages_pacman.txt"
YAY_FILE="packages_yay.txt"

PACKAGES_PACMAN=$(cat "$PACMAN_FILE")
PACKAGES_YAY=$(cat "$YAY_FILE")

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

if [[ -z "$PACKAGES_PACMAN" ]]; then
    echo "--> No hay paquetes en $PACMAN_FILE."
    exit 1
fi

echo "--> Instalando paquetes de pacman: $PACKAGES_PACMAN"
sudo pacman -S --needed --noconfirm $PACKAGES_PACMAN

if [[ -z "$PACKAGES_YAY" ]]; then
    echo "--> No hay paquetes en $YAY_FILE."
    exit 1
fi

echo "--> Instalando paquetes de yay: $PACKAGES_YAY"
yay -S --noconfirm $PACKAGES_YAY

echo "--> Instalación completada."
