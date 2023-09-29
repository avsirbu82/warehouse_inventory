def calculate_storage_allocation(storage_capacity, sales_ratios, product_volumes, pick_frequencies, replenishment_times, selling_speeds):
    allocations = {}

    # Calculate storage for each category
    for category, ratio in sales_ratios.items():
        daily_requirement = product_volumes[category] * selling_speeds[category]
        base_allocation = storage_capacity * ratio
        buffer_stock = pick_frequencies[category] * replenishment_times[category] * daily_requirement
        allocations[category] = base_allocation + buffer_stock

    # Calculate total storage need for all categories
    total_allocation = sum(allocations.values())

    # Distribute allocations across 4 floors while utilizing the entire space
    floor_allocations = {f"Floor {i+1}": {} for i in range(4)}
    for category in sales_ratios:
        for i in range(4):
            floor_allocations[f"Floor {i+1}"][category] = (allocations[category] / total_allocation) * storage_capacity

    return floor_allocations
# Input data
storage_capacity = 1000  # per floor
sales_ratios = {
    'clothes': 0.45,
    'shoes': 0.25,
    'accessories': 0.15
}
product_volumes = {
    'clothes': 0.1,
    'shoes': 0.3,
    'accessories': 0.2
}
pick_frequencies = {
    'clothes': 10,
    'shoes': 5,
    'accessories': 7
}
replenishment_times = {
    'clothes': 2,
    'shoes': 3,
    'accessories': 2.5
}
selling_speeds = {
    'clothes': 359,
    'shoes': 40,
    'accessories': 60
}

# Run the algorithm
allocations = calculate_storage_allocation(storage_capacity, sales_ratios, product_volumes, pick_frequencies, replenishment_times, selling_speeds)
print(allocations)
