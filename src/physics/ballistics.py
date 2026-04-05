import numpy as np

def simulate_flight(vx, vy, vz, spin_axis=0.0, dt=0.01):
    g = 9.81
    drag_coeff = 0.0015
    lift_coeff = 0.0008
    side_coeff = 0.0005

    x, y, z = 0.0, 0.0, 0.0
    positions = []

    while z >= 0:
        v = np.sqrt(vx**2 + vy**2 + vz**2)

        if v == 0:
            break

        drag = drag_coeff * v**2
        lift = lift_coeff * v**2
        side_force = side_coeff * v**2 * spin_axis

        ax = -drag * vx / v
        ay = -drag * vy / v + side_force
        az = -g - (drag * vz / v) + lift
        
        vx += ax * dt
        vy += ay * dt
        vz += az * dt

        x += vx * dt
        y += vy * dt
        z += vz * dt

        positions.append((x, y, z))

    return np.array(positions)


def simulate_shots(row, n=100):
    shots = []

    for _ in range(n):
        speed = np.random.normal(row["ball_speed_mps"], 1.5)
        launch = np.random.normal(row["launch_angle_rad"], 0.02)
        azimuth = np.random.normal(row["azimuth_rad"], 0.02)

        vx = speed * np.cos(launch) * np.cos(azimuth)
        vy = speed * np.cos(launch) * np.sin(azimuth)
        vz = speed * np.sin(launch)

        spin_axis = np.radians(row["spin_axis_deg"])

        traj = simulate_flight(vx, vy, vz, spin_axis=spin_axis)

        if len(traj) == 0:
            continue

        final_x, final_y, _ = traj[-1]
        shots.append((final_x, final_y))
        
    return np.array(shots)