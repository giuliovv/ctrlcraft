import logging

import numpy as np
import optuna

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
optuna.logging.set_verbosity(optuna.logging.CRITICAL)

class AutoTuner:
    def __init__(self, env, controller, n_trials=100, max_steps=30):
        self.env = env
        self.controller = controller
        self.n_trials = n_trials
        self.max_steps = max_steps

    def _objective(self, trial):
        # Dynamically get parameter bounds from the controller
        parameter_bounds = self.controller.get_parameter_bounds()
        
        parameters = {}
        for param, (low, high) in parameter_bounds.items():
            parameters[param] = trial.suggest_float(param, low, high)
        
        self.controller.reset()
        self.controller.set_parameters(**parameters)
        cumulative_reward = self._run_episode_with_controller(self.controller)
        return -cumulative_reward

    def _run_episode_with_controller(self, controller):
        state, info = self.env.reset()
        rewards = 0
        for _ in range(self.max_steps):
            # TODO generalize this or pass it to the user. Currenlty specific for Pendulum
            cos_theta, sin_theta, theta_dot = state
            angle = np.arctan2(sin_theta, cos_theta)
            ###################################################
            control_action = controller.compute_action(angle, reference=0)
            state, reward, done, truncated, _ = self.env.step([control_action])
            rewards += reward
            if done:
                break
        return rewards

    def tune(self):
        study = optuna.create_study(direction='minimize')
        study.optimize(self._objective, n_trials=self.n_trials, show_progress_bar=True)
        logging.info(f"Tuning completed! Best parameters: {study.best_params}")
        return study.best_params