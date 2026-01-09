from Customer import Customer

class CustomerRepository:
    def __init__(self):
        self.customers = {}

    def create(self, customer: Customer):
        self.customers[customer.id] = customer
        return customer

    def get_by_id(self, id: int):
        return self.customers.get(id)

    def list_all(self):
        return list(self.customers.values())

    def update(self, customer: Customer):
        if customer.id in self.customers:
            self.customers[customer.id] = customer
            return True
        return False

    def delete(self, id: int):
        if id in self.customers:
            del self.customers[id]
            return True
        return False
