#!/bin/bash
ffmpeg -i check1.ogg check1.wav
sox check1.wav -r 16000 audio.wav
exit 1
