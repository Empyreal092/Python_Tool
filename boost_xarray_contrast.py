
# Put this at the top of your notebook
import xarray as xr
from IPython.display import HTML, display

def boost_xarray_contrast(
    bg="#bfc8d1",       # background
    fg="#000000",       # foreground (main text)
    border="#3a3f4b",   # borders/dividers
    accent="#f77a7a",   # variable names / headers
    muted="#a8b3cf"     # secondary text
):
    css = f"""
    <style id="xr-contrast-override">
      :root {{
        --xr-bg: {bg};
        --xr-fg: {fg};
        --xr-border: {border};
        --xr-accent: {accent};
        --xr-muted: {muted};
      }}
      /* Container and general text */
      .xr-wrap {{
        background: var(--xr-bg) !important;
        color: var(--xr-fg) !important;
        border-color: var(--xr-border) !important;
      }}
      .xr-wrap * {{
        color: var(--xr-fg) !important;
      }}

      /* Sections and lists */
      .xr-section,
      .xr-array,
      .xr-var-list,
      .xr-attrs,
      .xr-coords {{
        background: transparent !important;
        border-color: var(--xr-border) !important;
      }}

      /* Dividers and borders */
      .xr-var-item,
      .xr-attr,
      .xr-coord,
      .xr-section + .xr-section {{
        border-color: var(--xr-border) !important;
      }}

      /* Emphasis: variable names, dims, coords */
      .xr-array-name,
      .xr-var-name,
      .xr-index-name,
      .xr-section-item > .xr-section-item-label {{
        color: var(--xr-accent) !important;
        font-weight: 600;
      }}

      /* Muted/secondary info (like comments) */
      .xr-comment,
      .xr-has-index .xr-index-name,
      .xr-dim-list {{
        color: var(--xr-muted) !important;
      }}

      /* Values */
      .xr-value {{
        color: var(--xr-fg) !important;
      }}

      /* Links inside repr */
      .xr-wrap a {{
        color: var(--xr-accent) !important;
        text-decoration: none;
      }}
      .xr-wrap a:hover {{
        text-decoration: underline;
      }}
    </style>
    """
    display(HTML(css))

# Use HTML repr (so the CSS matters)
xr.set_options(display_style="html")

# Inject the high-contrast style
boost_xarray_contrast()   # You can tweak colors here if you like