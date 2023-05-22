#!/bin/zsh

coverage run -m unittest discover -v
coverage report -m
