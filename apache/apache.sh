#!/usr/bin/env bash

function stop() {
  apache2ctl graceful-stop
  exit $?
}

trap stop SIGTERM

apache2ctl -D FOREGROUND &

wait $!