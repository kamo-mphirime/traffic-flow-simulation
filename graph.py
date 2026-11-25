"""
Author: Kamo Mphirime
Starting Date: 11/16/2026

Initial creation by Dietrich Geisler on 10/25/2025

Functions to graph various traffic simulation arrangements
"""

import matplotlib.pyplot as plt
import simulation


def graph_waiting_cars():
    """Create and display a graph of the number of waiting cars over time

    The x-axis of this graph is the timestep of the simulation
    The y-axis of this graph is the number of waiting cars at a given light
    Includes lines for each of the lights in the simulation

    Arguments:
      sim_length: The length of simulation to plot
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 300
    LIGHT_COUNT = 3
    LIGHT_CHANGE_LENGTH = 30
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    # Create the simulation
    sim = simulation.Simulation(LIGHT_COUNT,
                                LIGHT_CHANGE_LENGTH,
                                LIGHT_OFFSET,
                                SPAWN_LENGTH)

    # Setup lists for data collection
    timesteps = []
    light_values = []
    for _ in range(LIGHT_COUNT):  # Create one list per light
        light_values.append([])

    # Run the simulation, recording data each step
    for timestep in range(SIMULATION_LENGTH):
        timesteps.append(timestep * 3)  # Note the 3 seconds per timestep
        car_counts = sim.car_counts()
        for index in range(len(car_counts)):
            car_count = car_counts[index]
            light_values[index].append(car_count)
        # Update the simulation _after_ collecting the data
        # Otherwise, the timesteps are off-by-one
        sim.timestep()

    # Always a good idea to print "partially finished" information
    # Otherwise the terminal just freezes for a bit, and it's hard to know if
    #   something went wrong or it's still loading
    print('Simulation finished')

    # Setup the plot with axes
    _, ax = plt.subplots()
    ax.set(xlabel='time (s)', ylabel='number of waiting cars (by light)',
           title=f'Traffic simulation with {LIGHT_COUNT} lights')

    # Plot the light data as associated with each timestep
    for light_data in light_values:
        # Note that each piece of light_data is attached to a given light
        # This means we can use the same timesteps for each
        plt.plot(timesteps, light_data)

    # Add the lights to the legend
    legend_info = []
    for index in range(len(light_values)):
        legend_info.append(f'Light {index + 1}')
    plt.legend(legend_info)

    # Display and save the plot
    plt.savefig('waiting_cars.png')
    plt.show()


def graph_by_light_count():
    """Create and display a graph of varying numbers of lights

    The x-axis of this graph is the number of lights in the simulation
    The y-axis of this graph is the average number of waiting cars in that simulation

    Arguments:
        max_lights: The number of lights in this graph varies from 1 to max_lights
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 500
    LIGHT_COUNT = 5
    LIGHT_CHANGE_LENGTH = 20
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    MAX_LIGHTS = 5

    # Setup lists for data collection
    light_counts = []
    average_waiting_cars = []

    # Loop through each number of lights
    for light_count in range(1, MAX_LIGHTS+1):
        sim = simulation.Simulation(light_count,
                                    LIGHT_CHANGE_LENGTH,
                                    LIGHT_OFFSET,
                                    SPAWN_LENGTH)

        # For each simulation, calculate the average number of waiting cars
        #  over the course of our simulation
        waiting_cars = 0
        for _ in range(SIMULATION_LENGTH):
            waiting_cars += sim.waiting_car_count()
            sim.timestep()
        average_waiting = waiting_cars / SIMULATION_LENGTH

        # Store the data for this count
        light_counts.append(light_count)
        average_waiting_cars.append(average_waiting)

        # Always a good idea to print "partially finished" information
        # Otherwise we might worry a slow simulation crashed
        print(f'Simulation of {light_count} lights finished')

    # Setup the plot with axes
    _, ax = plt.subplots()
    ax.set(xlabel='number of lights', ylabel='average waiting cars',
           title=f'Traffic simulation for varying numbers of lights')

    # Plot our data
    plt.plot(light_counts, average_waiting_cars)

    # Display and save the plot
    plt.savefig('light_count.png')
    plt.show()
