# (str) Title of your application
title = MeetingMinutes

# (str) Package name
package.name = meetingminutes

# (str) Package domain (use a unique domain)
package.domain = com.example.meetingminutes

# (str) Source code directory
source.include_exts = py,png,jpg,kv,atlas

# (str) Your application version
version = 1.0

# (str) Android API level (Make sure it's compatible with the latest Android)
android.api = 33

# (list) Permissions your app requires
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
[app]
title = MeetingMinutesApp
package.name = meetingminutes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,whisper,openai,docx
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 30

[buildozer]
log_level = 2
warn_on_root = 1

[android]
package.format = apk

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
