def GetData(env):
        trainingX, trainingY = [], []
        scores = []

        for i_episode in range(10000): #trials
                observation = env.reset()
                score = 0
                training_sampleX, training_sampleY = [], []

                for t in range(500): #sim_steps
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
        return trainingX, trainingY

from keras.models import Sequential
from keras.layers import Dense

def CreateModel():
        model = Sequential()
        model.add(Dense(2, input_shape=(4,), activation="softmax"))

        model.compile(
                loss="categorical_crossentropy",
                optimizer="adam",
                metrics=["accuracy"])
        return model

import gym
import numpy as np

def predict():
        env = gym.make("CartPole-v0")
        trainingX, trainingY = GetData(env)
        model = CreateModel()
        model.fit(trainingX, trainingY, epochs=5)

        from gym import wrappers                                        # Output MP4
        env = wrappers.Monitor(env, '/tmp/cartpole-experiment-1')       # Output MP4

        scores = []
        for _ in range(50): #trials
                observation = env.reset()
                score = 0
                for step in range(500): #sim_steps
                        env.render()                                    # Output MP4
                        action = np.argmax(model.predict(observation.reshape(1,4)))
                        observation, reward, done, _ = env.step(action)
                        score += reward
                        if done:
                                break
                scores.append(score)
        print(np.mean(scores))

if __name__ == "__main__":
        predict()
