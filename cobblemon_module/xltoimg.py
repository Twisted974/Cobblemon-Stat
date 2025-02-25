import excel2img

# Save as PNG the range of used cells in test.xlsx on page named "Sheet1"
excel2img.export_img("output.xlsx", "../images/outputGlobal.png", "Global", "A1:N15")
excel2img.export_img("output.xlsx", "../images/outputShiny.png", "Shiny", "A1:N15")
excel2img.export_img("output.xlsx", "../images/outputLegendary.png", "Legendary", "A1:N15")