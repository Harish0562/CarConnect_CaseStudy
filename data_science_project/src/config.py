from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    base_dir: Path

    @property
    def data_raw(self) -> Path:
        return self.base_dir / "data" / "raw"

    @property
    def data_processed(self) -> Path:
        return self.base_dir / "data" / "processed"

    @property
    def models(self) -> Path:
        return self.base_dir / "models"


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PATHS = ProjectPaths(base_dir=PROJECT_ROOT)
