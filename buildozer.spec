[app]

# App name
title = School Project Demo

# Package name
package.name = schoolproject

# Package domain
package.domain = org.example

# Your Python file
source.dir = .

# Python entry point
source.include_exts = py,png,jpg,jpeg,kv,atlas

# Version
version = 1.0

# Requirements
requirements = python3,kivy

# Screen orientation
orientation = portrait

# Full screen
fullscreen = 0


[buildozer]

# Log level
log_level = 2

# Warning if running as root
warn_on_root = 1


[app:android]

# Android permissions
android.permissions = INTERNET

# Android API settings
android.api = 35
android.minapi = 21

# Architecture
android.arch = arm64-v8a

# APK format
android.entrypoint = org.kivy.android.PythonActivity
