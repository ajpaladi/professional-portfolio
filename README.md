# Professional Portfolio – Streamlit App

A Streamlit-powered personal portfolio that showcases Andrew Paladino’s background, experience, and side projects. The app bundles a sidebar “quick links” hub, a resume download widget, and a multi-section navigation experience that reads content from `core/app.py`.

## Features
- **Multi-page navigation** – Pick from About, Education, Experience, Projects, Certifications, and more via the sidebar select box.
- **Quick actions** – Download the latest resume PDF and jump to LinkedIn, GitHub, Medium, Etsy, and other external profiles.
- **Rich storytelling** – Each section in `core/app.py` is laid out with Streamlit markdown, images, and link buttons to highlight personal achievements.
- **Simple data storage** – Static assets (portrait photo, drone shot, resume PDF) are stored under `data/` to keep the app self-contained.

## Getting Started

### Prerequisites
- Python **3.11.x**
- [Poetry 2.2+](https://python-poetry.org/)

### Initial Setup
```bash
cd ~/Documents/projects/prof_portfolio
poetry env use python3.11        # ensures the correct interpreter
poetry install                   # installs Streamlit + pandas
```

To activate the virtual environment:
```bash
source "$(poetry env info --path)/bin/activate"
# or run commands ad hoc with: poetry run <command>
```

## Running the App
```bash
poetry run streamlit run core/app.py
```
The app opens at http://localhost:8501. Use the sidebar to switch between portfolio sections.

## Customization Tips
- **Resume & media paths** – `core/app.py` reads assets from `data/`. Replace `paladino_resume_20260101.pdf` and the `IMG_0358.jpg` portrait with your latest files or update the `Path(...)` references to your preferred location.
- **Navigation items** – Modify the `pages` list and the conditional blocks that follow to add/remove sections.
- **Links** – Update the `st.sidebar.link_button` entries for LinkedIn, GitHub, Medium, etc., to keep external profiles current.

## Project Structure
```
prof_portfolio/
├── core/
│   └── app.py          # Streamlit application entry point
├── data/               # Static assets (images, resume)
├── pyproject.toml      # Poetry + dependency definition
└── poetry.lock         # Locked dependency versions
```

## Useful Commands
- `poetry check` – validate `pyproject.toml`.
- `poetry add <package>` – add new dependencies (e.g., `poetry add geopandas`).
- `poetry run streamlit run core/app.py --server.port 8502` – start on a custom port.

Feel free to extend the layout with additional Streamlit components such as metrics, timelines, or embedded notebooks to keep the professional profile fresh.
