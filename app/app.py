# This code is initial demo codes. It will be deleted after the first demo.

import gradio as gr


def greet(name: str, intensity: int) -> str:
    return "Hello, " + name + "!" * int(intensity)


def create_interface():
    return gr.Interface(fn=greet, inputs=["text", "slider"], outputs=["text"])
