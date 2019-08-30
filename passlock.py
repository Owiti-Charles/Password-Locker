class User:
    """
    Create User class that generates new instances of a user.

    """
    user = []
    
    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password