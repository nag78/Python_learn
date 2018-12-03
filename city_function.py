def get_formatted_state_city(state,city,population = ''):
    """Возвращает отформатированое City, State."""
    if population:

        formatted = city.title() + ", " + state.title() + " - population "+ str(population) +"."
    else:
        formatted = city.title() + ", " + state.title() + "."
    return formatted


print(get_formatted_state_city('chile','city',5000000))