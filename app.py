# api/index.py
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

# 建立 Gradio 介面
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(placeholder="Your name here"),
    outputs=gr.Textbox(label="Greeting"),
    title="Greeting App"
)

# 匯出 ASGI app，Vercel 會自動使用它作為入口
app = demo.app

