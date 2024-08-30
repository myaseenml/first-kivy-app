from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from jnius import autoclass

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        if platform == 'android':
            # Load the Android WebView
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl('https://yaseenuom.pythonanywhere.com/')
            
            # Add the WebView to the layout
            layout.add_widget(webview)
        
        return layout

if __name__ == '__main__':
    MainApp().run()
