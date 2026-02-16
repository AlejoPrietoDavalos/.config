SHELL := /bin/bash
RUN := PYTHONPATH=. python3 ./main.py

.PHONY: install-core remove-core remove-core-purge \
	wm-requirements-install \
	sddm-install sddm-enable sddm-start bspwm-bootstrap \
	bspwm-install bspwm-uninstall bspwm-install-requirement bspwm-uninstall-requirement bspwm-install-files bspwm-uninstall-files bspwm-install-session bspwm-check-display bspwm-restart \
	sxhkd-install sxhkd-uninstall sxhkd-install-requirement sxhkd-uninstall-requirement sxhkd-install-files sxhkd-uninstall-files sxhkd-generate \
	polybar-install polybar-uninstall polybar-install-requirement polybar-uninstall-requirement polybar-install-files polybar-uninstall-files \
	kitty-install kitty-uninstall kitty-install-requirement kitty-uninstall-requirement kitty-install-files kitty-uninstall-files \
	ranger-install ranger-uninstall ranger-install-requirement ranger-uninstall-requirement ranger-install-files ranger-uninstall-files \
	picom-install picom-uninstall picom-install-requirement picom-uninstall-requirement picom-install-files picom-uninstall-files \
	rofi-install rofi-uninstall rofi-install-requirement rofi-uninstall-requirement rofi-install-files rofi-uninstall-files \
	thunar-install thunar-uninstall thunar-install-requirement thunar-uninstall-requirement thunar-install-files thunar-uninstall-files \
	vscode-install vscode-uninstall vscode-install-requirement vscode-uninstall-requirement vscode-install-files vscode-uninstall-files \
	wm-base-install wm-base-uninstall wm-base-install-requirement wm-base-uninstall-requirement wm-base-install-files wm-base-uninstall-files \
	pulseaudio-install pulseaudio-uninstall pulseaudio-install-requirement pulseaudio-uninstall-requirement pulseaudio-install-files pulseaudio-uninstall-files \
	display-tools-install display-tools-uninstall display-tools-install-requirement display-tools-uninstall-requirement display-tools-install-files display-tools-uninstall-files \
	clock-set keyboard-set-latam \
	nvidia-install nvidia-uninstall nvidia-install-requirement nvidia-uninstall-requirement nvidia-install-files nvidia-uninstall-files

install-core: bspwm-install sxhkd-install polybar-install picom-install

wm-requirements-install: wm-base-install-requirement pulseaudio-install-requirement display-tools-install-requirement nvidia-install-requirement

remove-core: picom-uninstall polybar-uninstall sxhkd-uninstall bspwm-uninstall

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

sddm-install:
	@sudo pacman -S --needed --noconfirm sddm

sddm-enable:
	@sudo systemctl enable sddm.service --force

sddm-start:
	@sudo systemctl start sddm.service

bspwm-bootstrap: install-core bspwm-install-session

bspwm-install: bspwm-install-requirement bspwm-install-files
bspwm-uninstall: bspwm-uninstall-files bspwm-uninstall-requirement
bspwm-install-requirement:
	@$(RUN) --action install-requirement --program bspwm
bspwm-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program bspwm
bspwm-install-files:
	@$(RUN) --action install-files --program bspwm
bspwm-uninstall-files:
	@$(RUN) --action uninstall-files --program bspwm

bspwm-install-session:
	@./scripts/install_bspwm_session.sh

bspwm-check-display:
	@./scripts/check_display_stack.sh

bspwm-restart:
	@./scripts/check_display_stack.sh --quiet
	@if command -v bspc >/dev/null 2>&1; then \
		bspc wm -r; \
	else \
		echo "bspc no encontrado en PATH"; \
		exit 1; \
	fi

sxhkd-install: sxhkd-install-requirement sxhkd-install-files
sxhkd-uninstall: sxhkd-uninstall-files sxhkd-uninstall-requirement
sxhkd-install-requirement:
	@$(RUN) --action install-requirement --program sxhkd
sxhkd-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program sxhkd
sxhkd-install-files:
	@$(RUN) --action install-files --program sxhkd
	@./scripts/generate_sxhkd.sh
sxhkd-uninstall-files:
	@$(RUN) --action uninstall-files --program sxhkd

sxhkd-generate:
	@./scripts/generate_sxhkd.sh

polybar-install: polybar-install-requirement polybar-install-files
polybar-uninstall: polybar-uninstall-files polybar-uninstall-requirement
polybar-install-requirement:
	@$(RUN) --action install-requirement --program polybar
