from transformers import pipeline
from models.base_model import BaseModel

#This model was picked because it is a well-known image classification model that provides good accuracy on a variety of image datasets.
class ImageModel(BaseModel):
    def __init__(self):
        super().__init__("google/vit-base-patch16-224", "Image Classification")
        self._pipe = pipeline("image-classification", model=self._model_name)

    def run(self, file_path):
        results = self._pipe(file_path)
        output = "\n".join([f"{r['label']} ({r['score']:.2f})" for r in results])
        info = self.get_info() + "Description: Vision Transformer model for image classification.\n"
        expl = "- Encapsulation: private _pipe\n- Polymorphism: run() overridden\n- Method Overriding: each model redefines run()\n- Decorators: could add logging/timing\n"
        return output, info, expl
