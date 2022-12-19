fhir_imaging_study_template = {
  "resourceType": "ImagingStudy",
  "id": "example",
  "status": "available",
  "subject": {
    "reference": "Patient/dicom"
  },
  "started": "2011-01-01T11:01:20+03:00",
  "numberOfSeries": 1,
  "numberOfInstances": 1,
  "series": [
    {
      "uid": "2.16.124.113543.6003.2588828330.45298.17418.2723805630",
      "number": 3,
      "modality": {
        "system": "http://dicom.nema.org/resources/ontology/DCM",
        "code": "CT"
      },
      "description": "CT Surview 180",
      "numberOfInstances": 1,
      "bodySite": {
        "system": "http://snomed.info/sct",
        "code": "67734004",
        "display": "Upper Trunk Structure"
      },
      "instance": [
        {
          "uid": "2.16.124.113543.6003.189642796.63084.16748.2599092903",
          "sopClass": {
            "system": "urn:ietf:rfc:3986",
            "code": "urn:oid:1.2.840.10008.5.1.4.1.1.2"
          },
          "number": 1
        }
      ]
    }
  ]
}

fhir_media_template = {
  "resourceType": "Media",
  "id": "example",
  "status": "completed",
  "type": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/media-type",
        "code": "image",
        "display": "Image"
      }
    ]
  },
  "content": {
    "id": "a1",
    "contentType": "image/dicom",
    "data": "",
    "creation": "2009-09-03"
  }
}