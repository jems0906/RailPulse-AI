# Railway deployment

1. Create a new Railway project and connect the GitHub repository `jems0906/RailPulse-AI`.
2. Add a PostgreSQL database from **New > Database > Add PostgreSQL**.
3. Create a backend service from the repository and set its Dockerfile path to `backend/Dockerfile` with `backend` as the Docker context.
4. Add the PostgreSQL service reference variable `DATABASE_URL` to the backend service. Railway can provide this from the PostgreSQL service variables panel.
5. Create a frontend service using `frontend/Dockerfile` with `frontend` as the Docker context.
6. Deploy the backend first, copy its public URL, and set `VITE_API_URL` on the frontend service to `<backend-url>/api`.
7. Run `alembic -c backend/alembic.ini upgrade head` as a release or one-time migration command before serving traffic.

The repository contains trained artifacts and does not train models during deployment. Railway account access, database provisioning, domains, and environment variables must be completed by the project owner.
