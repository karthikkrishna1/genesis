import bigframes.dataframe
import vertexai
# 'us-central1',animated-scope-418820
# TODO(developer): Vertex AI SDK - uncomment below & run
import bigframes.dataframe
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import time
import pandas

import json

# gcloud auth application-default login

def init_vertex(project_param = "animated-scope-418820", location_param = "us-central1"):
    vertexai.init(project=project_param, location=location_param)
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    return multimodal_model

def generate_text(model,  path:str) -> str:
  
    response = model.generate_content(
        [
            # Add an example image
            Part.from_uri(path, mime_type="image/jpeg"),
            # Add an example query
            "Tell me if this is an ai geneerated image, answer yes or no",
        ]
    )
    print(response)
        
    return response.text



model = init_vertex()
start_time = time.time()

te = generate_text(model, "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg" )
# print(text)
end_time = time.time()
duration = end_time - start_time
# start_time = time.time()
# text = generate_text(model, "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg" )

# end_time = time.time()
# duration = end_time - start_time
# print(duration)
