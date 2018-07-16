import gym
import time

env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    if done == True:
        print('resetado')
        env.reset()
    env.render()
    env.step(env.action_space.sample()) # take a random action
    time.sleep(0.05)
