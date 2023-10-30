import gymnasium as gym
import numpy as np

from controllers import PIDController
from utils.plot_utils import cumplot_rewards, generate_gif, display_gif

def main():
    # Initialize environment
    env = gym.make('Pendulum-v1', render_mode="rgb_array")

    max_steps = 100
    
    # Initialize controller
    controller = PIDController()
    controller.tune(env, n_trials=1000, max_steps=max_steps)
    
    # Simulation loop
    state, info = env.reset()
    done = False
    rewards = []
    frames = []
    for _ in range(max_steps):
        frame = env.render()
        frames.append(frame)
        cos_theta, sin_theta, theta_dot = state
        theta = np.arctan2(sin_theta, cos_theta)
        control_action = controller.compute_action(theta, derivative=theta_dot, reference=0)
        state, reward, done, truncated, _ = env.step([control_action])
        rewards.append(reward)
        if done:
            break

    # Visualize
    cumplot_rewards(rewards)
    generate_gif(frames)
    display_gif()
        
    env.close()

if __name__ == '__main__':
    main()