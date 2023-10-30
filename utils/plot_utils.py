import matplotlib.pyplot as plt
import numpy as np

def plot_rewards(rewards_history):
    plt.plot(rewards_history)
    plt.xlabel('Episode')
    plt.ylabel('Rewards')
    plt.title('Reward History over Episodes')
    plt.grid(True)
    plt.show()

def cumplot_rewards(rewards_history):

    cumulative_values = np.cumsum(rewards_history)
    plt.plot(cumulative_values)
    plt.xlabel('Episode')
    plt.ylabel('Cumulative Reward')
    plt.title('Reward History over Episodes')
    plt.grid(True)
    plt.show()