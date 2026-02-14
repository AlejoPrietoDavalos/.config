SHELL := /bin/bash

.PHONY: install-core remove-core remove-core-purge \
	install-bspwm remove-bspwm install-session-bspwm \
	install-sxhkd remove-sxhkd generate-sxhkd \
	install-polybar remove-polybar \
	install-ranger remove-ranger \
	install-picom remove-picom \
	install-rofi remove-rofi \
	install-thunar remove-thunar

install-core: install-bspwm install-sxhkd install-polybar

remove-core: remove-polybar remove-sxhkd remove-bspwm

remove-core-purge:
	@WM_REMOVE_PACKAGES=1 $(MAKE) remove-core

install-bspwm:
	@./_wm/scripts/link_unlink_file.sh install bspwm

remove-bspwm:
	@./_wm/scripts/link_unlink_file.sh remove bspwm

install-session-bspwm:
	@./_wm/scripts/install_bspwm_session.sh

install-sxhkd:
	@./_wm/scripts/link_unlink_file.sh install sxhkd
	@./_wm/scripts/generate_sxhkd.sh

remove-sxhkd:
	@./_wm/scripts/link_unlink_file.sh remove sxhkd

generate-sxhkd:
	@./_wm/scripts/generate_sxhkd.sh

install-polybar:
	@./_wm/scripts/link_unlink_file.sh install polybar

remove-polybar:
	@./_wm/scripts/link_unlink_file.sh remove polybar

install-ranger:
	@./_wm/scripts/link_unlink_file.sh install ranger

remove-ranger:
	@./_wm/scripts/link_unlink_file.sh remove ranger

install-picom:
	@./_wm/scripts/link_unlink_file.sh install picom

remove-picom:
	@./_wm/scripts/link_unlink_file.sh remove picom

install-rofi:
	@./_wm/scripts/link_unlink_file.sh install rofi

remove-rofi:
	@./_wm/scripts/link_unlink_file.sh remove rofi

install-thunar:
	@./_wm/scripts/link_unlink_file.sh install thunar "$(HOME)/.config/Thunar"

remove-thunar:
	@./_wm/scripts/link_unlink_file.sh remove thunar "$(HOME)/.config/Thunar"
