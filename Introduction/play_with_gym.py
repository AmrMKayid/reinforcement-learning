import gym

def test_envs(env_str):
	env = gym.make(env_str)
	env.reset()
	for _ in range(500):
	    env.render()
	    env.step(env.action_space.sample()) # take a random action
	env.close()


envs = ['CartPole-v0', 'MountainCar-v0', 'MsPacman-v0'] #, 'Hopper-v2']
for env in envs:
	test_envs(env)