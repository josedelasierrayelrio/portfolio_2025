import reflex as rx
from reflex.style import toggle_color_mode
from rxconfig import config
from .lang.translations import *
from .css.css import *


class State(rx.State):
    language: str = "en"

    @rx.event
    def set_language(self, new_language: str):
        self.language = new_language

    @rx.var(cache=True)
    def get_greeting(self) -> str:
        return get_greetings(self.language)


class Header:
    def __init__(self) -> None:
        def creation_menu_item_language(language: str):
            dict_lang: dict = get_selected_languages(language)
            lang = str(get_selected_languages(language)[language])
            print(lang)
            print(dict_lang)
            print(dict_lang[language]["language"])
            print(dict_lang[language]["shortcut"])
            return rx.menu.item(
                dict_lang[language]["language"],
                shortcut=dict_lang[language]["shortcut"].upper(),
                on_click=State.set_language(language),
            )

        self.email = rx.stack(
            rx.hstack( 
                rx.icon(
                    tag="mail",
                    size=16,
                ),
                rx.text(
                    "josedelasierrayelrio@gmail.com",
                ),
                align="center",
                justify="center",
                spacing="2",
            ),
            color=rx.color_mode_cond(light="#313131", dark="#F5F2EA"),
        )

        # Botón de cambiar el tema
        self.theme = rx.button(
            rx.color_mode_cond(light=rx.icon(tag="sun"), dark=rx.icon(tag="moon")),
            on_click=toggle_color_mode,
            variant="ghost",
            style=css.get("button"),
            color=rx.color_mode_cond(light="#313131", dark="#F5F2EA"),
        )

        # Botón para cambiar de idioma
        self.language = rx.menu.root(
            rx.menu.trigger(
                rx.box(
                    rx.button(
                        rx.icon(tag="languages"),
                        variant="ghost",
                        style=css.get("button"),
                        color=rx.color_mode_cond(light="#313131", dark="#F5F2EA"),
                    )
                )
            ),
            rx.menu.content(
                creation_menu_item_language("es"),
                creation_menu_item_language("en"),
                creation_menu_item_language("val"),
            ),
        )

        # Caja de los botones
        self.heading_box_button = rx.hstack(
            self.language,
            self.theme,
        )

    def compile_component(self) -> list[rx.Component]:
        return [
            rx.box(
                rx.stack(
                    self.email,
                    rx.spacer(),
                    self.heading_box_button,
                    justify="between",
                    align="center",
                    spacing="9",
                ),
                width="100%",
                height="100%",
            )
        ]

    def build(self) -> rx.Component:
        return rx.hstack(
            *self.compile_component(),
            width="100%",
            style={
                "border": "1px solid red",
            },
        )


# Contenedor central
class Main:
    def __init__(self) -> None:
        self.box = rx.box(
            width="100%",
            height="100%",
            style={
                "border": "1px solid yellow",
            },
        )

        self.name = rx.hstack(
            rx.text(
                State.get_greeting,
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="600",
                style=css.get("effect_text"),
            ),
            rx.text(
                "👋🏼",
                size="7",
                style={"border": "1px solid green"},
            ),
            style={"border": "1px solid green"},
            spacing="3",
        )

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                style=css.get("main").get("property"),
            ),
        )

    def build(self):
        self.box.children = [self.compile_desktop_component()]
        return self.box


# Contenedor padre principal, desde donde se llama todo para su renderización. Es la landing page
@rx.page(route="/")
def landing() -> rx.Component:
    header = Header().build()
    main = Main().build()

    return rx.box(
        rx.vstack(
            header,
            main,
            style=css.get("header"),
            background=rx.color_mode_cond(
                light=css.get("dots_background")["light"]["background"],
                dark=css.get("dots_background")["dark"]["background"],
            ),
            background_size=rx.color_mode_cond(
                light=css.get("dots_background")["light"]["background_size"],
                dark=css.get("dots_background")["dark"]["background_size"],
            ),
            background_color=rx.color_mode_cond(light="#F5F2EA", dark="#141618"),
            height="100vh",
            width="100%",
        ),
        height="100vh",
        width="100%",
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
    ),
)
