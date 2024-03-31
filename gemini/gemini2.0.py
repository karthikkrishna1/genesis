import bigframes.dataframe
import vertexai
# 'us-central1',animated-scope-418820
# TODO(developer): Vertex AI SDK - uncomment below & run
import bigframes.dataframe
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image
import time
import pandas
import io
import os
import http.client
import typing
import urllib.request
import json

# gcloud auth application-default login v export PATH="$PATH:/Users/cherryyang/Desktop/school/coop2/hackathon/gen2/genesis/google-cloud-sdk/bin"

def init_vertex(project_param = "animated-scope-418820", location_param = "us-central1"):
    vertexai.init(project=project_param, location=location_param)
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    return multimodal_model

# def load_image_from_url(image_url: str) -> Image:
#     with urllib.request.urlopen(image_url) as response:
#         response = typing.cast(http.client.HTTPResponse, response)
#         image_bytes = response.read()
#     return Image.from_bytes(image_bytes)

# img1 = load_image_from_url("https://storage.googleapis.com/animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.05.18_AM.png")
# img2 = load_image_from_url("https://storage.googleapis.com/animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.07.48_AM.png")
# img3 = load_image_from_url("https://storage.googleapis.com/animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.07.26_AM.png")
# img4 = load_image_from_url("https://storage.googleapis.com/animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.08.22_AM.png")
# img5 = load_image_from_url("https://storage.googleapis.com/animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.05.51_AM.png")

def generate_text(model,  path:str) -> str:
  
    response = model.generate_content(
        [
            # Add an example image
            " tell me if last image is a real or AI-generated image based on what the next three images are.",
            # Part.from_uri('./fake-agetriarxi.mp4', mime_type="video/mp4"),
            Part.from_uri('gs://animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.05.18_AM.png', mime_type='image/png'),
            "This is a deepfake image, remember the qualities and synthetic artifacts",
            Part.from_uri('gs://animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.07.48_AM.png', mime_type='image/png'),
            "This is a deepfake image, remember the qualities and synthetic artifacts",
            Part.from_uri('gs://animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.07.26_AM.png', mime_type='image/png'),
            "This is a deepfake image, remember the qualities and synthetic artifacts",
            Part.from_uri(path, mime_type='image/png'),
            # "Tell me if synthesis artifacts are in the face. Must return with 1) yes or no only; 2) if yes, explain where the artifacts exist by answering in [region, artifacts] form."
            # "I want you to work as an image forensic expert for AI-generated faces. Check if the second image has the artifact attribute listed in the following list and ONLY return the attribute number in this image. The artifact list is [1-asymmetric eye iris; 2-irregular glasses shape or reflection; 3-irregular teeth shape ore texture; 4-irregular ears or earrings; 5-strange hair texture; 6-inconsistent skin texture; 7-inconsistent lighting and shading; 8-strange background; 9-weird hands; 10-unnatural edges]."
        ]
    )
    print(response)
        
    return response.text



model = init_vertex()
# start_time = time.time()

te = generate_text(model, 'gs://animated-scope-418820.appspot.com/Screenshot_2024-03-31_at_4.08.22_AM.png')
print(te)
# end_time = time.time()
# duration = end_time - start_time
# start_time = time.time()
# text = generate_text(model, "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg" )

# end_time = time.time()
# duration = end_time - start_time
# print(duration)