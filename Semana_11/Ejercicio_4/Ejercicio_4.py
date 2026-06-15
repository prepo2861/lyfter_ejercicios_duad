"""
Cree las siguientes clases:
Head
Torso
Arm
Hand
Leg
Feet
Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

"""

# Class that represents a human head
class Head:

    # Initialize hair color and eye color
    def __init__(self, hair_color, eye_color):
        self.hair_color = hair_color
        self.eye_color = eye_color


# Class that represents the torso
class Torso:

    # Initialize chest size
    def __init__(self, chest_size):
        self.chest_size = chest_size


# Class that represents a hand
class Hand:

    # Initialize hand size
    def __init__(self, size):
        self.size = size


# Class that represents an arm
class Arm:

    # Initialize arm length and connect the arm with a hand
    def __init__(self, length, hand):
        self.length = length
        self.hand = hand


# Class that represents a foot
class Foot:

    # Initialize foot size
    def __init__(self, size):
        self.size = size


# Class that represents a leg
class Leg:

    # Initialize leg length and connect the leg with a foot
    def __init__(self, length, foot):
        self.length = length
        self.foot = foot


# Class that represents a human being
class Human:

    # Initialize the main body parts that make up a human
    def __init__(self, head, torso, arms, legs):

        # Store the head object
        self.head = head

        # Store the torso object
        self.torso = torso

        # Store both arms; each arm already has its own hand
        self.arms = arms

        # Store both legs; each leg already has its own foot
        self.legs = legs


# Create hands
right_hand = Hand(20)
left_hand = Hand(20)

# Create arms and connect each arm with its corresponding hand
right_arm = Arm(20, right_hand)
left_arm = Arm(20, left_hand)

# Create feet
right_foot = Foot(40)
left_foot = Foot(40)

# Create legs and connect each leg with its corresponding foot
right_leg = Leg(90, right_foot)
left_leg = Leg(90, left_foot)

# Create the head
head = Head("brown", "blue")

# Create the torso
torso = Torso(20)

# Create a Human object and connect all main body parts
human = Human(
    head,
    torso,
    [right_arm, left_arm],
    [right_leg, left_leg]
)

# Display basic information about the human
print(
    f"Human has {human.head.hair_color} hair "
    f"and {human.head.eye_color} eyes."
)

# Display information about connected body parts
print(f"Right arm length: {human.arms[0].length}")
print(f"Right hand size: {human.arms[0].hand.size}")

print(f"Left leg length: {human.legs[1].length}")
print(f"Left foot size: {human.legs[1].foot.size}")