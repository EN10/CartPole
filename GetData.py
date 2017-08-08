import gym
env = gym.make('CartPole-v0')

trainingX, trainingY = [], []
scores = []

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        action = env.action_space.sample()

        observation, reward, done, info = env.step(action)
        if done:
            break
