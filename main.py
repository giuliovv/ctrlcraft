import gym
from controllers import PIDController

def main():
    # Initialize environment
    env = gym.make('Pendulum-v0')
    
    # Initialize controller
    controller = PIDController(kp=1.0, ki=0.5, kd=0.1)
    
    # Simulation loop
    state = env.reset()
    done = False
    while not done:
        env.render()
        control_action = controller.control(state, reference=0)
        state, reward, done, _ = env.step(control_action)
        
    env.close()

if __name__ == '__main__':
    main()