# _wm

Contenedor minimo para manejar programas de WM (`bspwm`, `sxhkd`, `polybar`, `ranger`, `picom`, `rofi`, `Thunar`).

## Idea
- Fuente de verdad: `~/.config/_wm/programs/<program>/files/*`
- Runtime real: `~/.config/<program>/*`
- Conexion entre ambos: symlinks

Si editas `~/.config/bspwm/bspwmrc` y es symlink, se refleja en Git automaticamente.

## Comandos
- `make install-bspwm`
- `make install-session-bspwm`
- `make install-sxhkd`
- `make generate-sxhkd`
- `make install-polybar`
- `make install-ranger`
- `make install-picom`
- `make install-rofi`
- `make install-thunar`
- `make install-core`
- `make remove-core`
- `make remove-core-purge` (desinstala tambien paquetes de pacman)

## Dependencias
- Cada programa puede definir paquetes en `_wm/packages/<program>.txt`.
- `install-<program>` instala faltantes con `pacman -S --needed`.
- `remove-<program>` solo deslinkea configs por defecto.
- Para desinstalar paquetes al remover: `WM_REMOVE_PACKAGES=1 make remove-<program>`.

## Script operativo
- Script unico: `_wm/scripts/link_unlink_file.sh`
- Parametros:
- `install <program> [target_dir]`: instala dependencias y crea symlinks.
- `remove <program> [target_dir]`: quita symlinks; con `WM_REMOVE_PACKAGES=1` tambien desinstala paquetes.

## Nota sobre archivos generados
- `sxhkdrc` no se trackea.
- Se trackea solo `sxhkdrc.template` + generador.
