# Railway deployment

1. Create a new Railway project and connect the GitHub repository `jems0906/RailPulse-AI`.
2. Add a PostgreSQL database from **New > Database > Add PostgreSQL**.
3. Keep the application service rooted at the repository root so Railway uses the root `Dockerfile`.
4. Add the PostgreSQL service reference variable `DATABASE_URL` to the application service.
5. Deploy. The root container builds and serves both the dashboard and FastAPI API on one public URL.
6. API docs are available at `<service-url>/docs`; no `VITE_API_URL` variable is required.

The repository contains trained artifacts and does not train models during deployment. Railway account access, database provisioning, domains, and environment variables must be completed by the project owner.
