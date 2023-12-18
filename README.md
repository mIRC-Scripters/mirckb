[![Documentation Status](https://readthedocs.org/projects/mirckb/badge/?version=latest)](https://mirckb.readthedocs.io/en/latest/?badge=latest)

# mIRCKB
mIRC Knowledge Base

Build with Sphinx and ReStructered Text

Project page:	https://readthedocs.org/projects/mirckb/  
Webpage: https://docs.mircscripting.org  		
Webpage: https://mirckb.readthedocs.io/

This project is WIP (Work In Progress)

# Steps for getting up to speed in Windows
* Install chocolatey: https://chocolatey.org/install#individual
* Install sphinx: `choco install sphinx`
* Clone the mirckb repository to a dir on your machine
* Change directory to the local mirckb dir and run: `pip install -r requirements.txt --user`
* Run sphinx build in the cloned dir on your machine: `sphinx-build docs\source docs\build`
* Open up the index webpage: `docs\build\index.html`
