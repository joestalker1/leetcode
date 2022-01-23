def get_itinerary(flights, current_itinerary):
    if len(flights) == 0:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, origin, dest in enumerate(flights):
        flight_without_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(dest)
        if origin == last_stop:
            return get_itinerary(flight_without_current, current_itinerary)
        current_itinerary.pop()
    return None



