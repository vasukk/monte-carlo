# Import libraries
#final without variation
import math

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
from matplotlib.animation import FuncAnimation
import random

# Define the number of polymers and the length of each polymer
num_polymers = 6
polymer_length = 4
total_iterations = 10000

# Generate random positions for the polymers
positions = []
for _ in range(num_polymers):
    # Randomly choose whether the polymer will be horizontal or vertical
    is_horizontal = random.choice([True, False])

    # Randomly choose the starting position within the range of the graph
    if is_horizontal:
        x = random.randint(1, 37)  # To ensure the entire polymer fits within the 40x40 range
        y = random.randint(1, 40)
    else:
        x = random.randint(1, 40)
        y = random.randint(1, 37)

    positions.append((x, y, is_horizontal))

# Initialize empty lists to store coordinates for each polymer
polymer_lists = []

# Iterate through each polymer's position
for i, (x, y, is_horizontal) in enumerate(positions):
    polymer_coords = []  # Initialize empty list to store coordinates of current polymer

    # Generate coordinates based on the orientation of the polymer
    if is_horizontal:
        polymer_coords = [(x + j, y) for j in range(polymer_length)]
    else:
        polymer_coords = [(x, y + j) for j in range(polymer_length)]

    # Append coordinates of current polymer to the list of polymer lists
    polymer_lists.append(polymer_coords)

for i, polymer_coords in enumerate(polymer_lists):
    print(f"Starting Polymer {i + 1} coordinates:", polymer_coords)

# Create a plot with a 40x40 grid
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

# Plot initial polymers
lines = [ax.plot([], [], marker='o', markersize=8)[0] for _ in range(num_polymers)]
count_no = 0
pre_polymer_lists = []
prev_energy_system = 0
energy_counter = 0
prev_energy = 0

# Update function for animation

