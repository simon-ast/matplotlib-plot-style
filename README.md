# Matplotlib plotting styles
A repository for my preferred matplotlib stylesheet (custom), to homogenise 
Python plotting routines. As an example: The standard matplotlib plotting 
style setup produces a plot looking like this

![standard](plots/plotting_example_default.png)

For my preferred plot settings, I include (among other things) minor and 
major tick labels, larger axis and tick label sizes, a `tight_layout()` 
plot setting, thicker axis and tick lines, and a legend with no border.

![my_default](plots/plotting_example_my_default.png)

To use one of the style-sheets stored here, the easiest solution is to 
include the following code-snippet before creating plots in a script

```
plt.style.use("https://raw.githubusercontent.com/simon-ast/matplotlib-plot-style/main/default_style.mplstyle")
```

The link within `plt.style.use` is for the raw `*.mplstyle` file from 
within this repository.