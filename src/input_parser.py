import json
from .models import City, Drone, Order

def load_input(file_path: str):
    """
    Reads the input JSON file and converts it into Python objects.
        
    Returns:
        tuple: A tuple containing a City object, a list of Drone objects, and a list of Order objects.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Parse city information
    city_data = data.get("city", {})
    grid_size = city_data.get("grid_size", 20)
    city = City(grid_size=grid_size)
    
    # Parse drones: Expecting an array under "drones" -> "fleet"
    drones = []
    for d in data.get("drones", {}).get("fleet", []):
        drones.append(Drone(
            id=d["id"],
            max_payload=d["max_payload"],
            max_distance=d["max_distance"],
            speed=d["speed"],
            available=d["available"]
        ))
    
    # Parse orders: Expecting an array under "orders"
    orders = []
    for o in data.get("orders", []):
        orders.append(Order(
            id=o["id"],
            delivery_x=o["delivery_x"],
            delivery_y=o["delivery_y"],
            deadline=o["deadline"],
            package_weight=o["package_weight"]
        ))
    
    return city, drones, orders
