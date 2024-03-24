#!/bin/bash

path_bspwm_log=$HOME/.config/bspwm/_bspwm.log
echo "----------------------------------" >> $path_bspwm_log 2>&1
echo "----------------------------------" >> $path_bspwm_log 2>&1
exec bspwm >> $path_bspwm_log 2>&1
