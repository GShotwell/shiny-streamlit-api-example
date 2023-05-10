from shiny import App, render, ui, reactive
from helpers import read_penguins, scatter_plot, density_plot

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider(
                id="mass",
                label="Max Body Mass",
                min=2000,
                max=8000,
                value=6000,
            ),
            ui.input_checkbox("smoother", "Add Smoother"),
            ui.input_action_button("reset", "Reset Slider"),
        ),
        ui.panel_main(
            ui.output_plot(id="scatter"),
            ui.output_plot(id="mass_hist"),
        ),
    )
)


def server(input, output, session):
    df = read_penguins()

    @reactive.Calc
    def filtered_data():
        filt_df = df.copy()
        filt_df = filt_df.loc[df["body_mass_g"] < input.mass()]
        return filt_df

    @output
    @render.plot
    def mass_hist():
        return density_plot(filtered_data())

    @output
    @render.plot
    def scatter():
        return scatter_plot(filtered_data(), input.smoother())

    @reactive.Effect
    @reactive.event(input.reset)
    def _():
        ui.update_slider(id="mass", value=6000)


app = App(app_ui, server)
