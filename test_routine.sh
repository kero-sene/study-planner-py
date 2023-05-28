#!/bin/zsh

coverage run -m unittest discover -v
coverage html
