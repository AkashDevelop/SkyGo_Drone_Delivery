from .input_parser import load_input
from .optimizer import assign_orders
from .output_writer import write_output

def main():
    # Load input data from input.json
    city, drones, orders = load_input("input.json")
    
    # Run the assignment algorithm
    assignments = assign_orders(city.grid_size, drones, orders)
    
    write_output(assignments)
    
    print("Assignments generated successfully. Please check output.json for details.")

if __name__ == "__main__":
    main()
