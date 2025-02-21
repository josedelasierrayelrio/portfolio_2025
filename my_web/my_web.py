import reflex as rx
from reflex.style import toggle_color_mode
from rxconfig import config
from .lang.translations import *
from .css.css import *
from .utils.const import *


class State(rx.State):
    language: str = "en"

    @rx.event
    def set_language(self, new_language: str):
        self.language = new_language

    @rx.var(cache=True)
    def get_badges(self) -> list[str]:
        return get_list_text(self.language, "badge")

    @rx.var(cache=True)
    def get_greeting(self) -> str:
        return get_text(self.language, "greeting")


class Header:
    def __init__(self) -> None:
        # Método que crea las opciones de seleccionar item
        def creation_menu_item_language(language: str) -> rx.Component:
            dict_lang: dict = get_selected_languages(language)
            lang = str(get_selected_languages(language)[language])
            return rx.menu.item(
                rx.text(dict_lang[language]["language"]),
                # shortcut=dict_lang[language]["shortcut"].upper(),
                on_click=State.set_language(language),
            )

        self.email = rx.stack(
            rx.hstack(
                rx.icon(
                    tag="mail",
                    size=16,
                ),
                rx.text(EMAIL),
                align="center",
                justify="center",
                spacing="2",
            ),
            color=rx.color_mode_cond(light=C_DEEP_BLUE, dark=C_LIGHT_BLUE),
        )

        # Botón de cambiar el tema
        self.theme = rx.button(
            rx.color_mode_cond(light=rx.icon(tag="sun"), dark=rx.icon(tag="moon")),
            on_click=toggle_color_mode,
            variant="ghost",
            style=css["button"],
            color=rx.color_mode_cond(light=C_DEEP_BLUE, dark=C_LIGHT_BLUE),
        )

        # Botón para cambiar de idioma
        self.language = rx.menu.root(
            rx.menu.trigger(
                rx.box(
                    rx.button(
                        rx.icon(tag="languages"),
                        variant="ghost",
                        style=css["button"],
                        color=rx.color_mode_cond(light=C_DEEP_BLUE, dark=C_LIGHT_BLUE),
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
                style=css["effect_text"],
            ),
            rx.text(
                "👋🏼",
                size="7",
                style=wave,
            ),
            wrap="wrap",
            style={"border": "1px solid green"},
            spacing="3",
        )
        # Crea los badges
        self.badge_stack_max = rx.hstack(
            rx.foreach(State.get_badges, lambda title: self.create_badges(title)),
            spacing="3",
        )

        self.badge_stack_min = rx.vstack(
            rx.foreach(State.get_badges, lambda title: self.create_badges(title)),
            spacing="3",
        )

        # Crea los enlaces a redes sociales
        self.social_media_links = rx.hstack(
            rx.foreach(
                ICON_PATHS,
                lambda paths: self.create_social_media_links(
                    paths[0], paths[1], paths[2]
                ),
            ),
            spacing="3",
        )

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                self.social_media_links,
                style=css["main"]["property"],
            ),
        )

    def build(self):
        self.box.children = [self.compile_desktop_component()]
        return self.box

    # Crea los badgets bajo el saludo
    def create_badges(self, title: str) -> rx.Component:
        return rx.badge(
            rx.text(
                title.upper(),
                style=css["badges"]["badges_text"],
            ),
            color_scheme="gray",
            variant="solid",
            radius="small",
            style=css["badges"],
        )

    # Devuelve un componente con el social link
    def create_social_media_links(
        self, path: str, title: str, url: str | None
    ) -> rx.Component:
        return rx.link(
            rx.hstack(
                rx.image(
                    src=path,
                    width=css["social_media_links"]["width"],
                    height=css["social_media_links"]["height"],
                ),
                rx.text(
                    title,
                    color=rx.color_mode_cond(
                        light=css["social_media_links"]["color"]["light"],
                        dark=css["social_media_links"]["color"]["dark"],
                    ),
                ),
            ),
            href=url,
            #width=css["images"]["width"],
            #height=css["images"]["height"],
            weight="light",
            underline="hover",
            is_external="true",
        )


# Contenedor padre principal, desde donde se llama todo para su renderización. Es la landing page
@rx.page(route="/")
def landing() -> rx.Component:
    header = Header().build()
    main = Main().build()

    return rx.vstack(
        header,
        main,
        style={
            **css["header"],
            **dots["animations"],
        },  # Desempaqueta los diccionarios con **
        background=rx.color_mode_cond(
            light=dots["dots_background"]["light"]["background"],
            dark=dots["dots_background"]["dark"]["background"],
        ),
        background_size=rx.color_mode_cond(
            light=dots["dots_background"]["light"]["background_size"],
            dark=dots["dots_background"]["dark"]["background_size"],
        ),
        background_color=rx.color_mode_cond(
            light=C_BACKGROUND_LIGHT, dark=C_BACKGROUND_DARK
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
    ),
)
