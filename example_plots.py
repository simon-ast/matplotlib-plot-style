import corner
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # First, use the generic matplotlib rc-parameters
    mpl.rcParams.update(mpl.rcParamsDefault)
    make_generic_plot("default")
    make_generic_corner("default")

    # Make a comparison with my preferred parameters
    plt.style.use("default_style.mplstyle")
    make_generic_plot("my_default")
    
    # Do the same for a corner plot
    plt.style.use("corner_style.mplstyle")
    make_generic_corner("my_default")
    
    return None
    


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

    fig.savefig(f"plots/plotting_example_{save_id}.png", dpi=600)


def make_generic_corner(save_id: str) -> None:
    """DOC!"""
    # Set up the parameters of the problem.
    ndim, nsamples = 3, 50000

    # Generate some fake data.
    np.random.seed(42)
    data1 = np.random.randn(ndim * 4 * nsamples // 5).reshape(
        [4 * nsamples // 5, ndim]
    )
    data2 = 4 * np.random.rand(ndim)[None, :] + np.random.randn(
        ndim * nsamples // 5
    ).reshape([nsamples // 5, ndim])
    data = np.vstack([data1, data2])

    # Plot it.
    figure = corner.corner(
        data,
        labels=[
            r"$x$",
            r"$y$",
            r"$\log \alpha$",
            r"$\Gamma \, [\mathrm{parsec}]$",
        ],
        quantiles=[0.16, 0.5, 0.84],
        show_titles=True
    )
    
    figure.tight_layout()
    figure.savefig(f"plots/plotting_example_corner_{save_id}.png", dpi=600)
    
    return None




if __name__ == "__main__":
    main()
