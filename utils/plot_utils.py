import logging

import imageio
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

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

def generate_gif(frames, path='./animations/animation.gif', duration=0.1):
    logging.info(f"Saving gif...")
    imageio.mimsave(path, frames, duration=duration)

def display_gif(path='./animations/animation.gif'):
    """Display GIF using matplotlib."""
    logging.info(f"Showing gif")
    # Load GIF
    gif = imageio.get_reader(path)
    num_frames = gif.get_length()

    # Display the first frame
    fig, ax = plt.subplots()
    img = ax.imshow(gif.get_data(0))

    # Function to update the frame
    def update(i):
        img.set_data(gif.get_data(i))
        return (img,)

    # Function to close the plot once the animation is done
    def on_animation_end(event):
        plt.close(fig)

    # Animate the GIF using FuncAnimation
    metadata = gif.get_meta_data()
    interval = metadata.get('duration', 100)  # default to 100ms if no duration is found
    from matplotlib.animation import FuncAnimation
    ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True, repeat=False)

    # ani._stop = on_animation_end  # Override the _stop method to close the figure
    plt.show()