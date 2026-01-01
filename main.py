# main.py
# Flet WebView app: "الشهرة لتوصيل الإعلانات"

from flet import app, Page, WebView, Column, Text, UserControl, Container

APP_URL = "https://sites.google.com/view/amr-app?usp=sharing"
APP_TITLE = "الشهرة لتوصيل الإعلانات"

class WebViewer(UserControl):
    def build(self):
        return Column(
            [
                Container(
                    content=Text(APP_TITLE, size=20),
                    padding=10
                ),
                WebView(
                    src=APP_URL,
                    expand=True,
                ),
            ],
            expand=True,
            spacing=10
        )

def main(page: Page):
    page.title = APP_TITLE
    page.window_width = 900
    page.window_height = 700
    page.padding = 10
    page.add(WebViewer())

if __name__ == "__main__":
    app(target=main, view="app")  # use view="app" for desktop/web; Flet CLI will handle mobile builds
