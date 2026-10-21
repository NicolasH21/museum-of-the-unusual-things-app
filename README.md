Museum of the Unusual Things

Project Overview

Museum of the Unusual Things is an interactive, AI-powered museum experience that transforms ordinary everyday objects into fictional works of contemporary art.

Users describe an object, and the application generates an artwork tombstone, an extended museum label, and an image description. It then uses the generated text to create a visual representation of the artwork.

The project explores how artificial intelligence can imitate the language of contemporary art criticism and transform familiar objects through interpretation, abstraction, and visual representation.

How It Works

Object description: The user enters a description of an ordinary object, including details such as its shape, colour, material, and condition.

Text generation: GPT-4.1 generates an artwork tombstone and an extended museum label inspired by International Art English.

Image description: The model produces a visual description consistent with the fictional artwork and its interpretation.

Image generation: The application combines the generated museum label and image description into a prompt for GPT Image.

Artwork display: The generated image is saved in the application's static folder and displayed alongside the text.

The original object remains recognizable throughout the process. The image-generation prompt is derived from the AI-generated museum label and image description rather than relying only on the user's initial input.

International Art English

The text-generation instructions are inspired by Alix Rule and David Levine's 2012 essay, International Art English, which examines the specialized language used in contemporary art discourse.

The application incorporates three principles:

Abstraction and nominalization: Everyday qualities and actions are reframed through abstract concepts such as materiality, spatiality, relationality, and transformation.

Theoretical framing: The artwork is connected to broader cultural, social, and theoretical questions through art-critical language.

Complex syntax and specialized vocabulary: The label uses elaborate sentence structures and theoretical terminology while remaining coherent and connected to the original object.

The application also generates fictional artists, artwork details, provenance, and references to invented theorists and books. These details are presented as fictional rather than as real-world facts.

Technology

Python

Flask

OpenAI Responses API (gpt-4.1)

OpenAI Images API (gpt-image-1)

HTML and CSS

python-dotenv

Gunicorn

Running the Project Locally

Requirements

Python 3

An OpenAI API key with access to the required models

Installation

Clone or download this repository.

Open a terminal in the project directory.

Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\Activate.ps1

Install the dependencies:

pip install -r requirements.txt

Create a .env file in the project root and add your API key:

OPENAI_API_KEY=your_api_key_here

Replace the placeholder with your own API key. Never commit your .env file or expose your API key publicly.

Start the application:

python app.py

Open http://127.0.0.1:5000 in your browser.

Reflection: Language, Fluency, and Artificial Intelligence

This project explores how a language model can reproduce recognizable patterns associated with contemporary art criticism as an art curator. By using abstraction, theoretical references, and complex syntax, the generated labels imitate a rhetorical style while being inspired by International Art English.

The results can sound convincing and very sophisticated, but fluency does not necessarily indicate genuine understanding. A model can generate theoretical language that appears meaningful while remaining vague or only loosely connected to the object. For this reason, the instructions emphasize on preserving the object's specific physical details and maintaining coherence.

The image-generation stage extends this experiment from language into visual representation. What was aimed at in this assignment was to create a contemporary museum that could generate unusual artworks. Because the image prompt is created from the generated label and image description, the visual result reflects the model's interpretation of the generated text.

Ultimately, the project examines both the creative possibilities and the limitations of AI-generated art discourse: convincing creative artworks can be created, but coherence and meaningful interpretation still require attention as text can sound a bit confusing.

License

This project was created for an academic assignment. See the repository's license file for licensing information.