# Chinese Poetry Web Application

This project is a Flask-based web application designed for managing, querying, and generating Chinese poetry. It integrates various features, including poetry data management, AI-powered poetry generation using OpenAI, and a knowledge graph powered by Neo4j to visualize relationships among poems, authors, and key themes extracted from the poems.

## Features

- **Poetry Data Management:**  
  The application automatically loads poetry data from JSON files organized by category (e.g., Tang poetry, Song poetry). Users can search poems by title, author, or content.

- **Poetry Details & Statistics:**  
  View detailed information for individual poems along with statistics such as total poems, unique authors, and top authors based on the number of poems.

- **AI-Powered Poetry Generation:**  
  A dedicated chat page allows users to enter a prompt (theme or keyword) and generates a custom Chinese poem using OpenAI¡¯s GPT-based API.

- **Knowledge Graph Integration:**  
  The project builds a knowledge graph using Neo4j to capture relationships between:
  - **Authors** and the **poems** they created.
  - **Poems** and the **keywords** or themes they express.
  
  Users can update and query the knowledge graph through specific routes.

- **User-Friendly Navigation:**  
  A top navigation bar is available on all pages, allowing quick access to:
  - Home (Poetry Query)
  - AI-Powered Poetry Generation
  - Update Knowledge Graph
  - Query Knowledge Graph

## Installation & Setup

### Install Dependencies

Create a `requirements.txt` file containing:
- Flask
- py2neo
- openai
- jieba (optional)

Then run:

```bash
pip install -r requirements.txt
```
(Make sure to run this command in your virtual environment.)

### Configure Environment Variables
Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_openai_api_key"
```
### Configure Neo4j
Install and run Neo4j from https://neo4j.com/download/.   
Update the Neo4j connection details in the kg.py and app.py files (replace "your_password" with your actual password).

### Run the Application
Run:
```bash
python app.py
```
Then, open your web browser and navigate to http://127.0.0.1:5000.

## Usage
#### Poetry Query:
On the homepage, select a poetry category and optionally enter a search keyword. View statistics and click "View Details" to read a full poem.

#### Poem Detail:
Access detailed information about a poem, including its title, author, and full text.

#### AI Poetry Generation:
Navigate to the "AI Poetry Generation" page to enter a prompt and receive an AI-generated poem.

#### Knowledge Graph:

- Update Knowledge Graph: Visit /update_kg to build or update the Neo4j knowledge graph.
- Query Knowledge Graph: Use /query_kg (e.g., by author) to explore relationships in the graph.

## Navigation
The application features a consistent top navigation bar on all pages, providing quick links to:

- Home (Poetry Query)
- AI-Powered Poetry Generation
- Update Knowledge Graph
- Query Knowledge Graph

## License
This project is licensed under the MIT License.

## Acknowledgements
- Flask
- Neo4j
- OpenAI
- Contributions from various open-source projects in the fields of Chinese poetry, natural language processing, and knowledge graphs.