import gradio as gr
from fastapi import FastAPI

# 您的 Gradio 介面定義
def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# 建立一個 FastAPI 應用程式並掛載 Gradio 應用程式
app = FastAPI()
app = gr.mount_gradio_app(app, iface, path="/") # 將 Gradio 掛載到根路徑

# 注意：在 Vercel 環境中，您不需要呼叫 iface.launch()
