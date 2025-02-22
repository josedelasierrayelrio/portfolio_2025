import reflex as rx

C_BACKGROUND_LIGHT: str = "#fffffc"
C_BACKGROUND_DARK: str = "#1f1f1f"
C_RED: str = "#CE5151"
C_LIGHT_BLUE: str = "#f1faee"
C_BLUE: str = "#a8dadc"
C_MIDDLE_BLUE: str = "#457b9d"
C_DEEP_BLUE: str = "#1d3557"
C_DARK: str = "#1f1f1f"
C_ORANGE: str = "#FFB900"
C_DEEP_ORANGE: str = "#F89A00"
C_LIGHT_ORANGE: str = "#FFF2CC"
C_LIGHT_DOTS: str = ""
C_DARK_DOTS: str = ""

MAIN_SPACING: str = "3"

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
        "height": "auto",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
    },
    "button": {
        "background": "transparent",
        "_hover": {
            "color-scheme": rx.color_mode_cond(
                light=C_LIGHT_ORANGE,
                dark=C_MIDDLE_BLUE,
            ),
        },
    },
    "badges": {
        "width": "auto",
        "height": "auto",
        "badges_text": {
            "font_size": ["0.5rem", "0.85rem", "0.9rem", "1rem", "1rem"],
        },
    },
    "social_media_links": {
        "image_width": "16px",
        "image_height": "16px",
        # "border": f"1.5px solid {C_DEEP_BLUE}",
        "radius": "small",
        "width": "auto",
        "height": "auto",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "0.4em",
        "link_text": {
            "font_size": ["0.5rem", "0.85rem", "0.9rem", "1rem", "1rem"],
        },
        "color": {
            "light": C_DEEP_BLUE,
            "dark": C_LIGHT_BLUE,
        },
        "filter": {
            "light": "brightness(0) invert(0)",
            "dark": "brightness(0) invert(0)",
        },
        "_hover_CV": {
            "bg": rx.color_mode_cond(
                light=C_DEEP_ORANGE,
                dark=C_LIGHT_ORANGE,
            ),
        },
        "_hover_other": {
            "bg": rx.color_mode_cond(
                light=C_LIGHT_ORANGE,
                dark=C_MIDDLE_BLUE,
            ),
        },
    },
}

dots: dict = {
    "dots_background": {
        "light": {
            "background": "radial-gradient(circle, rgba(0,0,0,0.09) 1.5px, transparent 1px)",
            "background_size": "30px 30px",
        },
        "dark": {
            "background": "radial-gradient(circle, rgba(255,255,255,0.09) 1.5px, transparent 1px)",
            "background_size": "30px 30px",
        },
    },
    "animations": {
        "@keyframes dots": {
            "0%": {"background_position": "0 0"},
            "100%": {"background_position": "40px 40px"},
        },
        "animation": "dots 6s linear infinite alternate-reverse both",
        "-webkit-animation": "dots 6s linear infinite alternate-reverse both",
    },
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(15deg)"},
        "100%": {"transform": "rotate(-25deg)"},
    },
    "animation": "wave 0.8s cubic-bezier(0.9, 0.9, 0.9, 0.9) infinite alternate-reverse both",
}
