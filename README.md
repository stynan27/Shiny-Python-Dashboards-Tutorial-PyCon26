# PyCon 2026: Shiny Dashboards

Workshop materials for [**PyCon US 2026**](https://us.pycon.org/2026/) - Long Beach, California.

📖 **Setup & workshop website**: <https://chendaniely.github.io/pycon-2026-shiny>


## Verify Installation

```bash
python test-install.py
shiny run test-install.py
```

## Run in the Cloud

| Platform | Launch |
|---|---|
| GitHub Codespaces | [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/chendaniely/pycon-2026-shiny) |
| MyBinder | [![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chendaniely/pycon-2026-shiny/HEAD) |
| Posit Cloud | [Instructions](https://chendaniely.github.io/pycon-2026-shiny/cloud.html#posit-cloud) |

Full instructions: <https://chendaniely.github.io/pycon-2026-shiny/cloud.html>

## Slide Theming Notes

`website/slides/slides-theme.scss` — all slide visual tweaks live here:

- **Title slide font sizes**: `$title-font-size` and `$subtitle-font-size` variables near the bottom of the file
- **`.smaller` slide font size**: `$smaller-font-size` variable at the top of the file (Quarto default is `0.7em`)
