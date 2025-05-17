import gradio as gr
from fastapi import FastAPI
import uvicorn

# Gradio 接口
def greet(name):
    return f"Hello, {name}!"

gradio_app = gr.Interface(fn=greet, inputs="text", outputs="text")
app = FastAPI()

# Mount Gradio app 到 FastAPI（將其轉換成 ASGI app）
app.mount("/gradio", gradio_app)

# 啟動 uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

