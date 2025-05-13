import os
import subprocess
from termcolor import cprint

def runcmd(cmd, verbose = False, *args, **kwargs):
	process = subprocess.Popen(
		cmd,
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		text = True,
		shell = True,
	)
	std_out, std_err = process.communicate()
	if verbose:
		print(std_out.strip(), std_err)
	pass
	
c = os.getcwd()

VERSION = "go1.24.3.linux-amd64.tar.gz"

DESKTOP = os.path.normpath(os.path.expanduser("~/Desktop"))

if c != DESKTOP:
	os.chdir(DESKTOP)
	cprint(f'Changed dir to: {DESKTOP}', 'green')
	
cprint("Downloading the archive... ", 'green')
runcmd(f"wget https://go.dev/dl/{VERSION}", verbose = True)

cprint('Extracting to: "/usr/local"...', 'green')
runcmd(f"sudo tar -C /usr/local -xzf {VERSION}", verbose = True)

runcmd("echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/go.sh", verbose=True)
runcmd("sudo chmod +x /etc/profile.d/go.sh", verbose=True)

cprint("system-wide go-lang install...", 'green')
runcmd('echo \'export PATH="$PATH:/usr/local/go/bin"\' >> ~/.bashrc', verbose = True)

cprint("Refreshing the .bashrc file...", 'green')
runcmd('. ~/.bashrc', verbose = True)

cprint(f'Installed, version = {runcmd("PATH=$PATH:/usr/local/go/bin go version", verbose=True)}', 'green', attrs=['bold'])

