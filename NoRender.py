import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(observation)
        print action
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
