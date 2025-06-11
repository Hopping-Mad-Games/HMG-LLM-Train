# Contributing

Thanks for considering a contribution!  
Below is the lightning version—see `docs/ARCHITECTURE.md` for code layout details.

1. **Fork & clone** the repo.
2. Install dev requirements:
   ```bash
   pip install -r requirements-dev.txt
   pre-commit install
   ```
3. Add your plug‑in under `plugins/<my_plugin>/`.
4. Update or create unit tests in `tests/` (pytest).
5. Run `./scripts/dev.sh` and verify UI hot‑reload.
6. Submit a PR with:
   * short title + description
   * screenshot / GIF if UI changes
   * link to issue (if applicable)

We enforce black + isort + flake8 in CI.
