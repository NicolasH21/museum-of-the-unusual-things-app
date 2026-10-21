from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import base64

load_dotenv()

app = Flask(__name__)

# Connect to OpenAI using the API key in your .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Save generated images in the static folder
STATIC_FOLDER = Path(app.root_path) / "static"
STATIC_FOLDER.mkdir(exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    label = None
    image_url = None
    prompt = ""
    error = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()

        if not prompt:
            error = "Please describe an ordinary object first."
            return render_template(
                "index.html",
                label=label,
                image_url=image_url,
                prompt=prompt,
                error=error
            )

        try:
            # STEP 1: Generate the museum label
            instructions = """
You are the curator of a fictional museum of unusual contemporary art. Transform the user's ordinary object into a compelling fictional artwork.

Follow these three rules inspired by Alix Rule and David Levine's 2012 essay "International Art English":

1. Use abstraction and nominalization, turning actions and qualities into concepts such as materiality, spatiality, relationality, and transformation.
2. Connect the object to broader cultural, social, or theoretical questions using art-critical language.
3. Use complex syntax and specialized theoretical vocabulary, while keeping the writing coherent and meaningfully connected to the actual object.

Preserve the user's original object and its specific details, including its recognizable form, material, colour, and any other details supplied. Do not replace it with a different object.

Return exactly these three sections:

ARTWORK TOMBSTONE
Include:
- Invented artist name and a one-line fictional biography
- Artwork title and year
- Medium
- Dimensions in centimetres
- Fictional provenance
- Credit line

EXTENDED LABEL
Write 80–120 words interpreting the artwork as contemporary art. Use the three International Art English-inspired rules above. Refer to one invented theorist and one invented book, clearly presented as fictional. Do not borrow the reputation or authority of real artists, critics, curators, or theorists. Keep the interpretation coherent and consistent with the artwork's physical form and medium.

IMAGE DESCRIPTION
Describe the visual artwork for image generation. Preserve the object's recognizable identity and specific details. Specify its physical scale, medium, presentation, lighting, background, and exhibition setting. Keep all details consistent with the tombstone and extended label.

Do not claim that fictional people, books, provenance, or events are real. Do not add contradictory details or unrelated objects.


"""

            text_response = client.responses.create(
                model="gpt-4.1",
                instructions=instructions,
                input=prompt,
                max_output_tokens=1200
            )

            generated_text = text_response.output_text.strip()

            parts = generated_text.split("IMAGE DESCRIPTION", 1)

            if len(parts) != 2:
                raise ValueError(
                    "The AI did not return the required image description. "
                    "Please submit the object again."
                )

            label = parts[0].strip()
            import re
            label = re.sub(r"\*\*(.*?)\*\*", r"\1", label)
            image_description = parts[1].strip()

            image_prompt = f"""
Create a high-quality contemporary art exhibition image.

Use the following AI-generated museum label as the artwork brief.
The image must visually correspond to the described artwork.

{label}

Visual description:
{image_description}

Requirements:
- Preserve the exact identity and recognizable details of the
  original everyday object.
- Match the artwork's specified medium, proportions, and scale.
- Use a coherent, physically plausible exhibition setting.
- Make the artwork the main focus of the composition.
- Use thoughtful contemporary museum lighting and presentation.
- Do not add unrelated objects or invent contradictory details.
- Do not render museum-label text, captions, or watermarks
  inside the image.
"""

            image_response = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="1024x1024"
            )

            image_data = base64.b64decode(
                image_response.data[0].b64_json
            )

            image_path = STATIC_FOLDER / "generated_artwork.png"
            image_path.write_bytes(image_data)

            image_url = "/static/generated_artwork.png?v=" + str(
                os.path.getmtime(image_path)
            )

        except Exception as e:
            app.logger.exception("Artwork generation failed")
            error = (
                "We couldn't generate your artwork. "
                "Please check your API key, API access, and billing, "
                "then try again. Details: " + str(e)
            )

    return render_template(
        "index.html",
        label=label,
        image_url=image_url,
        prompt=prompt,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)