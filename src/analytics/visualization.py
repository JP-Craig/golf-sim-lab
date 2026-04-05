import matplotlib.pyplot as plt
import numpy as np

METERS_TO_YARDS = 1.09361


def plot_side_view(
    trajectory: np.ndarray,
    title: str = "Shot Trajectory (Side View)",
    use_yards: bool = True,
) -> None:
    x = trajectory[:, 0] * METERS_TO_YARDS if use_yards else trajectory[:, 0]
    z = trajectory[:, 2] * METERS_TO_YARDS if use_yards else trajectory[:, 2]

    x_label = "Carry Distance (yds)" if use_yards else "Carry Distance (m)"
    z_label = "Height (yds)" if use_yards else "Height (m)"

    plt.figure(figsize=(10, 6))
    plt.plot(x, z, linewidth=2)
    plt.xlabel(x_label)
    plt.ylabel(z_label)
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_top_down_view(
    trajectory: np.ndarray,
    title: str = "Shot Trajectory (Top View)",
    use_yards: bool = True,
) -> None:
    x = trajectory[:, 0] * METERS_TO_YARDS if use_yards else trajectory[:, 0]
    y = trajectory[:, 1] * METERS_TO_YARDS if use_yards else trajectory[:, 1]

    x_label = "Offline Distance (yds)" if use_yards else "Offline Distance (m)"
    y_label = "Carry Distance (yds)" if use_yards else "Carry Distance (m)"

    plt.figure(figsize=(10, 6))
    plt.plot(y, x, linewidth=2)
    plt.axvline(0, linestyle="--")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_multiple_side_views(
    trajectories: list[np.ndarray],
    labels: list[str] | None = None,
    use_yards: bool = True,
) -> None:
    plt.figure(figsize=(10, 6))

    for i, traj in enumerate(trajectories):
        label = labels[i] if labels else f"Shot {i+1}"
        x = traj[:, 0] * METERS_TO_YARDS if use_yards else traj[:, 0]
        z = traj[:, 2] * METERS_TO_YARDS if use_yards else traj[:, 2]
        plt.plot(x, z, alpha=0.8, label=label)

    plt.xlabel("Carry Distance (yds)" if use_yards else "Carry Distance (m)")
    plt.ylabel("Height (yds)" if use_yards else "Height (m)")
    plt.title("Multiple Shot Trajectories (Side View)")
    plt.grid(True)
    if labels:
        plt.legend()
    plt.show()


def plot_multiple_top_down_views(
    trajectories: list[np.ndarray],
    labels: list[str] | None = None,
    use_yards: bool = True,
) -> None:
    plt.figure(figsize=(10, 6))

    for i, traj in enumerate(trajectories):
        label = labels[i] if labels else f"Shot {i+1}"
        x = traj[:, 0] * METERS_TO_YARDS if use_yards else traj[:, 0]
        y = traj[:, 1] * METERS_TO_YARDS if use_yards else traj[:, 1]
        plt.plot(y, x, alpha=0.8, label=label)

    plt.axvline(0, linestyle="--")
    plt.xlabel("Offline Distance (yds)" if use_yards else "Offline Distance (m)")
    plt.ylabel("Carry Distance (yds)" if use_yards else "Carry Distance (m)")
    plt.title("Multiple Shot Trajectories (Top View)")
    plt.grid(True)
    if labels:
        plt.legend()
    plt.show()