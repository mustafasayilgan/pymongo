# hepapi — Flask + MongoDB API

Code in [`app/`](app/).  
CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)  
CD: [gitops](https://github.com/mustafasayilgan/gitops)

## Local

```sh
cd app && docker compose up --build
```

API: http://localhost:8000  

```sh
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "hepapi"}'

curl http://localhost:8000/api/items
curl http://localhost:8000/api/health
```

| Method | Path |
|--------|------|
| GET | `/api/health` |
| GET/POST | `/api/items` |
| GET/PUT/DELETE | `/api/items/<id>` |

Compose uses Mongo without auth (`MONGO_URL=mongodb://mongo:27017/`). Cluster auth is via Kubernetes Secrets in gitops.

## CI / CD

```sh
act push   # optional local run
```

| Branch | Image | GitOps bump |
|--------|-------|-------------|
| `main` | `*/hepapi:<sha>` | `apps/prod/values.yaml` |
| `develop` | `*/dev-hepapi:<sha>` | `apps/dev/values.yaml` |

Repo secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `GITOPS_REPO`, `GITOPS_TOKEN`

Argo syncs the gitops repo after the image tag commit. Details: [gitops README](https://github.com/mustafasayilgan/gitops).
