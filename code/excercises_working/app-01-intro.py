from palmerpenguins import load_penguins
from plotnine import aes, geom_point, ggplot, theme_minimal
from shiny import reactive
from shiny.express import input, render, ui

dat = load_penguins().dropna()
num_cols = dat.select_dtypes("float64").columns.tolist()
species = dat["species"].unique()
species_list = list(species)

ui.input_select("x", "", num_cols, selected="bill_depth_mm")
ui.input_select("y", "", num_cols, selected="body_mass_g")
ui.input_checkbox_group(  
    "selected_species",  
    "Species Filter",  
    choices=species_list,
    selected=species_list,  # all selected by default  
) 

@reactive.calc
def filtered_dat():
    selected = input.selected_species()
    return dat[dat["species"].isin(selected)]

@render.plot
def plot():
    return (ggplot(filtered_dat(), aes(x=input.x(), y=input.y(), color="species")) +
        geom_point(alpha=0.7) +
        theme_minimal()
    )
