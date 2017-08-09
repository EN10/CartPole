https://gym.openai.com/docs  
https://github.com/openai/gym/wiki/CartPole-v0

## Install

	pip install gym

**Render Requirements:**

	sudo apt install xvfb
	sudo apt install python-opengl

**Render to jupyter:**  
	pip install jupyter
	xvfb-run -s "-screen 0 1024x768x24" jupyter-notebook Render-matplotlib.ipynb  

**Render to MP4:**  

	sudo apt install ffmpeg
	xvfb-run -s "-screen 0 1024x768x24" python RenderToMP4.py

Gym NoRender.py `print(observation)` 

**Tensorflow**

	pip install tensorflow 

**Keras**  
Needed on C9: `sudo apt install python-dev`
	
	pip install keras

Simple RL.py `GetData() CreateModel() predict()` 

Visualise RLtoMP4.py `wrappers.Monitor ...`

**Performance**

https://github.com/EN10/TensorFlow-For-Poets/blob/master/tensorflow-1.2.1-cp27-none-linux_x86_64.whl

Ref:  

https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server

Missing jupyter:

	whereis jupyter
	export PATH=$PATH:~/.local/bin

RL Example:

https://medium.com/@yashpatel_86510/reinforcement-learning-w-keras-openai-698add10b4eb
https://gist.github.com/yashpatel5400/2e481657f247f0695200e8ca92d4b5df#file-cartpole-py