#!/usr/bin/env python3
"""Run the official Presidio Analyzer and Anonymizer against synthetic fixtures.

Generated files (and only these two files) are written to the selected output
directory: presidio_report.html and presidio_run.log.
"""

from __future__ import annotations

import argparse
import html
import json
import logging
import sys
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_FIXTURES = HERE / "sample_cases.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def load_fixtures(path: Path) -> list[dict[str, Any]]:
    fixtures = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(fixtures, list) or not fixtures:
        raise ValueError("Fixture file must contain a non-empty JSON array.")

    required = {"case_id", "description", "text", "expected_entities"}
    for index, fixture in enumerate(fixtures):
        if not isinstance(fixture, dict) or not required.issubset(fixture):
            raise ValueError(f"Fixture at index {index} is missing required fields.")
        if not isinstance(fixture["text"], str) or not fixture["text"].strip():
            raise ValueError(f"Fixture at index {index} has empty text.")
        if not isinstance(fixture["expected_entities"], list):
            raise ValueError(f"Fixture at index {index} expected_entities must be a list.")
    return fixtures


def package_version(package: str) -> str:
    try:
        return version(package)
    except PackageNotFoundError:
        return "not-installed"


def build_report(
    *,
    timestamp: str,
    execution_status: str,
    tool_version: str,
    rows: list[dict[str, Any]],
    error: str | None,
) -> str:
    executed = len(rows)
    missed_count = sum(bool(row["missed"]) for row in rows)
    unexpected_count = sum(bool(row["unexpected"]) for row in rows)

    if error:
        finding_status = "NOT_A_FINDING"
        risky_behavior = "Not assessed"
        summary = "Presidio execution failed; no security conclusion can be drawn."
    elif missed_count:
        finding_status = "POTENTIAL"
        risky_behavior = "Yes — expected fixture entity type(s) were missed"
        summary = (
            f"Presidio completed {executed} fixture(s), but expected entity types "
            f"were missed in {missed_count} fixture(s). Review as a potential privacy risk."
        )
    elif unexpected_count:
        finding_status = "FALSE_POSITIVE"
        risky_behavior = "No missed expected entity types in this fixture set"
        summary = (
            f"Presidio completed {executed} fixture(s). Unexpected entity types "
            f"were returned in {unexpected_count} fixture(s); review as fixture-level "
            "false-positive candidates."
        )
    else:
        finding_status = "OBSERVATION"
        risky_behavior = "No missed expected entity types in this fixture set"
        summary = (
            f"Presidio completed {executed} fixture(s), and detected entity types "
            "matched the declared expectations."
        )

    body_rows = []
    for row in rows:
        expected = ", ".join(row["expected"]) or "None"
        detected = ", ".join(row["detected"]) or "None"
        missed = ", ".join(row["missed"]) or "None"
        unexpected = ", ".join(row["unexpected"]) or "None"
        entity_details = "<br>".join(
            f'{html.escape(item["entity_type"])} (score {item["score"]:.2f})'
            for item in row["details"]
        ) or "None"
        body_rows.append(
            "<tr>"
            f'<td>{html.escape(row["case_id"])}</td>'
            f'<td>{html.escape(row["description"])}</td>'
            f'<td>{html.escape(expected)}</td>'
            f'<td>{html.escape(detected)}<br><small>{entity_details}</small></td>'
            f'<td>{html.escape(missed)}</td>'
            f'<td>{html.escape(unexpected)}</td>'
            f'<td><pre>{html.escape(row["anonymized_text"])}</pre></td>'
            "</tr>"
        )

    error_html = (
        f'<section class="warning"><strong>Execution error:</strong> '
        f'{html.escape(error)}</section>'
        if error else ""
    )
    rows_html = "".join(body_rows) or (
        '<tr><td colspan="7">No fixtures were processed.</td></tr>'
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Presidio PII Assessment Report</title>
<style>
:root {{ color-scheme: light; --ink:#172033; --muted:#5d687b; --line:#dce2eb; --panel:#f5f7fb; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; padding:32px; background:#f1f4f8; color:var(--ink); font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif; }}
main {{ max-width:1400px; margin:auto; background:white; padding:32px; border:1px solid var(--line); border-radius:14px; }}
h1 {{ margin:0 0 6px; font-size:28px; }}
h2 {{ margin-top:30px; font-size:19px; }}
.muted, small {{ color:var(--muted); }}
.meta {{ display:flex; flex-wrap:wrap; gap:10px 24px; padding:16px; background:var(--panel); border-radius:10px; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin:18px 0; }}
.metric {{ padding:15px; border:1px solid var(--line); border-radius:10px; }}
.metric strong {{ display:block; font-size:22px; }}
.summary {{ padding:16px; border-left:4px solid #526b91; background:var(--panel); }}
.warning {{ margin-top:16px; padding:14px; background:#fff1f0; border:1px solid #f2c6c2; border-radius:8px; }}
.table-wrap {{ overflow-x:auto; }}
table {{ width:100%; border-collapse:collapse; font-size:13px; }}
th,td {{ text-align:left; vertical-align:top; padding:11px; border-bottom:1px solid var(--line); }}
th {{ background:var(--panel); white-space:nowrap; }}
pre {{ white-space:pre-wrap; overflow-wrap:anywhere; margin:0; font:12px/1.5 ui-monospace,monospace; }}
code {{ background:var(--panel); padding:2px 5px; border-radius:4px; }}
footer {{ margin-top:28px; padding-top:16px; border-top:1px solid var(--line); color:var(--muted); font-size:12px; }}
@media(max-width:700px) {{ body {{ padding:10px; }} main {{ padding:18px; }} }}
</style>
</head>
<body><main>
<h1>Presidio PII Assessment</h1>
<p class="muted">Synthetic fixture assessment using the official Presidio Python packages.</p>
<div class="meta">
<div><strong>Tool:</strong> Microsoft Presidio</div>
<div><strong>Analyzer version:</strong> {html.escape(tool_version)}</div>
<div><strong>Execution:</strong> {html.escape(execution_status)}</div>
<div><strong>Generated (UTC):</strong> {html.escape(timestamp)}</div>
</div>
<div class="metrics">
<div class="metric"><span class="muted">Fixtures processed</span><strong>{executed}</strong></div>
<div class="metric"><span class="muted">Fixtures with misses</span><strong>{missed_count}</strong></div>
<div class="metric"><span class="muted">Unexpected-type cases</span><strong>{unexpected_count}</strong></div>
<div class="metric"><span class="muted">Finding status</span><strong>{html.escape(finding_status)}</strong></div>
</div>
<div class="summary"><strong>Assessment summary</strong><br>{html.escape(summary)}
<br><strong>Risky behavior:</strong> {html.escape(risky_behavior)}
<br><strong>Severity:</strong> UNASSESSED
<br><strong>OWASP mapping:</strong> Not assigned — this isolated PII detection sample does not establish an application or LLM vulnerability.
</div>
{error_html}
<h2>Fixture results</h2>
<div class="table-wrap"><table>
<thead><tr><th>Test ID</th><th>Scenario</th><th>Expected types</th><th>Detected types and scores</th><th>Missed types</th><th>Unexpected types</th><th>Anonymized output</th></tr></thead>
<tbody>{rows_html}</tbody>
</table></div>
<h2>Finding validity and interpretation</h2>
<p><strong>Classification:</strong> {html.escape(finding_status)}. A missed expected type is a potential finding in this synthetic test, not a confirmed production vulnerability. An unexpected type is a fixture-level false-positive candidate. Automated output requires human review.</p>
<p><strong>Execution status:</strong> {html.escape(execution_status)}. This is independent of finding status; successful execution does not mean the detector is effective, and a detection does not itself prove a vulnerability.</p>
<h2>Limitations</h2>
<ul>
<li>Only a small synthetic fixture set was used; no production or personal data was processed.</li>
<li>Evaluation compares entity types per fixture, not exact character spans or full precision/recall.</li>
<li>Detection depends on recognizers, language, context, NLP model, and configuration.</li>
<li>Presidio documentation explicitly cautions that automated detection cannot guarantee discovery of all sensitive information.</li>
<li>No OWASP category or severity is asserted without application-level evidence and security review.</li>
</ul>
<footer>Generated locally by privacy/presidio/run_presidio.py. The execution log intentionally omits raw input text and detected values.</footer>
</main></body></html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Presidio against synthetic PII fixtures.")
    parser.add_argument(
        "--fixtures",
        type=Path,
        default=DEFAULT_FIXTURES,
        help="Path to the JSON fixture file (default: sample_cases.json).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=HERE / "output",
        help="Directory for the HTML report and execution log (default: output/).",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    log_path = args.output_dir / "presidio_run.log"
    report_path = args.output_dir / "presidio_report.html"
    logger = logging.getLogger("presidio_sample")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)sZ %(levelname)s %(message)s"))
    logger.addHandler(handler)

    timestamp = utc_now()
    analyzer_version = package_version("presidio-analyzer")
    execution_status = "FAILED"
    rows: list[dict[str, Any]] = []
    error: str | None = None

    try:
        fixtures = load_fixtures(args.fixtures)
        from presidio_analyzer import AnalyzerEngine
        from presidio_anonymizer import AnonymizerEngine

        analyzer = AnalyzerEngine()
        anonymizer = AnonymizerEngine()
        logger.info("Presidio analyzer initialized; fixtures=%d", len(fixtures))

        for fixture in fixtures:
            expected = sorted(set(fixture["expected_entities"]))
            results = analyzer.analyze(
                text=fixture["text"],
                language="en",
                entities=expected or None,
            )
            detected = sorted({result.entity_type for result in results})
            missed = sorted(set(expected) - set(detected))
            unexpected = sorted(set(detected) - set(expected))
            anonymized = anonymizer.anonymize(
                text=fixture["text"],
                analyzer_results=results,
            ).text
            details = [
                {"entity_type": result.entity_type, "score": float(result.score)}
                for result in results
            ]
            rows.append(
                {
                    "case_id": fixture["case_id"],
                    "description": fixture["description"],
                    "expected": expected,
                    "detected": detected,
                    "missed": missed,
                    "unexpected": unexpected,
                    "details": details,
                    "anonymized_text": anonymized,
                }
            )
            logger.info(
                "Fixture %s complete: expected_types=%d detected_types=%d missed=%d unexpected=%d",
                fixture["case_id"], len(expected), len(detected), len(missed), len(unexpected),
            )

        execution_status = "EXECUTED"
        logger.info("Execution completed successfully.")
    except Exception as exc:  # Keep a failure report and diagnostic log.
        error = f"{type(exc).__name__}: {exc}"
        logger.exception("Presidio execution failed.")
        print(f"Presidio execution failed: {error}", file=sys.stderr)

    report = build_report(
        timestamp=timestamp,
        execution_status=execution_status,
        tool_version=analyzer_version,
        rows=rows,
        error=error,
    )
    report_path.write_text(report, encoding="utf-8")
    logger.info("HTML report written: %s", report_path.name)
    logger.info("Execution status: %s", execution_status)
    logger.info("Generated artifacts: presidio_report.html, presidio_run.log")
    for file_handler in logger.handlers:
        file_handler.flush()
        file_handler.close()
    logger.handlers.clear()

    print(f"Execution status: {execution_status}")
    print(f"HTML report: {report_path}")
    print(f"Execution log: {log_path}")
    return 0 if execution_status == "EXECUTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
