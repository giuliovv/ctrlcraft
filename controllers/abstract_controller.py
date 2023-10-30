from controllers.auto_tune import AutoTuner

class AbstractController:
    def __init__(self):
        """
        Initialize any basic properties for the controller.
        """
        pass

    def set_parameters(self, **kwargs):
        """
        Set or update controller parameters.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")

    def get_parameters(self):
        """
        Return the current set of controller parameters.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")

    def reset(self):
        """
        Reset any internal states or properties of the controller.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")

    def compute_action(self, state, derivative=None, reference=None):
        """
        Compute the control action based on the current state and possibly a reference.
        :param state: Current state of the system.
        :param reference: Desired state or reference signal.
        :return: Computed control action.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")

    def get_parameter_bounds(self):
        """
        This method should return a dictionary where
        - keys are parameter names
        - values are tuples of (lower_bound, upper_bound)
        """
        raise NotImplementedError

    def tune(self, env, n_trials=100, max_steps=30):
        tuner = AutoTuner(env, self, n_trials, max_steps)
        best_params = tuner.tune()
        self.reset()
        self.set_parameters(**best_params)
        return best_params