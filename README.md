## Install

	pip install gym
	sudo apt install python-opengl

	sudo apt install xvfb
	pip install jupyter
	xvfb-run -s "-screen 0 1024x768x24" jupyter-notebook

	sudo apt install ffmpeg
	xvfb-run -s "-screen 0 1024x768x24" python Record.py

Ref:
https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server

Missing jupyter:

	whereis jupyter
	export PATH=$PATH:~/.local/bin

RL Example:

https://gist.github.com/yashpatel5400/2e481657f247f0695200e8ca92d4b5df#file-cartpole-py
