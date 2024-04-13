class Environment:

    """
    Reset environment to a new grain field. If no field has been created a field will be initialized.
    Is called before any action is made.
    Returns the initial state variables of the field.
    """

    def reset(self):
        # Todo
        return observation

    """
    Action is taken and state variables are updated according to environment rules.
    Reward gained from the time step is returned.
    If action is the last time step in the field terminated returns true
    """

    def step(self, action):
        #Todo
        return observation, reward, terminated

    """
    Returns the reward earned from time step
    """

    def get_reward(self, observation, action):
        #Optional helper method for step()
        return reward

    """
    Update state based on action according to envrionment rules.
    """

    def update_state(self, observation, action):
        #Optional helper method for step()
        return observation

    """
    Checks if the environment completed its last time step. 
    """

    def is_terminated(self):
        #Optional helper method for step()
        return terminated

    """
    observation -> numpy array
    reward -> float
    terminated -> boolean
    """

