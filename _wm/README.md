# _wm

Contenedor minimo para manejar programas de WM (`bspwm`, `sxhkd`, `polybar`, `ranger`, `picom`, `rofi`, `Thunar`).

## Idea
- Fuente de verdad: `~/.config/_wm/programs/<program>/files/*`
- Runtime real: `~/.config/<program>/*`
- Conexion entre ambos: symlinks

Si editas `~/.config/bspwm/bspwmrc` y es symlink, se refleja en Git automaticamente.

## Comandos
- `make -C _wm install-bspwm`
- `make -C _wm install-session-bspwm`
- `make -C _wm install-sxhkd`
- `make -C _wm generate-sxhkd`
- `make -C _wm install-polybar`
- `make -C _wm install-ranger`
- `make -C _wm install-picom`
- `make -C _wm install-rofi`
- `make -C _wm install-thunar`
- `make -C _wm install-core`
- `make -C _wm remove-core`

## Nota sobre archivos generados
- `sxhkdrc` no se trackea.
- Se trackea solo `sxhkdrc.template` + generador.
