from controllers.abstract_controller import AbstractController


class PIDController(AbstractController):
    def __init__(self, kp=0, ki=0, kd=0):
        super().__init__()
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def set_parameters(self, kp=None, ki=None, kd=None):
        if kp is not None:
            self.kp = kp
        if ki is not None:
            self.ki = ki
        if kd is not None:
            self.kd = kd

    def get_parameters(self):
        return {
            'kp': self.kp,
            'ki': self.ki,
            'kd': self.kd
        }

    def get_parameter_bounds(self):
        return {
            'kp': (0, 500),
            'ki': (0, 500),
            'kd': (0, 500)
        }

    def reset(self):
        self.previous_error = 0
        self.integral = 0

    def compute_action(self, state, derivative=None, reference=0):
        error = reference - state
        self.integral += error
        if derivative is None:
            derivative = error - self.previous_error
        action = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return action