polybar-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program polybar
polybar-install-files:
	@$(RUN) --action install-files --program polybar
polybar-uninstall-files:
	@$(RUN) --action uninstall-files --program polybar

kitty-install: kitty-install-requirement kitty-install-files
kitty-uninstall: kitty-uninstall-files kitty-uninstall-requirement
kitty-install-requirement:
	@$(RUN) --action install-requirement --program kitty
kitty-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program kitty
kitty-install-files:
	@$(RUN) --action install-files --program kitty
kitty-uninstall-files:
	@$(RUN) --action uninstall-files --program kitty

ranger-install: ranger-install-requirement ranger-install-files
ranger-uninstall: ranger-uninstall-files ranger-uninstall-requirement
ranger-install-requirement:
	@$(RUN) --action install-requirement --program ranger
ranger-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program ranger
ranger-install-files:
	@$(RUN) --action install-files --program ranger
ranger-uninstall-files:
	@$(RUN) --action uninstall-files --program ranger

picom-install: picom-install-requirement picom-install-files
picom-uninstall: picom-uninstall-files picom-uninstall-requirement
picom-install-requirement:
	@$(RUN) --action install-requirement --program picom
picom-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program picom
picom-install-files:
	@$(RUN) --action install-files --program picom
picom-uninstall-files:
	@$(RUN) --action uninstall-files --program picom

rofi-install: rofi-install-requirement rofi-install-files
rofi-uninstall: rofi-uninstall-files rofi-uninstall-requirement
rofi-install-requirement:
	@$(RUN) --action install-requirement --program rofi
rofi-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program rofi
rofi-install-files:
	@$(RUN) --action install-files --program rofi
rofi-uninstall-files:
	@$(RUN) --action uninstall-files --program rofi

thunar-install: thunar-install-requirement thunar-install-files
thunar-uninstall: thunar-uninstall-files thunar-uninstall-requirement
thunar-install-requirement:
	@$(RUN) --action install-requirement --program thunar
thunar-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program thunar
thunar-install-files:
	@$(RUN) --action install-files --program thunar
thunar-uninstall-files:
	@$(RUN) --action uninstall-files --program thunar

vscode-install: vscode-install-requirement vscode-install-files
vscode-uninstall: vscode-uninstall-files vscode-uninstall-requirement
vscode-install-requirement:
	@$(RUN) --action install-requirement --program vscode
vscode-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program vscode
vscode-install-files:
	@$(RUN) --action install-files --program vscode
vscode-uninstall-files:
	@$(RUN) --action uninstall-files --program vscode

wm-base-install: wm-base-install-requirement wm-base-install-files
wm-base-uninstall: wm-base-uninstall-files wm-base-uninstall-requirement
wm-base-install-requirement:
	@$(RUN) --action install-requirement --program wm-base
wm-base-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program wm-base
wm-base-install-files:
	@$(RUN) --action install-files --program wm-base
wm-base-uninstall-files:
	@$(RUN) --action uninstall-files --program wm-base

pulseaudio-install: pulseaudio-install-requirement pulseaudio-install-files
pulseaudio-uninstall: pulseaudio-uninstall-files pulseaudio-uninstall-requirement
pulseaudio-install-requirement:
	@$(RUN) --action install-requirement --program pulseaudio
pulseaudio-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program pulseaudio
pulseaudio-install-files:
	@$(RUN) --action install-files --program pulseaudio
pulseaudio-uninstall-files:
	@$(RUN) --action uninstall-files --program pulseaudio

display-tools-install: display-tools-install-requirement display-tools-install-files
display-tools-uninstall: display-tools-uninstall-files display-tools-uninstall-requirement
display-tools-install-requirement:
	@$(RUN) --action install-requirement --program display-tools
display-tools-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program display-tools
display-tools-install-files:
	@$(RUN) --action install-files --program display-tools
display-tools-uninstall-files:
	@$(RUN) --action uninstall-files --program display-tools

clock-set:
	@PYTHONPATH=. python3 ./scripts/set_clock.py

keyboard-set-latam:
	@PYTHONPATH=. python3 ./scripts/set_keyboard_layout.py --layout latam

nvidia-install: nvidia-install-requirement nvidia-install-files
nvidia-uninstall: nvidia-uninstall-files nvidia-uninstall-requirement
nvidia-install-requirement:
	@$(RUN) --action install-requirement --program nvidia
nvidia-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program nvidia
nvidia-install-files:
	@$(RUN) --action install-files --program nvidia
nvidia-uninstall-files:
	@$(RUN) --action uninstall-files --program nvidia
