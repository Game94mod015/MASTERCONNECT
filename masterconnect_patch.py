#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(sys.argv[1]).resolve()
app = root / 'app'
if not app.is_dir():
    raise SystemExit('ERROR: upstream Open-SSTP-Client checkout does not contain app/')

# Android 13+ only.
build = app / 'build.gradle'
s = build.read_text(encoding='utf-8')
s = re.sub(r'(?m)^\s*applicationId\s+"[^"]+"', '        applicationId "com.masterconnect.sstp"', s)
s = re.sub(r'(?m)^\s*minSdk\s+\d+', '        minSdk 33', s)
s = re.sub(r'(?m)^\s*targetSdk\s+\d+', '        targetSdk 35', s)
build.write_text(s, encoding='utf-8')

# Brand strings without touching package/class names.
for p in root.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in {'.kt','.java','.xml','.md','.gradle','.kts'}:
        continue
    try:
        old = p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    new = old.replace('Open SSTP Client', 'MasterConnect')
    new = new.replace('Open-SSTP-Client', 'MasterConnect')
    if new != old:
        p.write_text(new, encoding='utf-8')

# Explicit app label fallback.
for p in app.rglob('AndroidManifest.xml'):
    old = p.read_text(encoding='utf-8')
    new = old.replace('android:label="@string/app_name"', 'android:label="MasterConnect"')
    if new != old:
        p.write_text(new, encoding='utf-8')

# Add a small branded palette; upstream theme/resources remain intact.
values = app / 'src/main/res/values'
values.mkdir(parents=True, exist_ok=True)
(values / 'masterconnect_brand.xml').write_text('''<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="masterconnect_accent">#7C5CFF</color>\n    <color name="masterconnect_cyan">#00D4FF</color>\n    <color name="masterconnect_background">#080A12</color>\n</resources>\n''', encoding='utf-8')

print('MasterConnect patch: OK')
print('  applicationId = com.masterconnect.sstp')
print('  minSdk = 33 (Android 13+)')
print('  targetSdk = 35')
