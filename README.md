# maas-llm

MaaS for your LLM API calls.

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

4. Create a `.env.local` file in the root directory with the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DB_PWD=your_database_password
   SUPABASE_PROJECT_URL=your_supabase_project_url
   SUPABASE_API_KEY=your_supabase_api_key
   DJANGO_SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```
