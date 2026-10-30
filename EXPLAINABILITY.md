# Appointment Preparation Assistant Explainability

## Decision and reasoning

The agent decides which administrative preparation items are missing or ready. Its reasoning checks user-provided appointment time, location, questions, documents, medication list, allergy list, and transport plan against transparent completeness rules.

## Inputs and data sources

The input is a local JSON record entered by the user. The agent does not retrieve an electronic health record, contact a clinic, or use an external medical data source.

## Limits and known constraints

The principal limitation is that the checklist cannot determine whether information is medically correct or whether care is urgent. It provides organizational support only and must not be used for diagnosis, triage, medication changes, or treatment decisions.

## Implementation in This Repository

`app.py` reads the local appointment record, applies deterministic completeness checks, and produces the preparation checklist. `sample_data.json` supplies a reproducible example, and `test_app.py` exercises the implemented parsing and recommendation behavior.

There is no EHR integration, clinical model, or action endpoint in the code. The returned checklist is transparent because each item follows directly from a missing or supplied field and remains subject to patient and clinician review.
