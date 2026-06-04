class Well:
    def __init__(self, name, depth, tvd, pressure, density, temperature):
        self.name = name
        self.depth = depth
        self.pressure = pressure
        self.tvd = tvd
        self.density = density
        self.temperature = temperature

    def hydrostatic_pressure(self):
        return 0.052 * self.tvd * self.density

    def overbalance_margin(self):
        return self.hydrostatic_pressure() - self.pressure
    
    def is_high_temp(self):
        return self.temperature > 250

class InjectionWell(Well):
    def __init__(self, name, depth, tvd, pressure, density, temperature, injection_rate, injection_fluid):
        super().__init__(name, depth, tvd, pressure, density, temperature)
        self.injection_rate = injection_rate
        self.injection_fluid = injection_fluid

    def daily_injection_volume(self):
        return self.injection_rate * 1 #bbl/day simplified

    def overbalance_margin(self):
        # Different math for injection — placeholder for now
        return self.pressure - self.hydrostatic_pressure()

if __name__ == "__main__":
    print("well.py is running!")