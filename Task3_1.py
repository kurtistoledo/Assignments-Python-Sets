# Lesson 3: Python Sets
# 1. Python Sets Adventure

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
unique_to_our_airline = our_routes - competitor_routes
neither_shared_destinations = our_routes.symmetric_difference(competitor_routes)

print(f"Common destinations: {common_destinations}")
print(f"Destinations unique to our airline: {unique_to_our_airline}")
print(f"Destinations neither airline shares: {neither_shared_destinations}")
