"""
Science Swarm Hub FoundUp — Reference Contract Definitions

These are the canonical contract dataclasses for the Science Swarm Hub.
This file is a REFERENCE COPY for external contributors.

The active implementation lives in:
  Foundups-Agent/modules/foundups/pqn_swarm_hub/src/contracts.py

Do not import from this file directly in production code.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional
import hashlib


# --- Enums ---

class WorkUnitStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class SubmissionStatus(Enum):
    PENDING_VERIFICATION = "pending_verification"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


# --- Core Contracts ---

@dataclass
class PQNWorkUnit:
    """Bounded research task registration."""
    work_unit_id: str          # Deterministic ID
    description: str           # Human-readable description
    config: Dict[str, Any]     # CMST detector config (steps, dt, seed, etc.)
    creator_id: str            # Agent/user who created this work unit
    status: WorkUnitStatus     # pending, in_progress, completed, cancelled
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class rESPSubmission:
    """Structured rESP result intake."""
    submission_id: str         # Deterministic ID
    work_unit_id: str          # Reference to parent work unit
    submitter_id: str          # Agent/user who submitted
    metrics: Dict[str, Any]    # {coherence, pqn_rate, paradox_rate, resonance_hz}
    artifacts: List[str]       # Paths or URIs to result artifacts
    status: SubmissionStatus   # pending_verification, accepted, rejected
    submitted_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class VerificationDecision:
    """Accept/reject outcome."""
    decision_id: str           # Deterministic ID
    submission_id: str         # Reference to submission
    decision: Literal["accept", "reject"]
    verifier_id: str           # Agent/user who made decision
    rationale: str             # Why accepted/rejected
    decided_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ContributionRecord:
    """ROC-style contribution output."""
    contribution_id: str       # Deterministic ID
    work_unit_id: str          # Reference to work unit
    submission_id: str         # Reference to submission
    decision_id: str           # Reference to verification decision
    contributor_id: str        # Who earned the contribution
    score: float               # 0.0-1.0 contribution score
    recorded_at: datetime = field(default_factory=datetime.utcnow)


# --- ID Generation ---

def generate_id(entity_type: str, *args: str) -> str:
    """Generate a deterministic ID for idempotency."""
    seed = f"{entity_type}:{':'.join(args)}"
    return hashlib.sha256(seed.encode()).hexdigest()[:16]


# --- Errors ---

class WorkUnitNotFoundError(Exception):
    """Raised when work_unit_id does not exist."""
    pass


class SubmissionNotFoundError(Exception):
    """Raised when submission_id does not exist."""
    pass


class InvalidStatusTransitionError(Exception):
    """Raised when attempting an invalid status transition."""
    pass


class DuplicateSubmissionError(Exception):
    """Raised when submitting a duplicate result (idempotent - returns existing)."""
    pass
