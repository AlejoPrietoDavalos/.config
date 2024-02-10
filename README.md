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
