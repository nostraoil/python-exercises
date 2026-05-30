class Zone:
    def __init__(self, name, pressure_psi, perforations):
        self.name = name
        self.pressure_psi = pressure_psi
        self.perforations = perforations
    
    def is_high_pressure(self):
        return self.pressure_psi > 9000


class Well:
    def __init__(self, name):
        self.name = name
        self.zones = []
    
    def add_zone(self, zone):
        self.zones.append(zone)
    
    def total_perforations(self):
        total = 0
        for zone in self.zones:
            total += zone.perforations
        return total
    
    def high_pressure_zones(self):
        return [z for z in self.zones if z.is_high_pressure()]


well = Well("AC-857-X1")
well.add_zone(Zone("M1", 9200, 24))
well.add_zone(Zone("M2", 8800, 32))
well.add_zone(Zone("M3", 9500, 18))

print(f"Total perforations: {well.total_perforations()}")

high_pressure = well.high_pressure_zones()
print(f"High pressure zones: {[z.name for z in high_pressure]}")
print(f"Number of high pressure zones: {len(high_pressure)}")