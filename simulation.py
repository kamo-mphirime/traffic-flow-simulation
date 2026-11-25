"""
Author: Kamo Mphirime
Starting Date: 11/14/2026

Initial creation by Dietrich Geisler on 10/25/2025

Implementation of a simple traffic stop simulation
"""

# Imports and constant definitions
import random

# How much time it takes to go from one light to the next
LIGHT_TRAVEL_TIME = 15

# Travel variation to account for faster or slower cars
TRAVEL_VARIATION = 5

# The random variation (in time steps) between when cars enter the simulation
SPAWN_VARIATION = 3


# Part 1: Light
# ----------------------------------------------

class Light:
    """
    Defines a traffic light with a queue of waiting cars

    Attributes:
        is_green: True if this light is green, and False otherwise
        max_countdown: How many total timesteps between each light switch
        countdown: How many timesteps until this light switches between Red and Green
        queue: A queue of Cars looking to pass through this traffic light
    """
    is_green: bool
    max_countdown: int
    countdown: int
    queue: list['Car']

    def __init__(self, max_countdown: int, initial_countdown: int):
        """Constructor for Light

        Initially sets this light to be Red (is_green to False)
        Also sets the light queue to be empty

        Arguments:
            max_countdown: How many total timesteps between each light switch
                           Must be a positive non-zero number
            initial_countdown: How many timesteps until the first light switch
                              Must be a positive non-zero number
        """
        assert type(max_countdown) == int
        assert type(initial_countdown) == int
        assert max_countdown > 0
        assert initial_countdown > 0

        self.is_green = False
        self.max_countdown = max_countdown
        self.countdown = initial_countdown
        self.queue = []

    def __str__(self) -> str:
        """Returns a string representation of this Light"""

        color = 'Green' if self.is_green else 'Red'
        return f'{color} Light'

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Light"""

        return f'Light(is_green={self.is_green}, ' + \
            f'max_countdown={self.max_countdown}, ' + \
            f'countdown={self.countdown}, ' + \
            f'queue_length={self.queue_length()})'

    def add_car_to_queue(self, car: 'Car'):
        """Adds a Car to the queue of Cars waiting at this Light"""

        self.queue.append(car)
        return

    def queue_length(self) -> int:
        """Returns the number of Cars waiting in this Light's queue"""


        return len(self.queue)

    def advance_queue(self) -> 'Car':
        """Advances the queue of this Light by one and returns the passing car

        Recall that a queue allows the car that arrived first to pass through first
        This function errors if there are no Cars in the queue

        HINT: you can use an assert to error explicitly,
              or you can call a built-in list function that produces
