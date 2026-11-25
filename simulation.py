"""
Author: Kamo Mphirime
Starting Date: 11/14/2026

Implementation of a simple traffic stop simulation
"""

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
        assert isinstance(max_countdown, int)
        assert isinstance(initial_countdown, int)
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
        return (
            f'Light(is_green={self.is_green}, '
            f'max_countdown={self.max_countdown}, '
            f'countdown={self.countdown}, '
            f'queue_length={self.queue_length()})'
        )

    def add_car_to_queue(self, car: 'Car'):
        """Adds a Car to the queue of Cars waiting at this Light"""
        self.queue.append(car)

    def queue_length(self) -> int:
        """Returns the number of Cars waiting in this Light's queue"""
        return len(self.queue)

    def advance_queue(self) -> 'Car':
        """Advances the queue of this Light by one and returns the passing car

        Returns:
            The Car that was removed from the queue
        """
        assert len(self.queue) != 0
        return self.queue.pop(0)

    def can_go(self) -> bool:
        """Indicates whether or not cars can pass through this Light

        Cars can only pass through this Light if the Light is green and
        at least one timestep has passed since this Light turned green
        (simulating driver reaction time).

        Returns:
            True if Cars can pass through this Light, and False otherwise
        """
        return self.is_green and self.countdown < self.max_countdown

    def timestep(self):
        """Advances time for this Light by a single timestep (3 seconds of real time)"""
        self.countdown -= 1

        if self.countdown == 0:
            self.is_green = not self.is_green
            self.countdown = self.max_countdown


# Part 2: Car
# ----------------------------------------------

class Car:
    """Represents a single Car driving through traffic lights

    Attributes:
        current_light: The Light this Car is currently stopped at,
                       or None if currently traveling to the next Light
        remaining_lights: An ordered list of all Lights this Car must still pass through
        travel_time: The number of timesteps until this Car reaches the next Light
    """
    current_light: Light | None
    remaining_lights: list[Light]
    travel_time: int

    def __init__(self, lights: list[Light]):
        """Constructor for the Car object"""
        assert isinstance(lights, list)
        for light in lights:
            assert isinstance(light, Light)

        self.current_light = None
        self.remaining_lights = lights
        self.travel_time = 1

    def __str__(self) -> str:
        """Returns a string representation of this Car"""
        return 'Car'

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Car"""
        return (
            f'Car(current_light={self.current_light}, '
            f'num_remaining_lights={len(self.remaining_lights)}, '
            f'travel_time={self.travel_time})'
        )

    def number_of_lights(self) -> int:
        """Returns the number of Lights this Car must still pass through"""
        return len(self.remaining_lights)

    def is_at_light(self) -> bool:
        """Returns whether or not this Car is currently stopped at a Light"""
        return self.current_light is not None

    def start_going(self):
        """Updates this Car to stop waiting at the current Light and travel to the next"""
        self.current_light = None
        self.travel_time = random.randint(
            LIGHT_TRAVEL_TIME, LIGHT_TRAVEL_TIME + TRAVEL_VARIATION
        )

    def timestep(self):
        """Advances time for this Car by a single timestep (3 seconds of real time)"""
        if self.current_light is None:
            self.travel_time -= 1
            if self.travel_time == 0:
                assert len(self.remaining_lights) != 0
                self.current_light = self.remaining_lights.pop(0)
                self.current_light.add_car_to_queue(self)


# Part 3: Simulation
# ----------------------------------------------

class Simulation:
    """Represents and controls a single traffic light simulation

    Attributes:
        lights: an ordered list of all Lights in this simulation
        cars: an unordered list of active Cars
        timestep_count: how many timesteps have passed in this Simulation
        spawn_time: how many baseline timesteps pass before a new Car is added
    """
    lights: list[Light]
    cars: list[Car]
    timestep_count: int
    spawn_time: int

    def __init__(self, light_count: int, light_change_length: int, light_offset: int, spawn_time: int):
        """Constructor for a new Simulation"""
        self.lights = []
        for index in range(light_count):
            light_countdown = ((index * light_offset) % light_change_length) + 1
            self.lights.append(Light(light_change_length, light_countdown))
        self.spawn_time = spawn_time
        self.cars = []
        self.spawn_countdown = 1
        self.timestep_count = 0

    def __str__(self) -> str:
        """Returns a formatted string representation of this Simulation"""
        result = f'Simulation of {len(self.lights)} light(s)\n'
        result += f'Timestep: {self.timestep_count}\n'
        result += '========================\n\n'
        for index in range(len(self.lights)):
            target_light_count = len(self.lights) - index
            for car in self.cars:
                if not car.is_at_light() and car.number_of_lights() == target_light_count:
                    result += f'{car}\n'

            result += '\n...\n\n'

            light = self.lights[index]
            for car in light.queue:
                result += f'{car}\n'
            result += f'{light}\n---\n'

        return result

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Simulation"""
        return (
            f'Simulation(num_lights={len(self.lights)}, '
            f'num_cars={len(self.cars)}, '
            f'spawn_time={self.spawn_time}, '
            f'spawn_countdown={self.spawn_countdown})'
        )

    def number_of_lights(self) -> int:
        """Returns the number of lights managed by this Simulation"""
        return len(self.lights)

    def active_cars(self) -> int:
        """Returns the number of Cars currently tracked by this simulation"""
        return len(self.cars)

    def waiting_car_count(self) -> int:
        """Returns the total number of Cars currently waiting at traffic lights"""
        num_waiting_cars = 0
        for car in self.cars:
            if car.current_light is not None:
                num_waiting_cars += 1
        return num_waiting_cars

    def car_counts(self) -> list[int]:
        """Calculates the number of Cars waiting at each traffic light"""
        return [light.queue_length() for light in self.lights]

    def timestep(self):
        """Advances this Simulation by exactly 1 timestep"""
        self.timestep_count += 1

        for light in self.lights:
            light.timestep()
            if light.can_go() and light.queue_length() > 0:
                car_removed = light.advance_queue()
                car_removed.start_going()
                if light == self.lights[-1]:
                    self.cars.remove(car_removed)

        for car in self.cars:
            car.timestep()

        self.spawn_countdown -= 1
        if self.spawn_countdown == 0:
            self.cars.append(Car(self.lights[:]))
            self.spawn_countdown = random.randint(
                self.spawn_time, self.spawn_time + SPAWN_VARIATION
            )

    def run(self, timesteps: int):
        """Advances this simulation by a fixed number of timesteps"""
        for _ in range(timesteps):
            self.timestep()


# Simulation Demonstration
# ----------------------------------------------

def main():
    """Runs an interactive traffic simulation and saves the output to simulation_result.txt"""
    random.seed(0)

    light_count = int(input('Give a number of lights: '))
    light_change_length = int(input('Give a number of timesteps before lights change: '))
    light_offset = int(input('Give the timestep "offset" between the starting lights: '))
    spawn_length = int(input('Give the timestep count between each car spawning: '))
    timesteps = int(input('Give the number of timesteps to run the simulation: '))

    simulation = Simulation(light_count, light_change_length, light_offset, spawn_length)
    simulation.run(timesteps)
    print(simulation)

    with open('simulation_result.txt', 'w') as f:
        f.write(str(simulation))


if __name__ == "__main__":
    main()
