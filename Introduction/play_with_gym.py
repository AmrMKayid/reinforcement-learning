import gym


def test_envs(env_str):
	env = gym.make(env_str)
	print(env)
	print(env.action_space)
	print(env.observation_space)
	for i_episode in range(20):
		observation = env.reset()
		for t in range(100):
			env.render()
			# print(observation)
			action = env.action_space.sample()
			observation, reward, done, info = env.step(action)
			if done:
				print("Episode finished after {} timesteps".format(t+1))
				break
	env.close()


if __name__ == '__main__':
	# List all envs available in installation
	from gym import envs
	print(envs.registry.all())
	envs = ['Ant-v2', 'HandManipulateBlock-v0', 'Humanoid-v2', 'FetchPickAndPlace-v1', 'CartPole-v0', 'MountainCar-v0', 'MsPacman-v0', 'Hopper-v2']
	for env in envs:
		test_envs(env)