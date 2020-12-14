import math

def main() -> None:
    with open('input') as f:
        timestamp, buses = f.readlines()
        timestamp = int(timestamp.strip('\n'))
        buses = buses.strip('\n').split(',')
        closest_bus = None
        diff = 0
        for bus in buses:
            if bus == 'x':
                continue
            bus_id = int(bus)
            closest_to_timestamp = (math.ceil(timestamp / bus_id) * bus_id) - timestamp
            if closest_bus is None or (closest_to_timestamp < diff):
                closest_bus = bus
                diff = closest_to_timestamp
        print(f'The closest bus is ---> {int(closest_bus) * diff}')


if __name__ == '__main__':
    main()
