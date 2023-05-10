from pandas import read_csv, DataFrame
from plotnine import ggplot, geom_density, aes, theme_light, geom_point, stat_smooth
import time


def read_penguins():
    return read_csv(
        "https://gist.githubusercontent.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv"
    )


def scatter_plot(df, smoother=False):
    plot = (
        ggplot(
            df,
            aes(
                x="bill_length_mm",
                y="bill_depth_mm",
                color="species",
                group="species",
            ),
        )
        + geom_point()
        + theme_light()
    )
    if smoother:
        plot = plot + stat_smooth()

    return plot


def density_plot(df):
    plot = (
        ggplot(df, aes(x="body_mass_g", fill="species"))
        + geom_density(alpha=0.2)
        + theme_light()
    )
    return plot
