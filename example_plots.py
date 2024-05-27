import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # First, use the generic matplotlib rc-parameters
    mpl.rcParams.update(mpl.rcParamsDefault)
    make_generic_plot("default")

    # Make a comparison with my preferred parameters
    plt.style.use("default_style.mplstyle")
    make_generic_plot("my_default")


def make_generic_plot(save_id: str) -> None:
    """
    Generate a generic plot and save it.

    Input
        save_id:    String defining a save-name extension

    Return
        None, figure is saved locally
    """
    x_array = np.linspace(0, 4 * np.pi, 1000)

    fig, ax = plt.subplots()
    ax.plot(x_array, np.sin(x_array), label="sin(x)")
    ax.plot(x_array, np.cos(x_array), label="cos(x)")

    ax.set(xlabel="Numpy linspace", ylabel="f(x) = sin(x)")
    ax.legend()

    plt.savefig(f"plots/plotting_example_{save_id}.png", dpi=600)


if __name__ == "__main__":
    main()
