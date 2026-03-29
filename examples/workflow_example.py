"""
Science Swarm Hub — Workflow Example

Demonstrates the intended external workflow for the Science Swarm Hub.
This is a REFERENCE EXAMPLE showing the API surface, not runnable production code.

The active implementation lives in:
  Foundups-Agent/modules/foundups/pqn_swarm_hub/

Workflow:
  1. Register a work unit
  2. Run computation (via detector bridge)
  3. Submit results
  4. Verify submission
  5. Record contribution
"""

from contracts.contracts import (
    PQNWorkUnit,
    rESPSubmission,
    VerificationDecision,
    ContributionRecord,
    WorkUnitStatus,
    SubmissionStatus,
    generate_id,
)


# =============================================================================
# Step 1: Register a Work Unit
# =============================================================================

def example_register_work_unit():
    """Create a bounded PQN work unit for a 7.05Hz resonance sweep."""

    work_unit_id = generate_id("work_unit", "7.05Hz_sweep", "agent_x")

    work_unit = PQNWorkUnit(
        work_unit_id=work_unit_id,
        description="7.05Hz resonance sweep — 1200 steps, dt=0.071",
        config={
            "script": "^^^&&&",
            "steps": 1200,
            "dt": 0.071,
            "seed": 42,
        },
        creator_id="agent_x",
        status=WorkUnitStatus.PENDING,
    )

    print(f"Registered work unit: {work_unit.work_unit_id}")
    print(f"  Description: {work_unit.description}")
    print(f"  Status: {work_unit.status.value}")
    return work_unit


# =============================================================================
# Step 2: Run Computation (via Detector Bridge)
# =============================================================================

def example_run_detector(work_unit: PQNWorkUnit):
    """
    In the real system, this calls:
        bridge = DetectorBridge()
        result = bridge.run(work_unit)

    The bridge internally calls pqn_alignment.run_detector(config)
    and returns a structured result dict.
    """

    # Simulated detector output
    bridge_result = {
        "events_path": "/tmp/pqn_events_abc123.json",
        "metrics_csv": "/tmp/pqn_metrics_abc123.csv",
        "metrics": {
            "coherence": 0.742,
            "pqn_rate": 0.85,
            "paradox_rate": 0.03,
            "resonance_hz": 7.05,
        },
        "steps": 1200,
        "raw_config": work_unit.config,
    }

    print(f"Detector completed: coherence={bridge_result['metrics']['coherence']}")
    return bridge_result


# =============================================================================
# Step 3: Submit Results
# =============================================================================

def example_submit_results(work_unit: PQNWorkUnit, bridge_result: dict):
    """
    In the real system, this calls:
        submission = sink.submit_from_detector(
            work_unit_id=work_unit.work_unit_id,
            bridge_result=bridge_result,
            submitter_id="agent_x",
        )
    """

    submission_id = generate_id(
        "submission", work_unit.work_unit_id, "agent_x"
    )

    submission = rESPSubmission(
        submission_id=submission_id,
        work_unit_id=work_unit.work_unit_id,
        submitter_id="agent_x",
        metrics=bridge_result["metrics"],
        artifacts=[
            bridge_result["events_path"],
            bridge_result["metrics_csv"],
        ],
        status=SubmissionStatus.PENDING_VERIFICATION,
    )

    print(f"Submitted: {submission.submission_id}")
    print(f"  Metrics: coherence={submission.metrics['coherence']}")
    print(f"  Status: {submission.status.value}")
    return submission


# =============================================================================
# Step 4: Verify Submission
# =============================================================================

def example_verify(submission: rESPSubmission):
    """
    In the real system, this calls:
        decision = verify_submission(
            submission_id=submission.submission_id,
            decision="accept",
            verifier_id="verifier_0102",
            rationale="Coherence above phi-floor threshold (0.618)",
        )

    Verification checks:
        - coherence >= 0.618 (phi-floor)
        - Future: triple-match across independent results
    """

    coherence = submission.metrics.get("coherence", 0.0)
    phi_floor = 0.618
    decision = "accept" if coherence >= phi_floor else "reject"
    rationale = (
        f"Coherence {coherence} >= phi-floor {phi_floor}"
        if decision == "accept"
        else f"Coherence {coherence} < phi-floor {phi_floor}"
    )

    decision_id = generate_id(
        "decision", submission.submission_id, "verifier_0102"
    )

    verification = VerificationDecision(
        decision_id=decision_id,
        submission_id=submission.submission_id,
        decision=decision,
        verifier_id="verifier_0102",
        rationale=rationale,
    )

    print(f"Verification: {verification.decision}")
    print(f"  Rationale: {verification.rationale}")
    return verification


# =============================================================================
# Step 5: Record Contribution
# =============================================================================

def example_record_contribution(
    work_unit: PQNWorkUnit,
    submission: rESPSubmission,
    decision: VerificationDecision,
):
    """
    In the real system, this calls:
        contribution = record_contribution(
            work_unit_id=...,
            submission_id=...,
            decision_id=...,
            contributor_id=...,
            score=...,
        )
    """

    if decision.decision != "accept":
        print("Submission rejected — no contribution recorded.")
        return None

    contribution_id = generate_id(
        "contribution",
        work_unit.work_unit_id,
        submission.submission_id,
        decision.decision_id,
    )

    # Score based on coherence (simplified)
    score = min(1.0, submission.metrics.get("coherence", 0.0))

    contribution = ContributionRecord(
        contribution_id=contribution_id,
        work_unit_id=work_unit.work_unit_id,
        submission_id=submission.submission_id,
        decision_id=decision.decision_id,
        contributor_id=submission.submitter_id,
        score=score,
    )

    print(f"Contribution recorded: {contribution.contribution_id}")
    print(f"  Contributor: {contribution.contributor_id}")
    print(f"  Score: {contribution.score}")
    return contribution


# =============================================================================
# Full Workflow
# =============================================================================

def run_full_workflow():
    """Execute the complete Science Swarm Hub workflow."""
    print("=" * 60)
    print("Science Swarm Hub — Full Workflow Example")
    print("=" * 60)

    print("\n--- Step 1: Register Work Unit ---")
    work_unit = example_register_work_unit()

    print("\n--- Step 2: Run Detector ---")
    bridge_result = example_run_detector(work_unit)

    print("\n--- Step 3: Submit Results ---")
    submission = example_submit_results(work_unit, bridge_result)

    print("\n--- Step 4: Verify Submission ---")
    decision = example_verify(submission)

    print("\n--- Step 5: Record Contribution ---")
    contribution = example_record_contribution(work_unit, submission, decision)

    print("\n" + "=" * 60)
    print("Workflow complete.")
    if contribution:
        print(f"Final score: {contribution.score}")
    print("=" * 60)


if __name__ == "__main__":
    run_full_workflow()
