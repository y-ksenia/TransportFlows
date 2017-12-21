import abc


class BaseTransport:
    @abc.abstractmethod
    def cost(self, time_price, type_users, road_users):
        raise NotImplemented()

    @abc.abstractmethod
    def get_road_type(self):
        pass


ROAD_TYPES = {
    'train':1,
    'road': 2,
    'bus_road': 3
}


class TrainTransport(BaseTransport):

    def __init__(self, ticket_cost, free_way_time, user_road_time_sensity, irritability):
        self.ticket_cost = ticket_cost
        self.free_way_time = free_way_time
        self.user_road_time_sensity = user_road_time_sensity
        self.irritability = irritability

    def _travel_time(self, type_users, road_users):
        return self.free_way_time + self.user_road_time_sensity * road_users ** 4

    def _irritability(self, type_users, road_users):
        return self.irritability * road_users ** 2

    def cost(self, time_price, type_users, road_users):
        return (self.ticket_cost +
                time_price * self._travel_time(type_users, road_users) +
                self._irritability(type_users, road_users))

    def get_road_type(self):
        return ROAD_TYPES['train']


class TaxiTransport(BaseTransport):

    def __init__(self, base_price, free_way_time, price_coeff, spec_road_percentage, load_road_coeff):
        self.base_price = base_price
        self.price_coeff = price_coeff
        self.spec_road_percentage = spec_road_percentage
        self.free_way_time = free_way_time
        self.load_road_coeff = load_road_coeff

    def _travel_price(self, type_users, road_users):
        return self.base_price + self.price_coeff * type_users ** 0.5

    def _travel_time(self, type_users, road_users):
        return self.free_way_time + (1 - self.spec_road_percentage) * self.load_road_coeff * road_users ** 4

    def cost(self, time_price, type_users, road_users):
        return self._travel_price(type_users, road_users) + time_price * self._travel_time(type_users, road_users)

    def get_road_type(self):
        return ROAD_TYPES['road']


class CarTransport(BaseTransport):

    def __init__(self, having_price, free_way_time, load_road_coeff, oil_per_time_coeff):
        self.having_price = having_price
        self.free_way_time = free_way_time
        self.load_road_coeff = load_road_coeff
        self.oil_per_time_coeff = oil_per_time_coeff

    def _travel_time(self, type_users, road_users):
        return self.free_way_time + self.load_road_coeff * road_users ** 4

    def _oil_cost(self, type_users, road_users):
        return self.oil_per_time_coeff * self._travel_time(type_users, road_users)

    def cost(self, time_price, type_users, road_users):
        return self.having_price + self._oil_cost(type_users, road_users) + time_price * self._travel_time(type_users, road_users)

    def get_road_type(self):
        return ROAD_TYPES['road']


