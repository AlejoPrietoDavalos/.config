
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

# WM Automation
La automatizacion vive en `_wm/main.py` y se ejecuta con:

```bash
cd ./_wm && PYTHONPATH=./src python3 ./main.py --action <action> --program <program>
```

Acciones soportadas:
- `install`
- `uninstall`
- `install-requirement`
- `uninstall-requirement`
- `install-files`
- `uninstall-files`

Atajos por `make`:
- `make install-<program>`
- `make uninstall-<program>`
- `make install-requirement-<program>`
- `make uninstall-requirement-<program>`
- `make install-files-<program>`
- `make uninstall-files-<program>`

### bspwm
```bash
make install-bspwm
make uninstall-bspwm
make install-requirement-bspwm
make install-files-bspwm
make install-session-bspwm
```

### sxhkd
```bash
make install-sxhkd
make uninstall-sxhkd
make install-requirement-sxhkd
make install-files-sxhkd
make generate-sxhkd
```

### polybar
```bash
make install-polybar
make uninstall-polybar
make install-requirement-polybar
make install-files-polybar
```

### ranger
```bash
make install-ranger
make uninstall-ranger
make install-requirement-ranger
make install-files-ranger
```

### picom
```bash
make install-picom
make uninstall-picom
make install-requirement-picom
make install-files-picom
```

### rofi
```bash
make install-rofi
make uninstall-rofi
make install-requirement-rofi
make install-files-rofi
```

### thunar
```bash
make install-thunar
make uninstall-thunar
make install-requirement-thunar
make install-files-thunar
```

### vscode
```bash
make install-vscode
make uninstall-vscode
make install-requirement-vscode
make install-files-vscode
```

Notas:
- `vscode` usa copia de `settings.json` (no symlink).
- `sxhkd` regenera `~/.config/sxhkd/sxhkdrc` en `install-files-sxhkd`.
