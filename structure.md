crm/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── contact.py
│   │   ├── deal.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── contact.py
│   │   ├── deal.py
│   │   └── task.py
│   └── routers/
│       ├── __init__.py
│       ├── contacts.py
│       ├── deals.py
│       └── tasks.py
├── requirements.txt
└── README.md


fastapi==0.68.0
uvicorn==0.15.0
sqlalchemy==1.4.23
pydantic==1.8.2

