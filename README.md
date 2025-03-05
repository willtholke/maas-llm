# maas-llm [WIP]

MaaS for your LLM API calls.

## What does this enable?

  - Comprehensive API usage logging with detailed request/response tracking
  - Configurable data export formats (CSV, JSON)
  - Rate limiting prevention strategies
    - Load balancing across multiple OpenAI accounts w/ rotating API keys
    - Intelligent request queuing and prioritization
    - Custom retry logic upon rate limiting by OpenAI
- Unrestricted prompt pre-processing
  - Use open-source models to reduce requests to necessary information, decreasing token costs
  - Integration with search APIs to contextualize requests
  - Pre-filtering to reduce likelihood of rejected API requests
- Unrestricted post-processing of model outputs
  - Content filtering and safety guardrails
  - Response formatting and standardization
- Integration with NVIDIA guardrails for enhanced content safety
- Model distillation capabilities

### Prioritized Features

- Comprehensive API usage logging with detailed request/response tracking
- Configurable Next.js 15 (React 18) + shadcn-ui + Tailwind CSS dashboard with features beyond OpenAI’s platform dashboard

### Deprioritized Features

- Everything else

## Requirements

1. **Supabase Account**
   - Create a [Supabase](https://supabase.com) account
   - Set up a new Supabase project
   - Obtain your project URL, API key, and database password

2. **OpenAI API Access**
   - Create an [OpenAI](https://openai.com/api/) developer account
   - Generate an API key

## Getting Started

1. Install pipenv
   ```bash
   pip3 install pipenv
   ```

2. Install dependencies
   ```bash
   pipenv install
   ```

3. Activate the virtual env
   ```bash
   pipenv shell
   ```

4. Generate a Django secret key:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'   
   ```

5. Create a `.env.local` file in the root directory with the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DB_PWD=your_database_password
   SUPABASE_PROJECT_URL=your_supabase_project_url
   SUPABASE_API_KEY=your_supabase_api_key
   DJANGO_SECRET_KEY=your_generated_django_secret_key
   DEBUG=True
   ```
6. Start the server
   ```bash
   make start
   ```

## Supabase Database Management

### Creating a Django Admin User

To view logs via the Django admin interface:

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Start the Django server:
   ```bash
   python manage.py runserver
   ```

3. Access the admin interface at http://localhost:8000/admin

### Database Migrations

When modifying the `OpenAIRequestLog` model:

1. Create migrations:
   ```bash
   python manage.py makemigrations openai_proxy
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate openai_proxy
   ```

4. Restart the server
   ```bash
   make restart
   ```
