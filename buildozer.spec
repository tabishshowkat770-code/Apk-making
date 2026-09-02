[app]

# App name
title = School Project Demo

# Package name
package.name = schoolproject

# Package domain
package.domain = org.example

# Your Python file
source.dir = .

# File extensions to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# Version
version = 1.0

# Requirements (explicit python version prevents build breaks)
requirements = python3==3.10.12,kivy

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

# Android API settings (Set to 33 for stable Buildozer compilation)
android.api = 33
android.minapi = 21

# Architecture (Include v7a alongside v8a for proper dependency linking)
android.archs = arm64-v8a, armeabi-v7a

# Allow accepting SDK licenses automatically
android.accept_sdk_license = True

# APK format
android.entrypoint = org.kivy.android.PythonActivity
