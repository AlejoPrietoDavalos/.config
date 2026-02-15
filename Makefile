SHELL := /bin/bash
RUN := cd ./_wm && PYTHONPATH=./src python3 ./main.py

.PHONY: install-core remove-core remove-core-purge \
	bspwm-install bspwm-uninstall bspwm-install-requirement bspwm-uninstall-requirement bspwm-install-files bspwm-uninstall-files bspwm-install-session \
	sxhkd-install sxhkd-uninstall sxhkd-install-requirement sxhkd-uninstall-requirement sxhkd-install-files sxhkd-uninstall-files sxhkd-generate \
	polybar-install polybar-uninstall polybar-install-requirement polybar-uninstall-requirement polybar-install-files polybar-uninstall-files \
	ranger-install ranger-uninstall ranger-install-requirement ranger-uninstall-requirement ranger-install-files ranger-uninstall-files \
	picom-install picom-uninstall picom-install-requirement picom-uninstall-requirement picom-install-files picom-uninstall-files \
	rofi-install rofi-uninstall rofi-install-requirement rofi-uninstall-requirement rofi-install-files rofi-uninstall-files \
	thunar-install thunar-uninstall thunar-install-requirement thunar-uninstall-requirement thunar-install-files thunar-uninstall-files \
	vscode-install vscode-uninstall vscode-install-requirement vscode-uninstall-requirement vscode-install-files vscode-uninstall-files

install-core: bspwm-install sxhkd-install polybar-install

remove-core: polybar-uninstall sxhkd-uninstall bspwm-uninstall

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

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
	@./_wm/scripts/install_bspwm_session.sh

sxhkd-install: sxhkd-install-requirement sxhkd-install-files
sxhkd-uninstall: sxhkd-uninstall-files sxhkd-uninstall-requirement
sxhkd-install-requirement:
	@$(RUN) --action install-requirement --program sxhkd
sxhkd-uninstall-requirement:
	@$(RUN) --action uninstall-requirement --program sxhkd
sxhkd-install-files:
	@$(RUN) --action install-files --program sxhkd
	@./_wm/scripts/generate_sxhkd.sh
sxhkd-uninstall-files:
	@$(RUN) --action uninstall-files --program sxhkd

sxhkd-generate:
	@./_wm/scripts/generate_sxhkd.sh

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
