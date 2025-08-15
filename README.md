<<<<<<< HEAD
# PlayWright-Smoke-Tests
=======
# Python Playwright Smoke Tests (GitHub Actions ready)

Minimal, production-friendly scaffold for **Playwright smoke tests in Python**, wired into **GitHub Actions**.
Uses an environment variable `BASE_URL` so tests can target staging or production without code changes.

## Quick start (local)

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install --with-deps
export BASE_URL="https://example.com"  # Windows PowerShell: $env:BASE_URL="https://example.com"
pytest -m smoke --screenshot=only-on-failure --video=retain-on-failure --junitxml=artifacts/junit.xml
```

## Key files
- `tests/test_smoke.py` — example smoke tests (homepage and core nav placeholder checks).
- `conftest.py` — `base_url` fixture read from `BASE_URL`.
- `pytest.ini` — custom `smoke` marker and default options.
- `.github/workflows/ci.yml` — GitHub Actions workflow (runs on PRs and pushes to `main`).
- `.env.example` — template for environment variables.

## Customizing for your app
1. Edit tests in `tests/` to match your app's key workflows (login, capture, search, playback, etc.).
2. Set `BASE_URL` in GitHub → Settings → Secrets and variables → Actions → *New repository secret*.
3. If auth is required, uncomment and adapt the login test and add credentials as GitHub Secrets.

## GitHub setup (create & push)
```bash
git init
git add .
git commit -m "Add Python Playwright smoke tests + CI"
# Create repo on GitHub (choose one):
#   a) Using GitHub CLI (https://cli.github.com/)
#      gh repo create <your-org/your-repo> --public --source=. --remote=origin --push
#   b) Or create the repo in the GitHub UI, then:
#      git remote add origin git@github.com:<your-org/your-repo>.git
#      git branch -M main
#      git push -u origin main
```
>>>>>>> beecc28 (Initial commit)
