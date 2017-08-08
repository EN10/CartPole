import gym
env = gym.make("CartPole-v0")

trainingX, trainingY = GetData(env)

model = NN()
model.fit(trainingX, trainingY, epochs=5)
	
scores = []

for _ in range(50): #trials
	observation = env.reset()
	score = 0
        for step in range(500): #sim_steps
		action = np.argmax(model.predict(observation.reshape(1,4)))
		observation, reward, done, _ = env.step(action)
		score += reward
		if done:
			break
	scores.append(score)

print(np.mean(scores))
