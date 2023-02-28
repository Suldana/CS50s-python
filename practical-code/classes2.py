class flight();
    def __init__(self, capacity)
        self.capacity = capacity
        self.passenger = []

    def add _passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return true

    def open_seats(self):
        return self.capacity - len(self.capacity)

Flights = flight(3)

people =["Juweria", "Mohamed", "Fadumo", "Hersi"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to the flight successfully")
    else:
        print(f"no available seats for {person}")