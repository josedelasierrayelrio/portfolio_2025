import reflex as rx

EMAIL: str = "josedelasierrayelrio@gmail.com"
MAILTO: str = f"mailto:{EMAIL}"
HAND: str = "👋🏼"

GITHUB_LINK: str = "https://github.com/josedelasierrayelrio"
LINKEDIN_LINK: str = "https://www.linkedin.com/in/josepedropardo/"
TWITCH_LINK: str = "https://www.twitch.tv/lasierrayelrio"
YOUTUBE_LINK: str = "https://www.youtube.com/@lasierrayelrio"
TIKTOK_LINK: str = "https://www.tiktok.com/@lasierrayelrio"
DISCORD_LINK: str = ""
TELEGRAM_LINK: str = ""
WHATSAPP_LINK: str = ""
FACEBOOK_LINK: str = ""
TWITTER_LINK: str = "https://x.com/lasierrayelrio"
INSTAGRAM_LINK: str = ""
SPOTIFY_LINK: str = ""
LINK_TREE: str = "https://linktr.ee/lasierrayelrio"

CV: str = "/CV_JP_2024.pdf"
LIGHT_ICON_CV: str = "/social_media/filled/light_curriculum.png"
LIGHT_ICON_MAIL: str = "/social_media/filled/light_email.png"
DARK_ICON_MAIL: str = "/social_media/filled/dark_email.png"

ICON_PATHS: list = [
    [rx.color_mode_cond(light="/social_media/filled/dark_linkedin.png", dark="/social_media/filled/light_linkedin.png"), "LinkedIn", f"{LINKEDIN_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_github_v2.png", dark="/social_media/filled/light_github_v2.png"), "GitHub", f"{GITHUB_LINK}"],
    [rx.color_mode_cond(light=DARK_ICON_MAIL, dark=LIGHT_ICON_MAIL), "Email", f"mailto:{EMAIL}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_twitch.png", dark="/social_media/filled/light_twitch.png"), "Twitch", f"{TWITCH_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_youtube.png", dark="/social_media/filled/light_youtube.png"), "Youtube", f"{YOUTUBE_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_tiktok.png", dark="/social_media/filled/light_tiktok.png"), "Discord", f"{TIKTOK_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_tiktok.png", dark="/social_media/filled/light_tiktok.png"), "Twitter", f"{TIKTOK_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_tiktok.png", dark="/social_media/filled/light_tiktok.png"), "Tiktok", f"{TIKTOK_LINK}"],
    [rx.color_mode_cond(light="/social_media/filled/dark_tiktok.png", dark="/social_media/filled/light_tiktok.png"), "Tiktok", f"{TIKTOK_LINK}"],
]
