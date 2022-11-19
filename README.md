# msdorkdump

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="left">
  <img src="/images/dorkdump.png" />
</p>

MSDorkDump is a Google Dork File Finder that queries a specified domain name and variety of file extensions (pdf, doc, docx, etc), downloads , and then runs Exiftool on them to enumerate metadata. Note that due to Google's built in rate limiting, queries may end up timed out if too many are made in a short amount of time.

The goal is to implement some custom tooling into a "MayorSec Toolkit" to be released sometime in the future.

## Usage
Installing MSDorkDump

```git clone https://github.com/dievus/msdorkdump.git```

Change directories to msdorkdump and run:

```pip3 install -r requirements.txt```

This will run the install script to add necessary dependencies to your system.

### Linux Users

Linux users MUST install Exiftool directly to their system.
```sudo apt install libimage-exiftool-perl```

### Windows Users

Windows users can download the ZIP file and extract it locally.  Do not move any files as Exiftool calls from the /tools directory.

You can then run:

```python3 msdorkdump.py -t <domain> -d```

And that's it!
