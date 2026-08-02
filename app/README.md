# Flask + MongoDB API

## Run with Docker

```sh
docker compose up --build
```

API: `http://localhost:8000`

### Why gunicorn instead of Flask’s server?

**Flask** is the application (routes + Mongo). `python app.py` / `app.run()` starts Flask’s **development server**, which is fine locally but not for production (weak process model; `debug` is unsafe).

**Gunicorn** is a production WSGI server: it loads the same Flask `app` and serves HTTP reliably. Docker runs gunicorn for that reason.

Create an item (browser alone only lists — use curl to POST):

```sh
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "hepapi"}'
```

Then open `http://localhost:8000/api/items` again.

## Run locally (without Docker)

```sh
pip install -r requirements.txt
python app.py
```

Requires MongoDB at `mongodb://localhost:27017/` (override with `MONGO_URL`).

| Method | Endpoint |
|--------|----------|
| GET | `/api/items` |
| GET | `/api/items/<id>` |
| POST | `/api/items` |
| PUT | `/api/items/<id>` |
| DELETE | `/api/items/<id>` |

## CI (GitHub Actions)

Workflow: [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)

Triggers: push to `develop` / `main`, or `workflow_dispatch`.

| Branch | Image | GitOps |
|--------|-------|--------|
| `develop` | `user/dev-hepapi:<sha>` | `apps/dev/values.yaml` |
| `main` | `user/hepapi:<sha>` | `apps/prod/values.yaml` |

Secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `GITOPS_REPO`, `GITOPS_TOKEN`

## CD (Argo CD)

See `../gitops` — AppProjects + `application-dev.yaml` / `application-prod.yaml`.
