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

    def compute_action(self, state, reference=None):
        """
        Compute the control action based on the current state and possibly a reference.
        :param state: Current state of the system.
        :param reference: Desired state or reference signal.
        :return: Computed control action.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")
