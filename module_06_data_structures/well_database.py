wells = [
    {"name": "Thunder Horse #7", "basin": "GoM", "depth_ft": 18500, "pressure_psi": 12450, "is_active": True},
    {"name": "Atlantis #3", "basin": "GoM", "depth_ft": 16200, "pressure_psi": 8200, "is_active": True},
    {"name":"Mad Dog #12", "basin": "GoM", "depth_ft": 19800,"pressure_psi": 11800, "is_active": False},
    {"name":"Spraberry #21", "basin": "Permian", "depth_ft": 9500,"pressure_psi": 4200, "is_active": True},
    {"name":"Wolfcamp #8", "basin": "Permian", "depth_ft": 11200,"pressure_psi": 5800, "is_active": True}
]

def get_active_wells(wells):
    active = []              
    for well in wells:          
        if well["is_active"] == True:    
           active.append(well)
    return active                 

result = get_active_wells(wells)

for well in result:
    print(well["name"])

def get_wells_by_basin(wells, basin_name):
    land = []
    for basin in wells:
        if basin["basin"] == basin_name:
            land.append(basin)
    return land

result_basin = get_wells_by_basin(wells, "GoM")

for basin in result_basin:
    print(f"{basin['name']} - {basin['basin']}")
