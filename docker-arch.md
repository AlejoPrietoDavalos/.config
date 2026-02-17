# Docker + Docker Compose en Arch Linux

## Instalacion automatizada en este repo

Usa el programa `docker` del instalador:

```bash
make install PROGRAM=docker
```

Ese comando hace:
- instala `docker` y `docker-compose`
- ejecuta `sudo systemctl enable --now docker.service`
- crea el grupo `docker` si no existe
- agrega tu usuario al grupo `docker` si no estaba

## Instalacion manual (tutorial con `yay`)

Si no tienes `yay`, sigue primero esta guia:
- https://itsfoss.com/install-yay-arch-linux

### Update
```sh
yay
```

### Install
```sh
yay -S docker docker-compose
```

### Start the service
```sh
sudo systemctl start docker.service
```

Si el comando anterior falla:
```sh
sudo systemctl enable docker.service
reboot
```

### Linux post-install (usar Docker sin `sudo`)
```sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Si agregaste tu usuario al grupo `docker`, puede requerir cerrar sesion y volver a entrar (o reiniciar) para que aplique en toda la sesion.

## Sobre `systemctl`

- `systemctl` viene con `systemd`
- en Arch Linux no es un programa "de otro repo aparte" para instalar suelto
- se usa para habilitar/iniciar servicios del sistema (como `docker.service`)
