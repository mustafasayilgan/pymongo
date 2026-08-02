# pymongo — Flask API + CI

Application code lives in [`app/`](app/).  
CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)  
CD / GitOps: separate repo — see `../gitops` (`https://github.com/mustafasayilgan/gitops`).

## Quick start (local)

```sh
cd app
docker compose up --build
```

## CI with act

```sh
act push
```

See [`app/README.md`](app/README.md) for secrets and the full CI/CD flow.
