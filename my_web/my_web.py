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
    def get_greetings(self) -> str:
        return get_text(self.language, "greeting")

    @rx.var(cache=True)
    def get_curriculum_text(self) -> str:
        return get_text(self.language, "CV")


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

        self.email = rx.link(
            rx.hstack(
                rx.image(
                    src=rx.color_mode_cond(
                        light=DARK_ICON_MAIL,
                        dark=LIGHT_ICON_MAIL,
                    ),
                    width=css["social_media_links"]["image_width"],
                    height=css["social_media_links"]["image_height"],
                ),
                rx.text(EMAIL),
                align="center",
                justify="center",
                spacing="2",
            ),
            href=MAILTO,
            is_external=True,
            trim="normal",
            underline="hover",
            color_scheme="orange",
            color=rx.color_mode_cond(light=C_DEEP_BLUE, dark=C_LIGHT_BLUE),
        )

        # Botón de cambiar el tema
        self.theme = rx.button(
            rx.color_mode_cond(light=rx.icon(tag="sun"), dark=rx.icon(tag="moon")),
            on_click=toggle_color_mode,
            variant="ghost",
            style=css["button"],
            color=rx.color_mode_cond(light=C_DEEP_ORANGE, dark=C_LIGHT_BLUE),
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
                ),
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
                State.get_greetings,
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="600",
                style=css["effect_text"],
            ),
            rx.text(
                HAND,
                size="7",
                style=wave,
            ),
            wrap="wrap",
            style={"border": "1px solid green"},
            spacing=MAIN_SPACING,
        )

        # Crea los enlaces a redes sociales para el tamaño máximo
        self.social_media_links_max = rx.flex(
            rx.foreach(
                ICON_PATHS,
                lambda paths: self.create_social_media_links(
                    paths[0], paths[1], paths[2]
                ),
            ),
            spacing=MAIN_SPACING,
            flex_wrap="wrap",
            width="100%",
        )

        # Crea los enlaces a redes sociales para el tamaño mínimo
        self.social_media_links_min = rx.flex(
            rx.foreach(
                ICON_PATHS,
                lambda paths: self.create_social_media_links(
                    paths[0], paths[1], paths[2]
                ),
            ),
            spacing=MAIN_SPACING,
            flex_wrap="wrap",
            width="100%",
        )

        # Crea el botón de descargar currículum
        self.download_cv = rx.button(
            rx.link(
                rx.text(
                    State.get_curriculum_text,
                    color=C_DEEP_BLUE,
                    style=css["social_media_links"]["link_text"],
                ),
                weight="medium",
                href=CV,
                is_external=True,
                trim="normal",
                underline="none",
            ),
            radius="small",
            background_color=C_ORANGE,
            style=css["social_media_links"],
            _hover=css["social_media_links"]["_hover_CV"],
        )

    # Responsivo para tablet y desktop
    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                rx.hstack(
                    self.download_cv,
                    self.social_media_links_max,
                ),
                style=css["main"]["property"],
                spacing=MAIN_SPACING,
            ),
        )

    # Responsivo para mobile
    def compile_mobile_component(self):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                self.download_cv,
                self.social_media_links_max,
                spacing=MAIN_SPACING,
            ),
        )

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
        return rx.button(
            rx.link(
                rx.hstack(
                    rx.image(
                        src=path,
                        width=css["social_media_links"]["image_width"],
                        height=css["social_media_links"]["image_height"],
                    ),
                    rx.text(
                        title,
                        color=rx.color_mode_cond(
                            light=css["social_media_links"]["color"]["light"],
                            dark=css["social_media_links"]["color"]["dark"],
                        ),
                    ),
                    align="center",
                    justify="center",
                    spacing="1",
                ),
                href=url,
                weight="regular",
                is_external=True,
                trim="normal",
                underline="none",
            ),
            radius="small",
            background_color="rgba(255, 185, 0, 0)",
            style=css["social_media_links"],
            _hover=css["social_media_links"]["_hover_other"],
        )

    def build(self):
        self.box.children = [
            self.compile_desktop_component(),
            self.compile_mobile_component(),
        ]
        return self.box


# Contenedor padre principal, desde donde se llama todo para su renderización. Es la landing page
@rx.page(route="/")
def landing() -> rx.Component:
    header = Header().build()
    main = Main().build()

    return rx.vstack(
        rx.flex(
            rx.box(header, style=css["box_wh"]),
            rx.box(main, width="100%", height="100vh", style=css["box_wh"]),
            direction="column",
            width="100%",
            height="100vh",
            spacing="4",
            style={
                **css["header"],
                **dots["animations"],
                "minHeight": "100vh",
                "overflow": "auto",
            },
            background=rx.color_mode_cond(
                light=dots["dots_background"]["light"]["background"],
                dark=dots["dots_background"]["dark"]["background"],
            ),
            background_size=rx.breakpoints(
                initial=dots["dots_background"]["light"]["background_size"],
                sm=dots["dots_background"]["dark"]["background_size"],
            ),
            background_color=rx.color_mode_cond(
                light=C_BACKGROUND_LIGHT, dark=C_BACKGROUND_DARK
            ),
        ),
        
        style={"minHeight": "100vh", "overflow": "auto"},
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        style={
            **responsive,
            "minHeight": "100vh",
            "width": "100%",
        },
    ),
)
