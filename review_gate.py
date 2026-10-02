# ==============================================================================
# Task 3.4 — Review Gate Tool with Audit Log (review_gate_v1)
# ==============================================================================

import json
import uuid
from datetime import datetime, timezone
from draft_report import draft_report_v1
from metrics_engine import flagged_regions, monthly_summary


# Task 3.4: Review gate function
def review_gate_v1(report, decision, reviewer_note="Reviewed and approved."):
    if decision not in ['approve', 'edit', 'reject']:
        raise ValueError("Decision must be approve, edit, or reject.")

    if decision == "approve":
        external_use_allowed = True
    else:
        external_use_allowed = False

    review_report = {
        'run_id': report['run_id'],
        'region': report['region'],
        "report": report['report'],
        "decision": decision,
        "external_use_allowed": external_use_allowed,
        "reviewer_note": reviewer_note
    }

    audit_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "run_id": review_report['run_id'],
        "region": review_report['region'],
        "decision": review_report['decision'],
        "reviewer_note": review_report['reviewer_note']
    }

    with open('audit_log.jsonl', 'a', encoding='utf-8') as f:
        f.write(json.dumps(audit_entry) + "\n")

    return review_report

if __name__ == "__main__":
    drafts = draft_report_v1(flagged_regions, monthly_summary)
    run_id = str(uuid.uuid4())

    print("--- Test 1: Approve Path ---")
    report_approve = {
        'run_id': run_id,
        'region': 'Guntur',
        'report': drafts['Guntur']
    }
    print("BEFORE:", report_approve)
    reviewed_approve = review_gate_v1(
        report_approve,
        'approve',
        "Reviewed against Part 2 metrics."
    )
    print("AFTER:", reviewed_approve)

    print("\n--- Test 2: Edit Path ---")
    report_edit = {
        'run_id': run_id,
        'region': 'Hyderabad',
        'report': drafts['Hyderabad']
    }
    print("BEFORE:", report_edit)
    reviewed_edit = review_gate_v1(
        report_edit,
        'edit',
        "Please revise the wording before external use."
    )
    print("AFTER:", reviewed_edit)

    print("\n--- Test 3: Reject Path ---")
    report_reject = {
        'run_id': run_id,
        'region': 'Visakhapatnam',
        'report': drafts['Visakhapatnam']
    }
    print("BEFORE:", report_reject)
    reviewed_reject = review_gate_v1(
        report_reject,
        'reject',
        "Evidence requires further verification."
    )
    print("AFTER:", reviewed_reject)
