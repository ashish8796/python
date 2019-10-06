mountain = [
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]

def peak_height(mountain):
    for ind, val in enumerate(mountain):
        if ind==0 or ind== len(mountain)-1:
            mountain[ind] = val.replace("^", "1")
        else:
            mountain[ind] = val.replace('^', "1", 1)
    
    return mountain

print(peak_height(mountain))