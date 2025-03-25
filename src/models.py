from dataclasses import dataclass

@dataclass
class City:
    grid_size: int  

@dataclass
class Drone:
    id: str             # Unique identifier (e.g., "D1")
    max_payload: float  # Maximum payload in kilograms
    max_distance: float # Maximum round-trip distance in city blocks
    speed: float        # Speed in city blocks per second
    available: bool     # Availability status (True if available)

@dataclass
class Order:
    id: str             # Unique order identifier (e.g., "O1")
    delivery_x: int     # X-coordinate of the delivery location on the grid
    delivery_y: int     # Y-coordinate of the delivery location on the grid
    deadline: float     # Deadline in minutes for delivery
    package_weight: float   # Weight of the package in kilograms
