def calculate_active_time(data):
    # Assumes data is well-formed.
    count = 0

    total_active_time = 0

    start_current_active_time = None

    for delivery_id, timestamp, delivery_type in data:
        if delivery_type == 'pickup' and count == 0:
            start_current_active_time = timestamp
            count += 1
        elif delivery_type == 'dropoff' and count == 1:
            total_active_time = timestamp - start_current_active_time
            count -= 1

    return total_active_time


print(calculate_active_time(
    [(1, 1573280047, 'pickup'), (1, 1570320725, 'dropoff'), (2, 1570321092, 'pickup'), (3, 1570321212, 'pickup'),
     (3, 1570322352, 'dropoff'), (2, 1570323012, 'dropoff')]))
