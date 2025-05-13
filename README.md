### GoLang Download Script ###

This script allows you to easily download and install GoLang on any Linux distribution.

## Prerequisites ##

Before running the script, make sure you have the following tools installed:
1. **wget**
2. **tar**

You can install them with the following commands:

On **Ubuntu/Debian**-based systems:
```bash
sudo apt update
sudo apt install wget tar
```
On **Fedora/Red** Hat-based systems:
```bash
sudo dnf install wget tar
```
On **Arch** Linux:
```bash
sudo pacman -S wget tar
```
## Installation ##
1. Clone this repository:
```bash
git clone https://github.com/yourusername/gol-download-script.git
cd gol-download-script
```

2. Run the script to download & install **GoLang**:
```bash
python3 script.py
```

The script will:

Download the latest **GoLang** archive,
Extract it to /usr/local,
Update your system PATH to include the Go binary directory.
