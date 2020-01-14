"""Functions which format the output."""

def print_links(lst):
    """Prints a simple, human-readable list in the CLI."""

    if len(lst) == 0:
        print("No links found.")
        return None

    print("Links found:\n------------")
    for i, link in enumerate(lst):
        print(f"{i+1}. {link}")
    return None
    
## tbd: graphical output, plots, etc.
