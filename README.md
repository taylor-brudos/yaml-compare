# yaml-compare
Python script to compare Github members/repos with the YAML files that are used with Docker/TFE for Github organization administration so that anything missing from TFE can be imported.


STEPS:

Install Python 3 and dependencies: PyGithub and pyyaml

Add your Github access token (line 9) and organization name (line 15) within the script

Copy the most recent membership.yaml and repository.yaml files and place them in the same folder as compare.py

python compare.py

Output will be printed to your terminal
