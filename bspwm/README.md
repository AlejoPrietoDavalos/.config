- Crear el json de monitores.
```bash
# Into "monitors.json".
{"monitors": ["HDMI-A-0", "eDP"]}
```


### Para que bspwm se ejecute con logs, ir a:
```bash
sudo nano /usr/share/xsessions/bspwm.desktop
```

- Esto es lo que vamos a ver.
```bash
[Desktop Entry]
Name=bspwm
Comment=Binary space partitioning window manager
Exec=bspwm
Type=Application
```

- Se debe cambiar el campo "Exec" para que ejecute start_bspwm.sh
```bash
# Reemplazar MY_USER con el usuario actual.
Exec=/home/{{MY_USER}}/.config/bspwm/start_bspwm.sh
```
