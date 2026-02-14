#!/bin/bash

echo "--> Actualizando repositorios y paquetes de pacman."
sudo pacman -Syu --noconfirm

echo "--> Actualizando paquetes de AUT con yay."
yay -Syu --noconfirm


echo "--> Limpiando el cache de pacman."
sudo pacman -Scc --noconfirm

echo "--> Limpiando cache de yay."
yay -Scc --noconfirm


echo "--> Actualizando paquetes de snap"
sudo snap refresh


echo "--> Verificando sistema de archivos."
sudo fsck -Af -M


echo "Eliminando dependencias huérfanas..."
sudo pacman -Rns $(pacman -Qdtq) --noconfirm
