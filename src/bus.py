class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination 
        self.price = price
        self.capacity = capacity
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - self.passenger_count()

    def pick_up(self, person):
        self.passengers.append(person)
    
    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []

    def pay(self, person):
        self.pick_up(person)
        person.reduce_cash(self.price)
    
    def pick_up_from_stop(self, bus_stop):
        
        # if self.remaining_capacity() >= bus_stop.queue_length():
        for person in bus_stop.queue:
            if person.destination == self.destination and person.cash >= self.price and self.remaining_capacity() >= bus_stop.queue_length():
                self.passengers.append(person)
                self.pay(person)
                bus_stop.queue.remove(person)
        # self.passengers += bus_stop.queue
        # bus_stop.clear()


        
    
