
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
cd ./_wm && PYTHONPATH=. python3 ./main.py --action <action> --program <program>
```

Acciones soportadas:
- `install`
- `uninstall`
- `install-requirement`
- `uninstall-requirement`
- `install-files`
- `uninstall-files`

Atajos por `make`:
- `make <program>-install`
- `make <program>-uninstall`
- `make <program>-install-requirement`
- `make <program>-uninstall-requirement`
- `make <program>-install-files`
- `make <program>-uninstall-files`
- `make install-core`
- `make wm-requirements-install`
- `make bspwm-install-session`
- `make bspwm-check-display`
- `make bspwm-restart`
- `make sddm-install`
- `make sddm-enable`
- `make sddm-start`
- `make bspwm-bootstrap`

Primera configuracion para probar `bspwm`:
```bash
make bspwm-bootstrap
```
Opcional si usas SDDM:
```bash
make sddm-install
make sddm-enable
make sddm-start
```
Luego cerrar sesion y elegir `bspwm` en SDDM (o iniciar con tu metodo de sesion X preferido).

### bspwm
```bash
make bspwm-install
make bspwm-uninstall
make bspwm-install-requirement
make bspwm-install-files
make bspwm-install-session
make bspwm-bootstrap
make bspwm-check-display
make bspwm-restart
```

### sxhkd
```bash
make sxhkd-install
make sxhkd-uninstall
make sxhkd-install-requirement
make sxhkd-install-files
make sxhkd-generate
```

### polybar
```bash
make polybar-install
make polybar-uninstall
make polybar-install-requirement
make polybar-install-files
```

### kitty
```bash
make kitty-install
make kitty-uninstall
make kitty-install-requirement
make kitty-install-files
```

### ranger
```bash
make ranger-install
make ranger-uninstall
make ranger-install-requirement
make ranger-install-files
```

### picom
```bash
make picom-install
make picom-uninstall
make picom-install-requirement
make picom-install-files
```

### rofi
```bash
make rofi-install
make rofi-uninstall
make rofi-install-requirement
make rofi-install-files
```

### thunar
```bash
make thunar-install
make thunar-uninstall
make thunar-install-requirement
make thunar-install-files
```

### vscode
```bash
make vscode-install
make vscode-uninstall
make vscode-install-requirement
make vscode-install-files
```

### nvidia
```bash
make nvidia-install
make nvidia-uninstall
make nvidia-install-requirement
make nvidia-install-files
```

### wm-base
```bash
make wm-base-install
make wm-base-uninstall
make wm-base-install-requirement
make wm-base-install-files
```

### pulseaudio
```bash
make pulseaudio-install
make pulseaudio-uninstall
make pulseaudio-install-requirement
make pulseaudio-install-files
```

### display-tools
```bash
make display-tools-install
make display-tools-uninstall
make display-tools-install-requirement
make display-tools-install-files
```

### clock / keyboard commands
```bash
make clock-set
make keyboard-set-latam
```

Instalar dependencias modulares del stack WM (incluyendo NVIDIA):
```bash
make wm-requirements-install
```

Notas:
- `vscode` usa copia de `settings.json` (no symlink).
- `sxhkd` regenera `~/.config/sxhkd/sxhkdrc` en `sxhkd-install-files`.