#--------------------------------------------------------------------------------------------------------------------------
def graph_by_light_length():
    """Create and display a graph of varying numbers of lights

    The x-axis of this graph is the number of lights in the simulation
    The y-axis of this graph is the average number of waiting cars in that simulation

    Arguments:
        max_lights: The number of light_lengh in this graph varies from 1 to max_light_length
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 500
    LIGHT_COUNT = 5
    LIGHT_CHANGE_LENGTH = 20
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    MAX_LIGHTS = 5
    MAX_CHANGE_LENGTH = 40


    # Setup lists for data collection
    list_light_change_lengths = []
    average_waiting_cars = []

    # Loop through each number of lights
    for light_ in range(1, MAX_CHANGE_LENGTH+1):
        sim = simulation.Simulation(LIGHT_COUNT,
                                    light_,
                                    LIGHT_OFFSET,
                                    SPAWN_LENGTH)

        # For each simulation, calculate the average number of waiting cars
        #  over the course of our simulation
        waiting_cars = 0
        for _ in range(SIMULATION_LENGTH):
            waiting_cars += sim.waiting_car_count()
            sim.timestep()
        average_waiting = waiting_cars / SIMULATION_LENGTH

        # Store the data for this count
        list_light_change_lengths.append(light_)
        average_waiting_cars.append(average_waiting)

        # Always a good idea to print "partially finished" information
        # Otherwise we might worry a slow simulation crashed
        print(f'Simulation of light change length {light_}  finished')

    # Setup the plot with axes
    _, ax = plt.subplots()
    ax.set(xlabel='light change length', ylabel='average waiting cars',
           title=f'Traffic simulation for varying light change lengths')

    # Plot our data
    plt.plot(list_light_change_lengths, average_waiting_cars)

    # Display and save the plot
    plt.savefig('light_length.png')
    plt.show()
#-------------------------------------------------------------------------------------------------------------------------------
def graph_by_light_offset():
    """Create and display a graph of varying numbers of lights

    The x-axis of this graph is the number of lights in the simulation
    The y-axis of this graph is the average number of waiting cars in that simulation

    Arguments:
        max_lights: The number of light_lengh in this graph varies from 1 to max_light_length
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 500
    LIGHT_COUNT = 5
    LIGHT_CHANGE_LENGTH = 20
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    MAX_LIGHTS = 5
    MAX_CHANGE_LENGTH = 40
    MAX_LIGHT_OFFSET=6

    # Setup lists for data collection
    list_light_change_lengths = []
    average_waiting_cars = []
    list_light_offset=[]

    # Loop through each number of lights
    for light_ in range(1, MAX_LIGHT_OFFSET+1):
        sim = simulation.Simulation(LIGHT_COUNT,
                                    LIGHT_CHANGE_LENGTH,
                                    light_,
                                    SPAWN_LENGTH)

        # For each simulation, calculate the average number of waiting cars
        #  over the course of our simulation
        waiting_cars = 0
        for _ in range(SIMULATION_LENGTH):
            waiting_cars += sim.waiting_car_count()
            sim.timestep()
        average_waiting = waiting_cars / SIMULATION_LENGTH

        # Store the data for this count
        list_light_offset.append(light_)
        average_waiting_cars.append(average_waiting)

        # Always a good idea to print "partially finished" information
        # Otherwise we might worry a slow simulation crashed
        print(f'Simulation of light offset {light_} finished')

    # Setup the plot with axes
    _, ax = plt.subplots()
    ax.set(xlabel='light offset', ylabel='average waiting cars',
           title=f'Traffic simulation for varying light offset values')

    # Plot our data
    plt.plot(list_light_offset, average_waiting_cars)

    # Display and save the plot
    plt.savefig('light_offset.png')
    plt.show()

#-------------------------------------------------------------------------------------------------------------------------------
def graph_by_density():
    """Create and display a graph of varying numbers of lights

    The x-axis of this graph is the number of lights in the simulation
    The y-axis of this graph is the average number of waiting cars in that simulation

    Arguments:
        max_lights: The number of light_lengh in this graph varies from 1 to max_light_length
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 500
    LIGHT_COUNT = 5
    LIGHT_CHANGE_LENGTH = 20
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    MAX_LIGHTS = 5
    MAX_CHANGE_LENGTH = 40


    # Setup lists for data collection
    list_light_change_lengths = []
    average_waiting_cars = []
    list_spawn_lengths=[]

    # Loop through each number of lights
    for light_ in range(1, SPAWN_LENGTH+1):
        sim = simulation.Simulation(LIGHT_COUNT,
                                    LIGHT_CHANGE_LENGTH,
                                    LIGHT_OFFSET ,
                                    light_)

        # For each simulation, calculate the average number of waiting cars
        #  over the course of our simulation
        waiting_cars = 0
        for _ in range(SIMULATION_LENGTH):
            waiting_cars += sim.waiting_car_count()
            sim.timestep()
        average_waiting = waiting_cars / SIMULATION_LENGTH

        # Store the data for this count
        list_spawn_lengths.append(light_)
        average_waiting_cars.append(average_waiting)

        # Always a good idea to print "partially finished" information
        # Otherwise we might worry a slow simulation crashed
        print(f'Simulation of light offset {light_} finished')

    # Setup the plot with axes
    _, ax = plt.subplots()
    ax.set(xlabel='light offset', ylabel='average waiting cars',
           title=f'Traffic simulation for varying light offset values')

    # Plot our data
    plt.plot(list_spawn_lengths, average_waiting_cars)

    # Display and save the plot
    plt.savefig('density.png')
    plt.show()



def main():
    """The function we use to decide which experiment to run"""
    graph_by_light_count()
    graph_waiting_cars()
    graph_by_light_length()
    graph_by_light_offset()
    graph_by_density()


if __name__ == "__main__":

    main()



ordered_trails=[]
trails2=trails[:]
min=0
min_name=''
#ordertin the trails by lenth first
for t in trails:
    min=t.length
    min_name=t
    for t2 in trails2:
        if min<t2.length:
            min=t2.length
            min_name=t2
    ordered_trails.append(trails2.pop(index(min_name)))
result={}
for trail in ordered_trails:
    if trail.difficulty not in result:
        result[train.difficulty].append(trail)
    else:
        result[trail.difficulty].append(trail)
