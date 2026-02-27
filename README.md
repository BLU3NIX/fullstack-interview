# ToDo Backend

## Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database


## Project Structure

```
backend/
├── main.py          # FastAPI app initialization and middleware
├── database.py      # Database connection and session
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas for request/response
├── todos.py         # Todo endpoints router
├── requirements.txt # Python dependencies
├── request.http     # Example HTTP requests
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

- **NextJS** - 
- **TypeScript** - 
- **SCSS** -

First install the relevant packages using:
```bash
npm install
or
pnpm install
```
Then run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Your Task

The application should do the following:
- Use the provided endpoints to fetch, create, edit, and delete todo items
- Currently fetched items should be stored in state
- Display the todo items as a list
- Each item should be checkable and deletable
- Add items via a text input + button
- Include an "Edit" Button for updating todos
 
<img width="1898" height="658" alt="image" src="https://github.com/user-attachments/assets/4a9cd88f-b877-42f6-a981-ef4053ebb420" />
