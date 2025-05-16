import gradio as gr

# 您的 Gradio 介面定義
def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# 將 Gradio 應用程式轉換為 ASGI 應用程式
# Vercel 通常會尋找一個名為 'app' 或 'application' 的 ASGI 實例
app = gr.routes.App.create_app(iface)

# 注意：在 Vercel 環境中，您不需要呼叫 iface.launch()
# Vercel 會處理 HTTP 請求的傳遞