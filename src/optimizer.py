from .models import Drone, Order

def manhattan_distance(p1, p2):

    "Calculates the Manhattan distance between two points p1 and p2."

    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def can_deliver_order(drone: Drone, current_route, order: Order, current_payload: float) -> bool:
    """
    Determines if a drone can deliver a new order given its current route and payload.
    
    Checks:
       Payload: Total weight must not exceed drone.max_payload.
       Distance: Total round-trip distance (including new order) must not exceed drone.max_distance.
       Deadline: Estimated travel time must be within order.deadline.
    
    Returns:
      bool: True if the order can be added, False otherwise.
    """
    # Check payload capacity
    if current_payload + order.package_weight > drone.max_payload:
        return False

    last_position = current_route[-1]
    # Calculate distance to new order location
    distance_to_order = manhattan_distance(last_position, (order.delivery_x, order.delivery_y))
    
    # Calculate current route distance
    route_distance = sum(manhattan_distance(current_route[i], current_route[i+1]) for i in range(len(current_route)-1))
    
    # New total distance: current route + leg to order + return to base (0,0)
    new_total_distance = route_distance + distance_to_order + manhattan_distance((order.delivery_x, order.delivery_y), (0, 0))
    
    # Check if distance exceeds drone's maximum distance
    if new_total_distance > drone.max_distance:
        return False

    # Estimate travel time: distance / speed (convert seconds to minutes)
    travel_time_minutes = new_total_distance / drone.speed / 60
    if travel_time_minutes > order.deadline:
        return False

    return True

def assign_orders(grid_size: int, drones, orders):
    """
    Assigns orders to drones.
    
    Procedure:
      1. Sort orders by (earliest first).
      2. For each available drone, try to add orders one by one.
      3. Check constraints: payload, distance, and deadline.
      4. Record the assigned orders and compute the total round-trip distance.
    
    Returns:
     List of assignment dictionaries with drone ID, order Id, and total distance.
    """
    assignments = []
    orders_sorted = sorted(orders, key=lambda o: o.deadline)
    assigned_orders = set()  # Track orders that have been assigned
    
    for drone in drones:
        if not drone.available:
            continue
        
        current_route = [(0, 0)] 
        current_payload = 0
        drone_orders = []
        
        for order in orders_sorted:
            if order.id in assigned_orders:
                continue
            if can_deliver_order(drone, current_route, order, current_payload):
                # Append order's location to the current route
                current_route.append((order.delivery_x, order.delivery_y))
                current_payload += order.package_weight
                drone_orders.append(order.id)
                assigned_orders.add(order.id)
        
        if drone_orders:
            # Calculate total distance traveled
            route_distance = sum(manhattan_distance(current_route[i], current_route[i+1]) for i in range(len(current_route)-1))
            total_distance = route_distance + manhattan_distance(current_route[-1], (0, 0))
            assignments.append({
                "drone": drone.id,
                "orders": drone_orders,
                "total_distance": total_distance
            })
    
    return assignments
