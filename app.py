import gradio as gr

def greet(name):
    return "Hello " + name + "!"

def main():
    gr.Interface(fn=greet, inputs="text", outputs="text").launch()

if __name__ == '__main__':
	main()
