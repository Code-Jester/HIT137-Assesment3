from transformers import pipeline
from models.base_model import BaseModel

#This model was picked because it is a lightweight version of GPT-2 that balances performance and resource usage, making it suitable for text generation tasks in a GUI application.
class TextModel(BaseModel):
    def __init__(self):
        super().__init__("distilgpt2", "Text Generation")
        self._pipe = pipeline("text-generation", model="distilgpt2")

    def run(self, prompt):
        if not prompt:
            return "No input provided.", "", ""
        result = self._pipe(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
        info = self.get_info() + "Description: Lightweight GPT-2 model for generating text.\n"
        expl = "- Encapsulation: private _pipe\n- Polymorphism: run() overridden\n- Method Overriding: each model redefines run()\n- Decorators: could add logging/timing\n"
        return result, info, expl
