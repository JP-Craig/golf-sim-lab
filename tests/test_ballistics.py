from src.physics.ballistics import simulate_flight

def test_simulation_runs():
    traj = simulate_flight(50, 0, 50)
    assert len(traj) > 0