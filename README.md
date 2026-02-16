
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
La automatizacion vive en `main.py` y se ejecuta con:

```bash
PYTHONPATH=. python3 ./main.py --action <action> --program <program>
```

Acciones soportadas:
- `install`
- `uninstall`
- `install-requirement`
- `uninstall-requirement`
- `install-files`
- `uninstall-files`
- `dirty_install_all_packages` (solo testing)

## Makefile simplificado
Ahora hay 6 comandos genericos y todos reciben `PROGRAM=<program>`:

```bash
make install PROGRAM=<program>
make uninstall PROGRAM=<program>
make install-requirement PROGRAM=<program>
make uninstall-requirement PROGRAM=<program>
make install-files PROGRAM=<program>
make uninstall-files PROGRAM=<program>
make install-all
```

Programas disponibles:
- `bspwm`, `sxhkd`, `polybar`, `kitty`, `ranger`, `picom`, `rofi`, `thunar`, `vscode`, `wm-base`, `pulseaudio`, `display-tools`, `nvidia`.

Ejemplos:
```bash
make install PROGRAM=bspwm
make install-files PROGRAM=sxhkd
make uninstall PROGRAM=polybar
```

Notas:
- `make install-files PROGRAM=sxhkd` regenera automaticamente `~/.config/sxhkd/sxhkdrc`.
- `vscode` usa copia de `settings.json` (no symlink).
- `make install-all` usa la accion dirty para instalar paquetes+files de todos los repos del registry.

## Comandos auxiliares
```bash
make install-core
make install-all
make remove-core
make remove-core-purge
make wm-requirements-install
make bspwm-bootstrap
make bspwm-install-session
make bspwm-check-display
make bspwm-restart
make sxhkd-generate
make scripts-chmod
make clock-set
make keyboard-set-latam
make sddm-install
make sddm-enable
make sddm-start
```
