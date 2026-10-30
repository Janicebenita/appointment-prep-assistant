# Appointment Preparation Assistant Explainability

## Decision and reasoning

The agent decides which administrative preparation items are missing or ready. Its reasoning checks user-provided appointment time, location, questions, documents, medication list, allergy list, and transport plan against transparent completeness rules.

## Inputs and data sources

The input is a local JSON record entered by the user. The agent does not retrieve an electronic health record, contact a clinic, or use an external medical data source.

## Limits and known constraints

The principal limitation is that the checklist cannot determine whether information is medically correct or whether care is urgent. It provides organizational support only and must not be used for diagnosis, triage, medication changes, or treatment decisions.

## Implementation in This Repository

The executable implementation is in `app.py`. Its `prepare(data)` function iterates over the seven declared `CHECKS` fields, treats a supplied value as ready (including an explicitly empty allergy list), and returns each field's `ready` or `missing` status, action, and reason together with `ready_count`, `appointment_type`, and the non-clinical disclaimer.

The same file provides a command-line entry point that reads `sample_data.json` or a user-selected JSON file and prints the exact structured result. `test_app.py` checks missing-field behavior and the explicit empty-allergy case. The implementation is deterministic, has no EHR integration, clinical model, or action endpoint, and leaves every checklist item subject to patient and clinician review.

## Outputs and supporting evidence

The output contains the appointment type, number of ready items, and a checklist whose `reason` states whether each required field was provided. That direct mapping from input field to status is the supporting evidence for every action shown.

## Uncertainty and human review

The worker cannot verify that supplied information is current, complete, or medically correct. The user and clinician must review the checklist, and urgent or clinical questions must follow appropriate professional or emergency channels.
