SHELL := /bin/bash
RUN := PYTHONPATH=. python3 ./main.py
PROGRAM ?=

PROGRAMS := bspwm sxhkd polybar kitty ranger picom rofi thunar vscode wm-base pulseaudio display-tools nvidia

# Usage: make <target> PROGRAM=<program>
define require_program
$(if $(strip $(PROGRAM)),,$(error Missing PROGRAM. Use: make <target> PROGRAM=<program>. Available: $(PROGRAMS)))
endef

.PHONY: \
	install uninstall install-requirement uninstall-requirement install-files uninstall-files \
	install-all install-core remove-core remove-core-purge wm-requirements-install \
	sddm-install sddm-enable sddm-start bspwm-bootstrap bspwm-install-session bspwm-check-display bspwm-restart \
	sxhkd-generate clock-set keyboard-set-latam scripts-chmod

install:
	$(call require_program)
	@$(RUN) --action install --program $(PROGRAM)

uninstall:
	$(call require_program)
	@$(RUN) --action uninstall --program $(PROGRAM)

install-requirement:
	$(call require_program)
	@$(RUN) --action install-requirement --program $(PROGRAM)

uninstall-requirement:
	$(call require_program)
	@$(RUN) --action uninstall-requirement --program $(PROGRAM)

install-files:
	$(call require_program)
	@$(RUN) --action install-files --program $(PROGRAM)
	@if [ "$(PROGRAM)" = "sxhkd" ]; then ./scripts/generate_sxhkd.sh; fi

uninstall-files:
	$(call require_program)
	@$(RUN) --action uninstall-files --program $(PROGRAM)

install-all:
	@$(RUN) --action dirty_install_all_packages

install-core:
	@$(MAKE) install PROGRAM=bspwm
	@$(MAKE) install PROGRAM=sxhkd
	@$(MAKE) install PROGRAM=polybar
	@$(MAKE) install PROGRAM=picom

remove-core:
	@$(MAKE) uninstall PROGRAM=picom
	@$(MAKE) uninstall PROGRAM=polybar
	@$(MAKE) uninstall PROGRAM=sxhkd
	@$(MAKE) uninstall PROGRAM=bspwm

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

wm-requirements-install:
	@$(MAKE) install-requirement PROGRAM=wm-base
	@$(MAKE) install-requirement PROGRAM=pulseaudio
	@$(MAKE) install-requirement PROGRAM=display-tools
	@$(MAKE) install-requirement PROGRAM=nvidia

sddm-install:
	@sudo pacman -S --needed --noconfirm sddm

sddm-enable:
	@sudo systemctl enable sddm.service --force

sddm-start:
	@sudo systemctl start sddm.service

bspwm-bootstrap: install-core bspwm-install-session

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

sxhkd-generate:
	@./scripts/generate_sxhkd.sh

clock-set:
	@PYTHONPATH=. python3 ./scripts/set_clock.py

keyboard-set-latam:
	@PYTHONPATH=. python3 ./scripts/set_keyboard_layout.py --layout latam

scripts-chmod:
	@find ./scripts -maxdepth 1 -type f -exec chmod +x {} +
