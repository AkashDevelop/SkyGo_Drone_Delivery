import pytest
from src.optimizer import manhattan_distance, can_deliver_order, assign_orders
from src.models import Drone, Order, City

def test_manhattan_distance():
    assert manhattan_distance((0, 0), (5, 5)) == 10
    assert manhattan_distance((2, 3), (2, 3)) == 0
    assert manhattan_distance((1, 2), (3, 5)) == 5

def test_can_deliver_order_success():
    drone = Drone(id="D1", max_payload=5, max_distance=20, speed=2, available=True)
    current_route = [(0, 0)]
    current_payload = 0
    order = Order(id="O1", delivery_x=5, delivery_y=5, deadline=15, package_weight=2)
    result = can_deliver_order(drone, current_route, order, current_payload)
    assert result is True

def test_can_deliver_order_fail_due_to_payload():
    drone = Drone(id="D1", max_payload=5, max_distance=20, speed=2, available=True)
    current_route = [(0, 0)]
    current_payload = 4
    order = Order(id="O1", delivery_x=2, delivery_y=2, deadline=15, package_weight=2)
    result = can_deliver_order(drone, current_route, order, current_payload)
    assert result is False

def test_assign_orders():
    drones = [
        Drone(id="D1", max_payload=5, max_distance=30, speed=2, available=True),
        Drone(id="D2", max_payload=10, max_distance=50, speed=1.5, available=True)
    ]
    orders = [
        Order(id="O1", delivery_x=5, delivery_y=5, deadline=20, package_weight=2),
        Order(id="O2", delivery_x=10, delivery_y=0, deadline=30, package_weight=3)
    ]
    
    assignments = assign_orders(20, drones, orders)
    assert isinstance(assignments, list)
    for assignment in assignments:
        assert "drone" in assignment
        assert "orders" in assignment
        assert "total_distance" in assignment
