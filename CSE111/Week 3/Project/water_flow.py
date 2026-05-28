# Enhancements beyond base requirements:
# 1. Added named constants: EARTH_ACCELERATION_OF_GRAVITY, WATER_DYNAMIC_VISCOSITY
# 2. Added kpa_to_psi() function to convert kilopascals to pounds per square inch
# 3. main() now prints final pressure in both kPa and psi

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

WATER_DENSITY = 998.2           # density of water (kilogram / meter^3)
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # (meter / second^2)
WATER_DYNAMIC_VISCOSITY = 0.0010016     # (Pascal seconds)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")


def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4


def pressure_gain_from_water_height(height):
    # P = (rho * g * h) / 1000
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # P = -(f * L * rho * v^2) / (2000 * d)
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # P = (-0.04 * rho * v^2 * n) / 2000
    return -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    # R = (rho * d * v) / mu
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * fluid_velocity ** 2 / 2000


def kpa_to_psi(pressure_kpa):
    """Convert pressure from kilopascals to pounds per square inch."""
    return pressure_kpa * 0.145038


if __name__ == "__main__":
    main()
