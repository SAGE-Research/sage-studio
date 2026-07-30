# SAGE Studio

SAGE Studio (`isage-studio`) is the visual workflow editor for the SAGE
ecosystem. It combines a React/TypeScript canvas with a FastAPI integration
layer that turns saved visual flows into SAGE pipelines.

The current Studio scope is deliberately narrow:

- visual flow editing and persistence;
- operator discovery and configuration;
- pipeline construction and execution;
- endpoint configuration;
- Studio process and frontend lifecycle management.

Inference-engine scheduling belongs to the `sagellm-*` projects, and SAGE core
execution belongs to the `isage-*` framework packages. Studio integrates those
capabilities; it does not duplicate them. The detailed boundary is recorded in
[`docs/boundary_phase1.md`](docs/boundary_phase1.md).

## Architecture

```text
React + TypeScript frontend
  ├─ Flow editor and operator palette
  ├─ Playground and output preview
  └─ Domain API clients and stores
             │ HTTP / REST
             ▼
FastAPI integration layer (`sage.studio.api.app`)
  ├─ authentication routes
  ├─ canvas / flow routes
  └─ endpoint configuration routes
             │ Python API
             ▼
Studio services
  ├─ NodeRegistry
  ├─ PipelineBuilder
  ├─ PlaygroundExecutor
  └─ WorkflowGenerator
             │
             ▼
SAGE and SageLLM packages
```

The backend entry point is `sage.studio.api.app:app`. The frontend production
bundle is mounted by the FastAPI app when `frontend/dist/` exists.

## Requirements

- Python 3.11 or newer
- Node.js 18 or newer
- an existing non-venv Python environment (for example, Conda or the system
  interpreter selected for this workspace)

## Installation

The quickstart script installs the package, development dependencies, optional
Studio integrations, frontend dependencies, and repository hooks:

```bash
git clone https://github.com/SAGE-Research/sage-studio.git
cd sage-studio
./quickstart.sh
```

Available modes:

```bash
./quickstart.sh --standard  # core dependencies only
./quickstart.sh --full      # optional runtime integrations
./quickstart.sh --dev       # development + full extras
./quickstart.sh --doctor    # environment diagnostics
```

To install manually, bind pip to the active interpreter:

```bash
python -m pip install -e ".[dev,full]"
cd src/sage/studio/frontend
npm install
```

## Run Studio

The package registers a `studio` plugin with the SAGE CLI:

```bash
sage studio start
sage studio status
sage studio open
sage studio logs
sage studio logs --backend --follow
sage studio stop
```

Useful lifecycle options:

```bash
sage studio start --dev
sage studio start --prod
sage studio start --port 5173 --backend-port 8765
sage studio restart
sage studio stop --all
```

For frontend-only development:

```bash
sage studio npm install
sage studio npm run dev
```

For a production frontend build:

```bash
sage studio build
sage studio start --prod
```

## Backend API

The application factory is exposed directly for backend development:

```bash
python -m uvicorn sage.studio.api.app:app \
  --host 127.0.0.1 \
  --port 8765
```

The current backend surface includes:

- `GET /health`
- authentication routes under `/api/auth`
- endpoint configuration routes under `/api/config/v1`
- canvas, flow, operator, and execution routes from
  `sage.studio.api.canvas`

The OpenAPI document at `/docs` is the authoritative route inventory for a
running backend.

## Project Layout

```text
src/sage/studio/
├── api/                 FastAPI application and routers
├── application/         Studio lifecycle orchestration
├── contracts/           shared backend data contracts
├── frontend/            React/TypeScript application
├── runtime/             external runtime and endpoint adapters
├── services/            workflow, registry, and execution services
├── supervisor/          process, port, and health primitives
├── cli.py               SAGE CLI plugin
└── studio_manager.py    stable public manager facade
```

Key implementation paths:

- `src/sage/studio/api/app.py`
- `src/sage/studio/application/studio_manager.py`
- `src/sage/studio/services/node_registry.py`
- `src/sage/studio/services/pipeline_builder.py`
- `src/sage/studio/frontend/src/`

## Development

Run backend tests and checks:

```bash
python -m pytest tests/
ruff check src/ tests/
ruff format --check src/ tests/
```

Run frontend checks:

```bash
cd src/sage/studio/frontend
npm test -- --run
npm run lint
npm run build
```

When a change affects startup, API routes, dependencies, or directory
ownership, update this README, `CONTRIBUTING.md`, and
`docs/boundary_phase1.md` in the same pull request. The repository PR template
contains the corresponding documentation checklist.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup, validation, and pull request
guidance.

## License

SAGE Studio is distributed under the MIT License. See [`LICENSE`](LICENSE).