def update(frame):
    global count_no
    global pre_polymer_lists
    global prev_energy_system
    global energy_counter
    global prev_energy
    global polymer_lists
    total_matches = 0

    # Select a random index (0 or 3) for each polymer and update the bead position accordingly
    #for a in range(total_iterations):
    count_no += 1
    # Initialize energy counter
    pre_polymer_lists = polymer_lists
    prev_energy_system = prev_energy
    # for polymer_coords,line in zip(polymer_lists,lines):
    for polymer_coords in polymer_lists:
        pre_polymer_coords = polymer_coords
        print(f"Iteration is {count_no} : \n Starting Polymer coordinates:", polymer_coords)
        selected_index = random.choice([0, 1, 2, 3])
        selected_bead_coords = polymer_coords[selected_index]
        selected_bead_choices = []
        print("Selected index is ", selected_index)
        if (selected_index in [0, 3]):

            # Check if left and right coordinates are in the polymer list
            left_coords = (selected_bead_coords[0] - 1, selected_bead_coords[1])
            right_coords = (selected_bead_coords[0] + 1, selected_bead_coords[1])

            # Check if top and bottom coordinates are in the polymer list
            top_coords = (selected_bead_coords[0], selected_bead_coords[1] + 1)
            bottom_coords = (selected_bead_coords[0], selected_bead_coords[1] - 1)

            if left_coords in polymer_coords and polymer_coords.index(left_coords) in (
                    selected_index - 1, selected_index + 1):
                # Check if the upper left or lower left coordinate is available
                upper_left = (selected_bead_coords[0] - 1, selected_bead_coords[1] + 1)
                lower_left = (selected_bead_coords[0] - 1, selected_bead_coords[1] - 1)

                # boundary
                if upper_left not in polymer_coords and 0 <= upper_left[0] <= 40 and 0 <= upper_left[1] <= 40:
                    selected_bead_coords = upper_left
                    selected_bead_choices.append(selected_bead_coords)
                if lower_left not in polymer_coords and 0 <= lower_left[0] <= 40 and 0 <= lower_left[1] <= 40:
                    selected_bead_coords = lower_left
                    selected_bead_choices.append(selected_bead_coords)

            if right_coords in polymer_coords and polymer_coords.index(right_coords) in (
                    selected_index - 1, selected_index + 1):
                # Check if the upper right or lower right coordinate is available
                upper_right = (selected_bead_coords[0] + 1, selected_bead_coords[1] + 1)
                lower_right = (selected_bead_coords[0] + 1, selected_bead_coords[1] - 1)

                if upper_right not in polymer_coords and 0 <= upper_right[0] <= 40 and 0 <= upper_right[1] <= 40:
                    selected_bead_coords = upper_right
                    selected_bead_choices.append(selected_bead_coords)
                elif lower_right not in polymer_coords and 0 <= lower_right[0] <= 40 and 0 <= lower_right[1] <= 40:
                    selected_bead_coords = lower_right
                    selected_bead_choices.append(selected_bead_coords)

            if top_coords in polymer_coords and polymer_coords.index(top_coords) in (
                    selected_index - 1, selected_index + 1):
                # Check if the left top or right top coordinate is available
                left_top = (selected_bead_coords[0] - 1, selected_bead_coords[1] + 1)
                right_top = (selected_bead_coords[0] + 1, selected_bead_coords[1] + 1)

                if left_top not in polymer_coords and 0 <= left_top[0] <= 40 and 0 <= left_top[1] <= 40:
                    selected_bead_coords = left_top
                    selected_bead_choices.append(selected_bead_coords)
                if right_top not in polymer_coords and 0 <= right_top[0] <= 40 and 0 <= right_top[1] <= 40:
                    selected_bead_coords = right_top
                    selected_bead_choices.append(selected_bead_coords)

            if bottom_coords in polymer_coords and polymer_coords.index(
                    bottom_coords) in (
                    selected_index - 1, selected_index + 1):
                # Check if the left bottom or right bottom coordinate is available
                left_bottom = (selected_bead_coords[0] - 1, selected_bead_coords[1] - 1)
                right_bottom = (selected_bead_coords[0] + 1, selected_bead_coords[1] - 1)

                if left_bottom not in polymer_coords and 0 <= left_bottom[0] <= 40 and 0 <= left_bottom[1] <= 40:
                    selected_bead_coords = left_bottom
                    selected_bead_choices.append(selected_bead_coords)
                if right_bottom not in polymer_coords and 0 <= right_bottom[0] <= 40 and 0 <= right_bottom[
                    1] <= 40:
                    selected_bead_coords = right_bottom
                    selected_bead_choices.append(selected_bead_coords)

        else:  # corner bead

            # print("Selected bead is corner or middle ", selected_index)
            selected_choice = random.choice([0, 1, 2, 3])
            # Check if top and left coordinates are in the polymer list
            top_coords = (selected_bead_coords[0], selected_bead_coords[1] + 1)
            left_coords = (selected_bead_coords[0] - 1, selected_bead_coords[1])
            bottom_coords = (selected_bead_coords[0], selected_bead_coords[1] - 1)
            right_coords = (selected_bead_coords[0] + 1, selected_bead_coords[1])

            if top_coords in polymer_coords and polymer_coords.index(top_coords) in (
                    selected_index - 1,
                    selected_index + 1) and left_coords in polymer_coords and polymer_coords.index(
                left_coords) in (selected_index - 1, selected_index + 1):
                new_coords = (selected_bead_coords[0] - 1, selected_bead_coords[1] + 1)
                if new_coords not in polymer_coords and 0 <= new_coords[0] <= 40 and 0 <= new_coords[1] <= 40:
                    selected_bead_coords = new_coords
                    selected_bead_choices.append(selected_bead_coords)

            if top_coords in polymer_coords and polymer_coords.index(top_coords) in (
                    selected_index - 1,
                    selected_index + 1) and right_coords in polymer_coords and polymer_coords.index(
                right_coords) in (selected_index - 1, selected_index + 1):
                new_coords = (selected_bead_coords[0] + 1, selected_bead_coords[1] + 1)
                if new_coords not in polymer_coords and 0 <= new_coords[0] <= 40 and 0 <= new_coords[1] <= 40:
                    selected_bead_coords = new_coords
                    selected_bead_choices.append(selected_bead_coords)

            if bottom_coords in polymer_coords and polymer_coords.index(
                    bottom_coords) in (
                    selected_index - 1,
                    selected_index + 1) and right_coords in polymer_coords and polymer_coords.index(
                right_coords) in (selected_index - 1, selected_index + 1):
                new_coords = (selected_bead_coords[0] + 1, selected_bead_coords[1] - 1)
                if new_coords not in polymer_coords and 0 <= new_coords[0] <= 40 and 0 <= new_coords[1] <= 40:
                    selected_bead_coords = new_coords
                    selected_bead_choices.append(selected_bead_coords)

            if bottom_coords in polymer_coords and polymer_coords.index(
                    bottom_coords) in (
                    selected_index - 1,
                    selected_index + 1) and left_coords in polymer_coords and polymer_coords.index(
                left_coords) in (selected_index - 1, selected_index + 1):
                new_coords = (selected_bead_coords[0] - 1, selected_bead_coords[1] - 1)
                if new_coords not in polymer_coords and 0 <= new_coords[0] <= 40 and 0 <= new_coords[1] <= 40:
                    selected_bead_coords = new_coords
                    selected_bead_choices.append(selected_bead_coords)

            # print(f"corner move {selected_bead_coords} ")

        # Update the polymer coordinates with the new bead position
        # polymer_coords[selected_index] = selected_bead_coords
        # if not selected_bead_choices:
        #   polymer_coords[selected_index] = selected_bead_coords
        # else:
        #   polymer_coords[selected_index] = random.choice(selected_bead_choices)

        if selected_bead_choices:
            polymer_coords[selected_index] = random.choice(selected_bead_choices)

        print(f" Polymer coordinates after Iteration {count_no}:", polymer_coords)

        def energy_with_the_move(polymer_lists, prev_energy):
            # Iterate through each polymer's coordinates
            move_accepted = 0
            match_count = 0
            total_matches = 0

            for index in range(polymer_length):
                # Initialize a list to store matched coordinates
                matched_coords = []
                for polymer_coords in polymer_lists:
                    # Get the coordinates at the current index
                    current_coord = polymer_coords[index]

                    # Check against other polymers at the same index
                    for other_coords in polymer_lists:
                        if polymer_coords != other_coords:  # Avoid comparing with itself
                            other_coord = other_coords[index]

                            # Check if the x or y coordinate difference is 1
                            if abs(current_coord[0] - other_coord[0]) == 1 or abs(
                                    current_coord[1] - other_coord[1]) == 1:
                                # Append the matched coordinates to the list
                                matched_coords.append(current_coord)

                    # Count the number of matches without repetition
                    unique_matched_coords = set(matched_coords)
                match_count = len(matched_coords)
                total_matches += match_count
                # print(f"Matches at index {index}: {match_count}")
                # print(f"matched_records{index}: {matched_coords}")

            energy_counter = (total_matches / 2) * -10

            energy = math.pow(2.78, energy_counter - prev_energy)
            print(f"Energy_counter: {energy_counter}")
            print(f"Prev Energy: {prev_energy}")
            print(f"Current Energy: {energy}")

            return energy

        def energy_accepted(current_energy):

            if current_energy < 1:
                move_accepted = 0
                random_number = random.random()
                if (current_energy > random_number):
                    move_accepted = 1
            else:
                move_accepted = 1

            return move_accepted

        current_energy = energy_with_the_move(polymer_lists, prev_energy)

        if (energy_accepted(current_energy)):
            prev_energy = current_energy
        else:
            polymer_chords = pre_polymer_coords

        print(f" Polymer coordinates after Iteration {count_no}:", polymer_coords)

    # check energy

    def check_duplicates(polymer_lists):
        all_coords = set()
        duplicates = []

        for polymer_coords in polymer_lists:
            for coord in polymer_coords:
                if coord in all_coords:
                    duplicates.append(coord)
                else:
                    all_coords.add(coord)
        print(f"duplicates {duplicates}")
        return duplicates

    if not check_duplicates(polymer_lists):
        print(f"duplicate not detected ")
        for polymer_coords, line in zip(polymer_lists, lines):
            x_coords, y_coords = zip(*polymer_coords)
            line.set_data(x_coords, y_coords)

    else:
        print(f"duplicate detected :reverting to previous setup")
        polymer_lists = pre_polymer_lists
        prev_energy = prev_energy_system
        count_no = count_no-1

    # Set the title with energy and iteration information
    ax.set_title(f'Iteration: {count_no} - Energy: {prev_energy}')

    print(f'end iteration {count_no}')


    return lines


# Print the updated polymer coordinates
# for i, polymer_coords in enumerate(polymer_lists):
#   print(f"Final Polymer {i + 1} coordinates:", polymer_coords)


# Create the animation
ani = FuncAnimation(fig, update, frames=range(total_iterations), interval=1, blit=True, repeat=False)

plt.title('Polymers Animation')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
