
# SDDM (Simple Desktop Display Manager)
- Habilida SDDM para que inicie automáticamente con el sistema.
```bash
sudo systemctl enable sddm.service --force
```


# Keepass + Syncthing
### Instalar Keepass
- `Arch:` sudo pacman -S keepassxc
- `Windows:`
- `Android:` Google Play Store `KeePassDX`
### Instalar Syncthing
- `Arch Linux:` sudo pacman -S syncthing
- `Windows:` Descargar instalador en [syncthing.net](https://www.syncthing.net).
- `Android:` Google Play Store `Syncthing-Fork`.
### Crear y compartir keepass en Syncthing.
- Guardar credenciales en `$HOME/.config/Sync/credentials.kdbx`.

# Bluetooth (blueman)
sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service


### Etc...
- Search Google Hack: `gatitos filetype:png`