# This .spec config file tells Buildozer an app's requirements for being built.

[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,Cython==0.29.33

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) Permissions required by your app
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (str) Android NDK version to use (25b is required)
android.ndk = 25b

# (str) Path to Android NDK directory
android.ndk_path = /content/android-ndk-r25b

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Format used to package the app for release (aab or apk)
android.release_artifact = aab

# (str) Format used to package the app for debug (apk or aar)
android.debug_artifact = apk

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin
