#!/usr/bin/env bash
set -u

QUIET="${1:-}"

if [[ "${QUIET}" == "--quiet" ]]; then
  if [[ -z "${DISPLAY:-}" ]]; then
    echo "[WARN] DISPLAY no esta seteado."
    exit 0
  fi

  if ! command -v xrandr >/dev/null 2>&1; then
    echo "[WARN] xrandr no disponible."
    exit 0
  fi

  connected_count="$(xrandr --query 2>/dev/null | awk '/ connected/{c++} END{print c+0}')"
  active_count="$(xrandr --listmonitors 2>/dev/null | awk 'NR==1{print $2+0}')"
  if [[ "${connected_count}" -gt "${active_count}" ]]; then
    echo "[WARN] Hay salidas conectadas sin activar (${active_count}/${connected_count})."
  fi

  if lspci -k 2>/dev/null | grep -q "NVIDIA Corporation" && lspci -k 2>/dev/null | grep -q "Kernel driver in use: nouveau"; then
    echo "[WARN] NVIDIA usando nouveau (posible problema con monitor externo)."
  fi
  exit 0
fi

echo "== Display/GPU check =="
echo

if [[ -z "${DISPLAY:-}" ]]; then
  echo "[WARN] DISPLAY no esta seteado. Ejecuta esto dentro de la sesion grafica."
  echo
else
  echo "[INFO] DISPLAY=${DISPLAY}"
fi

if [[ -n "${DISPLAY:-}" ]] && command -v xrandr >/dev/null 2>&1; then
  echo
  echo "-- xrandr --listmonitors --"
  xrandr --listmonitors || true
  echo
  echo "-- xrandr connected outputs --"
  xrandr --query | awk '/ connected/{print}' || true
else
  echo "[WARN] xrandr no disponible o sin DISPLAY."
fi

echo
echo "-- GPU kernel driver (lspci -k) --"
if command -v lspci >/dev/null 2>&1; then
  lspci -k | awk '
    /VGA compatible controller|3D controller|Display controller/ {print; show=1; next}
    show && /^$/ {show=0}
    show {print}
  ' || true
else
  echo "[WARN] lspci no encontrado (instalar pciutils)."
fi

echo
echo "-- DRM modules loaded --"
lsmod | awk '/^(amdgpu|i915|nouveau|nvidia|nvidia_drm|radeon)/{print}' || true

echo
echo "-- Recent kernel display errors --"
journalctl -b -k --no-pager 2>/dev/null | grep -Ei 'drm|amdgpu|i915|nouveau|nvidia|edid|dp|hdmi|displayport' | tail -n 40 || true

echo
if lspci -k 2>/dev/null | grep -q "NVIDIA Corporation" && lspci -k 2>/dev/null | grep -q "Kernel driver in use: nouveau"; then
  echo "[WARN] Detectado NVIDIA usando nouveau."
  echo "       En RTX 40 mobile esto puede causar pantalla externa en negro/inestable."
  echo "       Recomendado en EndeavourOS/Arch: usar driver propietario nvidia."
  echo "       Ejemplo:"
  echo "         sudo pacman -Syu nvidia nvidia-utils nvidia-settings"
  echo "         sudo mkinitcpio -P"
  echo "         reboot"
fi

echo
echo "[TIP] Si el monitor figura 'connected' pero no activo, proba:"
echo "      xrandr --output <SALIDA> --auto --right-of eDP-1"
echo "      (reemplaza <SALIDA> por HDMI-1, DP-1, etc.)"
