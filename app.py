"""Create a non-clinical appointment preparation checklist."""
import argparse, json
from pathlib import Path

CHECKS=(
    ("appointment_time","Confirm the appointment date and time."),
    ("location","Confirm the clinic address or video link."),
    ("questions","Write down questions to ask the clinician."),
    ("medications","Bring an up-to-date medication list."),
    ("allergies","Record known allergies or explicitly state none known."),
    ("documents","Prepare requested identification, referral, or prior reports."),
    ("transport_plan","Plan travel or technical setup for the appointment."),
)

def prepare(data:dict)->dict:
    items=[]
    for field,message in CHECKS:
        value=data.get(field)
        complete=bool(value) or (field=="allergies" and value==[])
        items.append({"field":field,"status":"ready" if complete else "missing","action":message,
                      "reason":f"{field.replace('_',' ')} was {'provided' if complete else 'not provided'}"})
    return {"appointment_type":data.get("appointment_type","unspecified"),"ready_count":sum(i["status"]=="ready" for i in items),
            "checklist":items,"disclaimer":"Organization only; not medical advice or urgency assessment."}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",nargs="?",default="sample_data.json")
    print(json.dumps(prepare(json.loads(Path(p.parse_args().input).read_text())),indent=2))
if __name__=="__main__":main()
