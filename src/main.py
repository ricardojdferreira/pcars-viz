import requests as rq
import json
from crest_api import Crest
from elastic_api import Elastic

def main():
    crest_data = Crest()
    es = Elastic()
    doc_id = 1

    while True:
        info_to_upload = {}

        mTyreTemp = crest_data.getWheelsAndTyres()["mTyreTemp"]
        info_to_upload["wheelsAndTyres$mTyreTemp$FL"] = int(mTyreTemp[0])
        info_to_upload["wheelsAndTyres$mTyreTemp$FR"] = int(mTyreTemp[1])
        info_to_upload["wheelsAndTyres$mTyreTemp$RL"] = int(mTyreTemp[2])
        info_to_upload["wheelsAndTyres$mTyreTemp$RR"] = int(mTyreTemp[3])

        es.create(
            index="pcars2", 
            id=doc_id,
            body=json.dumps(info_to_upload)
            )

        doc_id += 1

if __name__ == "__main__":
    main()