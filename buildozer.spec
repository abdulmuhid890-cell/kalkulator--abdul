[app]

# (str) Title of your application
title = Kalkulator Abdul

# (str) Package name
package.name = kalkulatorabdul

# (str) Package domain (needed for android packaging)
package.domain = org.abdul

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# SANGAT PENTING: Dikunci di versi stabil agar tidak memicu eror 3.14.2 lagi
requirements = python3==3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip apply patch widgets
android.skip_update = False

# (bool) Accept SDK license without identifying manually
android.accept_sdk_license = True

# (list) Architecture to build for (e.g. armeabi-v7a, arm64-v8a)
android.archs = armeabi-v7a, arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
