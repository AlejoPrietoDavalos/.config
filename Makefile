SHELL := /bin/bash

.PHONY: help install-core remove-core remove-core-purge \
	install-bspwm remove-bspwm install-session-bspwm \
	install-sxhkd remove-sxhkd generate-sxhkd \
	install-polybar remove-polybar \
	install-ranger remove-ranger \
	install-picom remove-picom \
	install-rofi remove-rofi \
	install-thunar remove-thunar

help:
	@echo "Targets:"
	@echo "  make install-core"
	@echo "  make remove-core"
	@echo "  make install-bspwm | remove-bspwm | install-session-bspwm"
	@echo "  make install-sxhkd | remove-sxhkd | generate-sxhkd"
	@echo "  make install-polybar | remove-polybar"
	@echo "  make install-ranger | remove-ranger"
	@echo "  make install-picom | remove-picom"
	@echo "  make install-rofi | remove-rofi"
	@echo "  make install-thunar | remove-thunar"
	@echo "  make remove-core-purge   # also removes pacman packages"
	@echo "  WM_REMOVE_PACKAGES=1 make remove-<program>"

install-core: install-bspwm install-sxhkd install-polybar

remove-core: remove-polybar remove-sxhkd remove-bspwm

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

install-bspwm:
	@./_wm/scripts/link_program.sh bspwm

remove-bspwm:
	@./_wm/scripts/unlink_program.sh bspwm

install-session-bspwm:
	@./_wm/scripts/install_bspwm_session.sh

install-sxhkd:
	@./_wm/scripts/link_program.sh sxhkd
	@./_wm/scripts/generate_sxhkd.sh

remove-sxhkd:
	@./_wm/scripts/unlink_program.sh sxhkd

generate-sxhkd:
	@./_wm/scripts/generate_sxhkd.sh

install-polybar:
	@./_wm/scripts/link_program.sh polybar

remove-polybar:
	@./_wm/scripts/unlink_program.sh polybar

install-ranger:
	@./_wm/scripts/link_program.sh ranger

remove-ranger:
	@./_wm/scripts/unlink_program.sh ranger

install-picom:
	@./_wm/scripts/link_program.sh picom

remove-picom:
	@./_wm/scripts/unlink_program.sh picom

install-rofi:
	@./_wm/scripts/link_program.sh rofi

remove-rofi:
	@./_wm/scripts/unlink_program.sh rofi

install-thunar:
	@./_wm/scripts/link_program.sh thunar

remove-thunar:
	@./_wm/scripts/unlink_program.sh thunar
