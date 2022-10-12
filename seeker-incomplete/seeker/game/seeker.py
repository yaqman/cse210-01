import random

class Seeker:
    def __init__(self):
         """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """

         self._location = random.randint(1, 1000)
        
    def get_location(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        return self._location
        
    def move_location(self, location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = location
