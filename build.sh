#!/bin/bash

# Regenerate from scratch
rm -rf site/*
mkdocs build
