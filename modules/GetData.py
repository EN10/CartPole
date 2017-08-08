import gym
import numpy as np
env = gym.make('CartPole-v0')

trainingX, trainingY = [], []
scores = []

for i_episode in range(10000):
    observation = env.reset()
    score = 0
    training_sampleX, training_sampleY = [], []
    for t in range(500):
        action = env.action_space.sample()
        one_hot_action = np.zeros(2)
	one_hot_action[action] = 1
	training_sampleX.append(observation)
	training_sampleY.append(one_hot_action)

        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            break

    if score > 50:
        scores.append(score)
	trainingX += training_sampleX
	trainingY += training_sampleY
        
trainingX, trainingY = np.array(trainingX), np.array(trainingY)
print(np.mean(scores))
