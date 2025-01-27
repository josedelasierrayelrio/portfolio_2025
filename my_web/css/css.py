import reflex as rx

# Diccionario de estilos CSS
css: dict = {
    "header": {
        "width": "100%",
        "min_height": "100vh",
        "padding": [
            "2rem 1rem",
            "2rem 1rem",
            "2rem 1rem",
            "4rem 8rem",
            "4rem 8rem",
        ],
        "transition": "all 512ms ease",
    },
    "main": {
        "property": {
            "width": "100%",
            "min_height": "84vh",
            "padding": "15rem 0rem",
            "align_items": "center",
            "justify_content": "start",
        }
    },
    "effect_text": {
        "background": rx.color_mode_cond(
            light="none", dark="linear-gradient(to right, #e1e1e1, #757575)"
        ),
        "WebkitBackgroundClip": "text",
        "WebkitTextFillColor": rx.color_mode_cond(light="initial", dark="transparent"),
    },
    "mid_text": {
        "border": "3px solid green",
        "height": "auto",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
    },
    "button": {
        "background": "transparent",
    },
    "dots_background": {
        "light": {
            "background": "radial-gradient(circle, rgba(0,0,0,0.09) 1px, transparent 1px)",
            "background_size": "30px 30px",
        },
        "dark": {
            "background": "radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
            "background_size": "30px 30px",
        },
    },
}
