#!/bin/bash
terminator -l web -g terminator.conf
# cleanup after the user closes the terminator window
docker compose down
