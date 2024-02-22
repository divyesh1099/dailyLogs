# LogEntry API

The LogEntry API is a Django-based application designed to allow users to create, retrieve, update, and delete log entries. It's built using Django REST Framework and features JWT authentication, rate limiting, and full CRUD capabilities.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete log entries.
- **Authentication**: Secured endpoints with JWT authentication.
- **Rate Limiting**: Configured to prevent abuse and ensure service availability.
- **Dark Theme UI**: Frontend templates using Tailwind CSS with a dark theme.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://<my_repository_name>.git
   cd my_repository_name
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.\.venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an Admin User**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the API

- **Base URL**: `http://localhost:8000/`
- **Auth**: Obtain JWT tokens at `api/token/` and refresh them at `api/token/refresh/`.
- **Endpoints**:
  - Log Entries: `logs/` supports GET (list and create) when authenticated.
  - Single Log Entry: `logs/<id>/` supports GET, PUT, PATCH, and DELETE for individual log entries when authenticated.

### Testing with Postman

1. **Obtain JWT Token**: Send a POST request to `api/token/` with your username and password.
2. **Access Protected Endpoints**: Use the obtained JWT token as a Bearer token in the Authorization header.

## Development

### Running Tests

Run the automated tests for the application using the following command:

```bash
python manage.py test
```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Deployment

For deploying this application, you can follow standard Django deployment strategies. Check [Django's deployment checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/) for more information.

## License

This project is licensed under the [MIT License](LICENSE).