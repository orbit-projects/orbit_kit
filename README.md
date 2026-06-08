# Orbit Kit

> Shared infrastructure, utilities, and developer tooling primitives for the Orbit ecosystem.

Orbit Kit provides the foundational building blocks used across Orbit packages, tooling, runtime components, and development workflows.

Rather than duplicating common functionality throughout the ecosystem, Orbit centralizes reusable infrastructure within Orbit Kit.

---

## Purpose

Orbit Kit exists to provide a stable collection of utilities that support the broader Orbit ecosystem.

These utilities are intentionally framework-agnostic and focus on common concerns such as:

* Filesystem operations
* Path resolution
* Validation
* Process execution
* Environment detection
* Runtime metadata
* Console output
* Typing utilities
* Shared exceptions

---

## Installation

```bash
pip install orbit-framework-kit
```

---

## Features

### Filesystem Utilities

Centralized filesystem operations with consistent exception handling.

```python
from orbit_kit.filesystem import (
    ensure_directory,
    read_file,
    write_file,
)
```

---

### Path Resolution

Helpers for working with filesystem paths and project locations.

```python
from orbit_kit.paths import (
    project_root,
    resolve_path,
)
```

---

### Validation Utilities

Reusable validation helpers used throughout the ecosystem.

```python
from orbit_kit.validation import (
    validate_directory,
    validate_file,
)
```

---

### Process Execution

Safe subprocess execution wrappers.

```python
from orbit_kit.process import (
    run_process,
)
```

---

### Environment Detection

Runtime and tooling discovery helpers.

```python
from orbit_kit.environment import (
    detect_node,
    detect_package_manager,
    python_executable,
)
```

---

### Runtime Metadata

Structured runtime information models.

```python
from orbit_kit.runtime import (
    RuntimeInfo,
)
```

---

### Console Output

Consistent terminal output utilities.

```python
from orbit_kit.console import (
    success,
    warning,
    error,
    info,
)
```

---

### Typing Utilities

Shared typing helpers and annotation inspection tools.

```python
from orbit_kit.typing import (
    issubclass_safe,
    is_optional_type,
)
```

---

## Design Goals

Orbit Kit is designed around several core principles:

* Consistency across the Orbit ecosystem.
* Strong typing and maintainability.
* Framework-independent infrastructure.
* Reusable developer tooling.
* Long-term scalability.

---

## Package Structure

```text
orbit_kit/
├── console/
├── environment/
├── exceptions/
├── filesystem/
├── paths/
├── process/
├── runtime/
├── typing/
└── validation/
```

---

## Role in the Orbit Ecosystem

Orbit Kit serves as a shared dependency layer for Orbit packages.

```text
orbit-types
      │
orbit-kit
      │
orbit-core
      │
orbit-server
      │
orbit-cli
```

This architecture helps keep common infrastructure centralized while reducing duplication across packages.

---

## License

MIT License.
