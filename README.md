# ToDo Backend

## Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database


## Project Structure

```
backend/
├── main.py          # FastAPI app entry point, CORS middleware setup
├── database.py      # SQLAlchemy engine, session factory, and DB dependency
├── models.py        # SQLAlchemy ORM model (Todo table)
├── schemas.py       # Pydantic schemas for request/response validation
├── todos.py         # Todo CRUD endpoint router (/todos/*)
├── requirements.txt # Python dependencies
├── sqlite.db        # SQLite database file (auto-generated)
└── venv/            # Python virtual environment (not committed)
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`


## Your Task


| Method | Endpoint | Description | Status |
|--------|----------|-------------|------|
| GET | `/todos/read` | Get all todos | Implemented |
| POST | `/todos/create` | Create a new todo | Not Implemented |
| PATCH | `/todos/update/{id}` | Update a todo | Not Implemented |
| DELETE | `/todos/delete/{id}` | Delete a todo | Not Implemented |

# ToDo Frontend

## Tech Stack

- **Next.js** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **SCSS** - CSS preprocessor for styling

## Project Structure

```
frontend/
├── app/
│   ├── page.tsx         # Main page component (todo list UI)
│   ├── layout.tsx       # Root layout with metadata and fonts
│   ├── hooks.ts         # Custom hook for todo CRUD operations
│   ├── todo-item.tsx    # Individual todo item component
│   ├── types.ts         # TypeScript type definitions
│   ├── styles.scss      # SCSS styles for the todo app
│   ├── globals.css      # Global CSS (Tailwind base styles)
│   └── favicon.ico      # App favicon
├── eslint.config.mjs    # ESLint configuration
├── next.config.ts       # Next.js configuration
├── postcss.config.mjs   # PostCSS configuration
├── tsconfig.json        # TypeScript configuration
└── package.json         # Dependencies and scripts
```

## Setup

First install the relevant packages using:
```bash
npm install
```
Then run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Your Task

The application should do the following:
- Use the provided endpoints to fetch, create, edit, and delete todo items
- Display the todo items as a list
- Fetched items should be stored in state
- Add items via a text input + button
- Each item should be checkable and deletable
 
<img width="1898" height="658" alt="image" src="https://github.com/user-attachments/assets/4a9cd88f-b877-42f6-a981-ef4053ebb420" />
