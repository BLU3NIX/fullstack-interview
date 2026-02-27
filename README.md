# Todo Backend

A RESTful API for managing todos built with FastAPI, SQLAlchemy, and SQLite.

## Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server

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


## API Endpoints

All endpoints require the `X-API-Key` header for authentication.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos/read` | Get all todos |
| POST | `/todos/create` | Create a new todo |
| PATCH | `/todos/update/{id}` | Update a todo |
| DELETE | `/todos/delete/{id}` | Delete a todo |

## Request Examples

### Get all todos
```http
GET /todos/read
X-API-Key: your-api-key
```

```
curl -X GET http://localhost:8000/todos/read
```

### Create a todo
```http
POST /todos/create
Content-Type: application/json

{
    "name": "Buy groceries",
    "order": 1,
    "completed": false
}
```

### Update a todo
```http
PATCH /todos/update/1
Content-Type: application/json

{
    "completed": true
}
```

### Delete a todo
```http
DELETE /todos/delete/1
```

## Response Format

### Success Response (Create/Update/Delete)
```json
{
    "success": true,
    "created_todo": { "id": 1, "name": "...", "order": 1, "completed": false },
    "error": null
}
```

### Error Response
```json
{
    "success": false,
    "created_todo": null,
    "error": "Error message"
}
```

# Todo Frontend

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

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

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

The application should do the following:
- Use the provided endpoints to fetch, create, edit, and delete todo items
- Currently fetched items should be stored in state
- Display the todo items as a list
- Each item should be checkable and deletable
- Add items via a text input + button
- Include an "Edit" Button for updating todos
 
<img width="1898" height="658" alt="image" src="https://github.com/user-attachments/assets/4a9cd88f-b877-42f6-a981-ef4053ebb420" />
