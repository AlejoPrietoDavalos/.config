SHELL := /bin/bash
RUN := cd ./_wm && PYTHONPATH=./src python3 ./main.py

.PHONY: install-core remove-core remove-core-purge \
	install-bspwm uninstall-bspwm install-requirement-bspwm uninstall-requirement-bspwm install-files-bspwm uninstall-files-bspwm install-session-bspwm \
	install-sxhkd uninstall-sxhkd install-requirement-sxhkd uninstall-requirement-sxhkd install-files-sxhkd uninstall-files-sxhkd generate-sxhkd \
	install-polybar uninstall-polybar install-requirement-polybar uninstall-requirement-polybar install-files-polybar uninstall-files-polybar \
	install-ranger uninstall-ranger install-requirement-ranger uninstall-requirement-ranger install-files-ranger uninstall-files-ranger \
	install-picom uninstall-picom install-requirement-picom uninstall-requirement-picom install-files-picom uninstall-files-picom \
	install-rofi uninstall-rofi install-requirement-rofi uninstall-requirement-rofi install-files-rofi uninstall-files-rofi \
	install-thunar uninstall-thunar install-requirement-thunar uninstall-requirement-thunar install-files-thunar uninstall-files-thunar \
	install-vscode uninstall-vscode install-requirement-vscode uninstall-requirement-vscode install-files-vscode uninstall-files-vscode

install-core: install-bspwm install-sxhkd install-polybar

remove-core: uninstall-polybar uninstall-sxhkd uninstall-bspwm

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

install-bspwm: install-requirement-bspwm install-files-bspwm
uninstall-bspwm: uninstall-files-bspwm uninstall-requirement-bspwm
install-requirement-bspwm:
	@$(RUN) --action install-requirement --program bspwm
uninstall-requirement-bspwm:
	@$(RUN) --action uninstall-requirement --program bspwm
install-files-bspwm:
	@$(RUN) --action install-files --program bspwm
uninstall-files-bspwm:
	@$(RUN) --action uninstall-files --program bspwm

install-session-bspwm:
	@./_wm/scripts/install_bspwm_session.sh

install-sxhkd: install-requirement-sxhkd install-files-sxhkd
uninstall-sxhkd: uninstall-files-sxhkd uninstall-requirement-sxhkd
install-requirement-sxhkd:
	@$(RUN) --action install-requirement --program sxhkd
uninstall-requirement-sxhkd:
	@$(RUN) --action uninstall-requirement --program sxhkd
install-files-sxhkd:
	@$(RUN) --action install-files --program sxhkd
	@./_wm/scripts/generate_sxhkd.sh
uninstall-files-sxhkd:
	@$(RUN) --action uninstall-files --program sxhkd

generate-sxhkd:
	@./_wm/scripts/generate_sxhkd.sh

install-polybar: install-requirement-polybar install-files-polybar
uninstall-polybar: uninstall-files-polybar uninstall-requirement-polybar
install-requirement-polybar:
	@$(RUN) --action install-requirement --program polybar
uninstall-requirement-polybar:
	@$(RUN) --action uninstall-requirement --program polybar
install-files-polybar:
	@$(RUN) --action install-files --program polybar
uninstall-files-polybar:
	@$(RUN) --action uninstall-files --program polybar

install-ranger: install-requirement-ranger install-files-ranger
uninstall-ranger: uninstall-files-ranger uninstall-requirement-ranger
install-requirement-ranger:
	@$(RUN) --action install-requirement --program ranger
uninstall-requirement-ranger:
	@$(RUN) --action uninstall-requirement --program ranger
install-files-ranger:
	@$(RUN) --action install-files --program ranger
uninstall-files-ranger:
	@$(RUN) --action uninstall-files --program ranger

install-picom: install-requirement-picom install-files-picom
uninstall-picom: uninstall-files-picom uninstall-requirement-picom
install-requirement-picom:
	@$(RUN) --action install-requirement --program picom
uninstall-requirement-picom:
	@$(RUN) --action uninstall-requirement --program picom
install-files-picom:
	@$(RUN) --action install-files --program picom
uninstall-files-picom:
	@$(RUN) --action uninstall-files --program picom

install-rofi: install-requirement-rofi install-files-rofi
uninstall-rofi: uninstall-files-rofi uninstall-requirement-rofi
install-requirement-rofi:
	@$(RUN) --action install-requirement --program rofi
uninstall-requirement-rofi:
	@$(RUN) --action uninstall-requirement --program rofi
install-files-rofi:
	@$(RUN) --action install-files --program rofi
uninstall-files-rofi:
	@$(RUN) --action uninstall-files --program rofi

install-thunar: install-requirement-thunar install-files-thunar
uninstall-thunar: uninstall-files-thunar uninstall-requirement-thunar
install-requirement-thunar:
	@$(RUN) --action install-requirement --program thunar
uninstall-requirement-thunar:
	@$(RUN) --action uninstall-requirement --program thunar
install-files-thunar:
	@$(RUN) --action install-files --program thunar
uninstall-files-thunar:
	@$(RUN) --action uninstall-files --program thunar

install-vscode: install-requirement-vscode install-files-vscode
uninstall-vscode: uninstall-files-vscode uninstall-requirement-vscode
install-requirement-vscode:
	@$(RUN) --action install-requirement --program vscode
uninstall-requirement-vscode:
	@$(RUN) --action uninstall-requirement --program vscode
install-files-vscode:
	@$(RUN) --action install-files --program vscode
uninstall-files-vscode:
	@$(RUN) --action uninstall-files --program vscode
