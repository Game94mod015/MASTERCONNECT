# MasterConnect — Android 13+ SSTP

This repository is a small build wrapper for the MIT-licensed Open SSTP Client engine. GitHub Actions downloads the pinned upstream release **v1.10.2**, applies MasterConnect branding, sets `minSdk 33` (Android 13+) and builds a release APK.

## Features inherited from the SSTP engine

- SSTP / MS-SSTP VPN
- Android `VpnService`
- Host / Username / Password
- PAP and MS-CHAPv2 authentication
- IPv4 / IPv6 PPP options
- Custom DNS
- Trusted certificates
- App-based VPN rules
- VPN routing / default route
- Saved profiles
- Quick Settings tile
- Foreground VPN service

The upstream project documents these capabilities and is MIT licensed:
https://github.com/kittoku/Open-SSTP-Client

## Build

1. Create a **public** GitHub repository.
2. Upload every file from this folder, including `.github/workflows/build.yml`.
3. Open **Actions** → **Build MasterConnect APK**.
4. Click **Run workflow**.
5. When it finishes, open the run and download the artifact named `MasterConnect-Android13Plus`.

No AndroidIDE or Termux is needed for the GitHub build.

## Important

The app does not invent VPN credentials from `https://ipspeed.info/`. A configuration importer should only consume an endpoint that actually provides valid SSTP host, username and password data.
