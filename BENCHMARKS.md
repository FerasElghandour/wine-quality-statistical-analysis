# Reproduction and benchmark scope

The full retained analysis has been rerun against the real 6,497-row wine table, with exact source/input hashes and captured outputs.

## Execute a recorded profile

```sh
python run_reproduction.py --profile checks --output reproduced/checks
```

Use a new output directory for each run. The driver writes command logs, source/input SHA-256 values, versions and an explicit outcome. It does not silently download data or turn generated fixtures into dataset-performance claims.

| Profile | Actual scope | Required inputs |
|---|---|---|
| `checks` | Source parsing only; not model training or behavior verification | None |
| `full-notebook` | Execute retained notebook against an explicitly supplied input; preserves the original experiment protocol | csv |

Supply named paths with `--input name=/absolute/path`. Exact commands are versioned in [reproduction.json](reproduction.json); direct training commands and preparation contracts are below.

## Evidence boundary

The contrast remains observational and pooled; it is not a causal alcohol-quality effect.

Keep input acquisition and source credits in [DATA.md](DATA.md). Historical results, new reference runs and small contract fixtures have separate evidential scope.

## Recorded command definitions

### checks

```text
{python} scripts/validate_source.py
```

### full-notebook

```text
{python} reproduce.py --input {input:csv} --output {output}/notebook
```

`{python}` is the current interpreter. `{output}` is the new run directory. `{input:name}` refers to a named absolute input path supplied to the driver. Install declared dependencies in a clean environment before executing. Never execute untrusted serialized models or notebooks.
