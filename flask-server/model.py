import bigframes.dataframe
import vertexai
# 'us-central1',animated-scope-418820
# TODO(developer): Vertex AI SDK - uncomment below & run
import bigframes.dataframe
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import time
import pandas
import io
import os

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
            # Part.from_uri('./fake-agetriarxi.mp4', mime_type="video/mp4"),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.05.18 AM.png', mime_type='image/png'),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.05.51 AM.png', mime_type='image/png'),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.07.04 AM.png', mime_type='image/png'),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.07.26 AM.png', mime_type='image/png'),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.07.48 AM.png', mime_type='image/png'),
            # Part.from_uri('./Screenshot 2024-03-31 at 4.08.22 AM.png', mime_type='image/png'),
            Part.from_uri(path, mime_type="image/jpeg"),
            # Add an example query
            "Tell me if this is a real or AI-generated image."
            # "Tell me if synthesis artifacts are in the face. Must return with 1) yes or no only; 2) if yes, explain where the artifacts exist by answering in [region, artifacts] form."
            # "I want you to work as an image forensic expert for AI-generated faces. Check if the second image has the artifact attribute listed in the following list and ONLY return the attribute number in this image. The artifact list is [1-asymmetric eye iris; 2-irregular glasses shape or reflection; 3-irregular teeth shape ore texture; 4-irregular ears or earrings; 5-strange hair texture; 6-inconsistent skin texture; 7-inconsistent lighting and shading; 8-strange background; 9-weird hands; 10-unnatural edges]."
        ]
    )
    print(response)
        
    return response.text



# model = init_vertex()
# start_time = time.time()

# te = generate_text(model, "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg" )
# print(te)
# end_time = time.time()
# duration = end_time - start_time
# start_time = time.time()
# text = generate_text(model, "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg" )

# end_time = time.time()
# duration = end_time - start_time
# print(duration)