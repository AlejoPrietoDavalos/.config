#!/bin/bash

function start_signal {
    signal_name=$1
    signal_name_py=$signal_name.py
    signal_name_pid=$HOME/.config/_infra/tmp/$signal_name.pid

    # Si no existe el proceso, ejecuta.
    if ! pgrep -f $signal_name_py > /dev/null; then
        echo "Start signal: $signal_name_py"
        python3 $HOME/.config/_infra/signals/$signal_name_py >> $HOME/.config/_infra/tmp/signals.log &
    else
        execution_signal_pid=$(pgrep -f $signal_name_py)
        stored_signal_pid=$(cat $signal_name_pid)
        if [ "$execution_signal_pid" != "$stored_signal_pid" ]; then
            echo "Kill signal: $signal_name_py"
            kill $execution_signal_pid
            echo "Start signal: $signal_name_py"
            python3 $HOME/.config/_infra/signals/$signal_name_py >> $HOME/.config/_infra/tmp/signals.log &
        fi
    fi
}


signal_name="signal_set_wallpaper"
echo "~~~~> Start: $signal_name"
start_signal $signal_name >> $HOME/.config/_infra/tmp/signals.log
