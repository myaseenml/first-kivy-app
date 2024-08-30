from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from jnius import autoclass

# Access Android's activity and WebView classes
PythonActivity = autoclass('org.kivy.android.PythonActivity')
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')

class MyWebApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWebApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Widget())  # Placeholder widget

        self.webview = WebView(PythonActivity.mActivity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.setWebViewClient(WebViewClient())
        self.webview.loadUrl('https://yaseenuom.pythonanywhere.com/')

        # Add a button to return to the app
        self.add_widget(Button(text='Back', size_hint=(1, 0.1), on_release=self.back_to_app))

        # Adding the WebView to the layout
        Window.add_widget(self.webview)

    def back_to_app(self, instance):
        # Remove the WebView when returning to the app
        Window.remove_widget(self.webview)

class MyApp(App):
    def build(self):
        return MyWebApp()

if __name__ == '__main__':
    MyApp().run()
