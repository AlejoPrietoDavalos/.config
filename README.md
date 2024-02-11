### Como formatear
##### Reconocer la unidad del pendrive.
```bash
lsblk
```
- Esto se verá como /dev/sdbX, con X las distintas particiones.
- Supongamos que `sdb` es `MY_PEN`.

##### Desmontar unidades USB
```bash
sudo umount /dev/MY_PEN1
sudo umount /dev/MY_PEN2
# ...
```

##### FORMATEAR (PELIGROSO)
- Con la unidad USB correcta, formateamos.
```bash
sudo dd if=/dev/zero of=/dev/MY_PEN bs=4M status=progress
```

##### Escribir el Pendrive.
```bash
sudo dd bs=4M if=/path/to/archlinux.xxxxxxx.iso of=/dev/MY_PEN status=progress oflag=sync
```

### Basic Install Arch
- Para cambiar a teclado latin.
~~~bash
sudo nano /etc/vconsole.conf
# cambiar:
#KEYMAP=la-latin1
~~~

~~~bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
rm -rf yay
yay --version
~~~

- Para instalar snap.
~~~bash
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
~~~

- Install Brave.
```bash
yay -S brave-bin
```

- Si querés bindear alguna tecla.
```bash
sudo evtest
# Seleccionás el teclado, y te dice todas las teclas.
```
