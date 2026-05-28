import numpy as np
import pandas as pd

diseases = {

    "d001": {
        "name": "cold",
        "weight": 0.85,
        "symptoms": {
            "s001": 0.7,  # cough
            "s006": 0.8,  # sore throat
            "s038": 0.7,  # sneezing
            "s015": 0.4,  # muscle aches
            "s007": 0.9   # runny nose
        }
    },
    "d002": {
        "name": "flu",
        "weight": 0.65,
        "symptoms": {
            "s002": 0.9,  # fever
            "s004": 0.8,  # fatigue
            "s015": 0.8,  # muscle aches
            "s017": 0.7,  # chills
            "s003": 0.6   # headache
        }
    },
    "d003": {
        "name": "COVID-19",
        "weight": 0.55,
        "symptoms": {
            "s001": 0.7,  # cough
            "s002": 0.7,  # fever
            "s004": 0.8,  # fatigue
            "s039": 0.95, # loss of smell
            "s040": 0.95, # loss of taste
            "s005": 0.8,  # shortness of breath
            "s003": 0.5,  # headache
            "s017": 0.6   # chills
        }
    },
    "d004": {
        "name": "pneumonia",
        "weight": 0.15,
        "symptoms": {
            "s001": 0.9,  # cough
            "s002": 0.85, # fever
            "s005": 0.9,  # shortness of breath
            "s004": 0.7,  # fatigue
            "s017": 0.6,  # chills
            "s011": 0.8,  # chest pain
            "s018": 0.5   # sweating
        }
    },
    "d005": {
        "name": "bronchitis",
        "weight": 0.45,
        "symptoms": {
            "s001": 0.95, # cough
            "s004": 0.6,  # fatigue
            "s005": 0.7,  # shortness of breath
            "s003": 0.4,  # headache
            "s015": 0.4   # muscle aches
        }
    },
    "d006": {
        "name": "asthma",
        "weight": 0.35,
        "symptoms": {
            "s005": 0.95, # shortness of breath
            "s001": 0.85, # cough
            "s011": 0.7,  # chest pain
            "s004": 0.5   # fatigue
        }
    },

    "d007": {
        "name": "gastroenteritis",
        "weight": 0.6,
        "symptoms": {
            "s008": 0.85, # nausea
            "s009": 0.85, # vomiting
            "s010": 0.9,  # diarrhea
            "s012": 0.8,  # abdominal pain
            "s002": 0.6,  # fever
            "s004": 0.5   # fatigue
        }
    },
    "d008": {
        "name": "food poisoning",
        "weight": 0.55,
        "symptoms": {
            "s008": 0.9,  # nausea
            "s009": 0.9,  # vomiting
            "s010": 0.85, # diarrhea
            "s012": 0.8,  # abdominal pain
            "s017": 0.5,  # chills
            "s002": 0.6   # fever
        }
    },
    "d009": {
        "name": "appendicitis",
        "weight": 0.08,
        "symptoms": {
            "s012": 0.95, # abdominal pain
            "s008": 0.7,  # nausea
            "s002": 0.7,  # fever
            "s019": 0.6,  # loss of appetite
            "s004": 0.4   # fatigue
        }
    },
    "d010": {
        "name": "irritable bowel syndrome",
        "weight": 0.4,
        "symptoms": {
            "s012": 0.9,  # abdominal pain
            "s022": 0.85, # bloating
            "s023": 0.7,  # constipation
            "s010": 0.7,  # diarrhea
            "s024": 0.5   # heartburn
        }
    },
    "d011": {
        "name": "gastroesophageal reflux disease",
        "weight": 0.5,
        "symptoms": {
            "s024": 0.95, # heartburn
            "s025": 0.85, # indigestion
            "s041": 0.6,  # difficulty swallowing
            "s001": 0.5,  # cough
            "s042": 0.4   # hoarseness
        }
    },
    "d012": {
        "name": "peptic ulcer",
        "weight": 0.25,
        "symptoms": {
            "s012": 0.9,  # abdominal pain
            "s024": 0.8,  # heartburn
            "s008": 0.7,  # nausea
            "s019": 0.6,  # loss of appetite
            "s020": 0.5   # weight loss
        }
    },
    "d013": {
        "name": "gallstones",
        "weight": 0.2,
        "symptoms": {
            "s012": 0.95, # abdominal pain
            "s008": 0.8,  # nausea
            "s024": 0.6,  # heartburn
            "s019": 0.5,  # loss of appetite
            "s002": 0.4   # fever
        }
    },

    "d014": {
        "name": "hypertension",
        "weight": 0.55,
        "symptoms": {
            "s003": 0.8,  # headache
            "s016": 0.6,  # dizziness
            "s031": 0.7,  # blurred vision
            "s004": 0.8,  # fatigue
            "s011": 0.7   # chest pain
        }
    },
    "d015": {
        "name": "heart attack",
        "weight": 0.03,
        "symptoms": {
            "s011": 0.99, # chest pain
            "s005": 0.85, # shortness of breath
            "s008": 0.6,  # nausea
            "s046": 0.75, # shoulder pain
            "s016": 0.6,  # dizziness
            "s018": 0.5   # sweating
        }
    },
    "d016": {
        "name": "heart failure",
        "weight": 0.08,
        "symptoms": {
            "s005": 0.95, # shortness of breath
            "s004": 0.8,  # fatigue
            "s028": 0.9,  # swelling
            "s011": 0.7,  # chest pain
            "s016": 0.5   # dizziness
        }
    },
    "d017": {
        "name": "angina",
        "weight": 0.2,
        "symptoms": {
            "s011": 0.95, # chest pain
            "s005": 0.8,  # shortness of breath
            "s004": 0.5,  # fatigue
            "s046": 0.6,  # shoulder pain
            "s016": 0.4   # dizziness
        }
    },
    "d018": {
        "name": "pulmonary embolism",
        "weight": 0.02,
        "symptoms": {
            "s005": 0.95, # shortness of breath
            "s011": 0.85, # chest pain
            "s016": 0.7,  # dizziness
            "s002": 0.5,  # fever
            "s001": 0.6   # cough
        }
    },

    "d019": {
        "name": "migraine",
        "weight": 0.5,
        "symptoms": {
            "s003": 0.99, # headache
            "s008": 0.8,  # nausea
            "s031": 0.75, # blurred vision
            "s016": 0.6,  # dizziness
            "s050": 0.4   # numbness
        }
    },
    "d020": {
        "name": "tension headache",
        "weight": 0.6,
        "symptoms": {
            "s003": 0.95, # headache
            "s045": 0.8,  # neck pain
            "s046": 0.6,  # shoulder pain
            "s004": 0.4   # fatigue
        }
    },
    "d021": {
        "name": "meningitis",
        "weight": 0.01,
        "symptoms": {
            "s003": 0.9,  # headache
            "s002": 0.9,  # fever
            "s045": 0.95, # neck pain
            "s017": 0.7,  # chills
            "s008": 0.6,  # nausea
            "s053": 0.8   # seizures
        }
    },
    "d022": {
        "name": "stroke",
        "weight": 0.03,
        "symptoms": {
            "s003": 0.7,  # headache
            "s016": 0.8,  # dizziness
            "s055": 0.9,  # confusion
            "s050": 0.9,  # numbness
            "s031": 0.8,  # blurred vision
            "s052": 0.7   # tremors
        }
    },
    "d023": {
        "name": "vertigo",
        "weight": 0.30,
        "symptoms": {
            "s016": 0.99, # dizziness
            "s008": 0.7,  # nausea
            "s034": 0.5,  # ear pain
            "s036": 0.6   # ringing in ears
        }
    },
    "d024": {
        "name": "epilepsy",
        "weight": 0.08,
        "symptoms": {
            "s053": 0.99, # seizures
            "s055": 0.7,  # confusion
            "s054": 0.6,  # memory loss
            "s004": 0.4   # fatigue
        }
    },

    "d025": {
        "name": "rheumatoid arthritis",
        "weight": 0.2,
        "symptoms": {
            "s014": 0.95, # joint pain
            "s028": 0.85, # swelling
            "s015": 0.7,  # muscle aches
            "s004": 0.7,  # fatigue
            "s002": 0.5   # fever
        }
    },
    "d026": {
        "name": "osteoarthritis",
        "weight": 0.45,
        "symptoms": {
            "s014": 0.95, # joint pain
            "s047": 0.85, # knee pain
            "s046": 0.7,  # shoulder pain
            "s013": 0.6,  # back pain
            "s028": 0.5   # swelling
        }
    },
    "d027": {
        "name": "gout",
        "weight": 0.15,
        "symptoms": {
            "s014": 0.95, # joint pain
            "s028": 0.9,  # swelling
            "s026": 0.7,  # itching
            "s002": 0.5,  # fever
            "s047": 0.8   # knee pain
        }
    },
    "d028": {
        "name": "fibromyalgia",
        "weight": 0.25,
        "symptoms": {
            "s015": 0.95, # muscle aches
            "s004": 0.9,  # fatigue
            "s003": 0.7,  # headache
            "s058": 0.8,  # insomnia
            "s050": 0.6,  # numbness
            "s056": 0.5   # anxiety
        }
    },
    "d029": {
        "name": "sciatica",
        "weight": 0.3,
        "symptoms": {
            "s013": 0.95, # back pain
            "s050": 0.9,  # numbness
            "s051": 0.85, # tingling
            "s049": 0.8,  # foot pain
            "s047": 0.6   # knee pain
        }
    },

    "d030": {
        "name": "malaria",
        "weight": 0.05,
        "symptoms": {
            "s002": 0.95, # fever
            "s017": 0.9,  # chills
            "s018": 0.8,  # sweating
            "s003": 0.7,  # headache
            "s015": 0.6,  # muscle aches
            "s004": 0.7   # fatigue
        }
    },
    "d031": {
        "name": "dengue fever",
        "weight": 0.005,
        "symptoms": {
            "s002": 0.9,  # fever
            "s003": 0.85, # headache
            "s014": 0.8,  # joint pain
            "s015": 0.8,  # muscle aches
            "s027": 0.7,  # rash
            "s004": 0.6   # fatigue
        }
    },
    "d032": {
        "name": "urinary tract infection",
        "weight": 0.55,
        "symptoms": {
            "s059": 0.9,  # frequent urination
            "s060": 0.95, # painful urination
            "s012": 0.6,  # abdominal pain
            "s002": 0.5,  # fever
            "s004": 0.4   # fatigue
        }
    },
    "d033": {
        "name": "sepsis",
        "weight": 0.01,
        "symptoms": {
            "s002": 0.95, # fever
            "s017": 0.85, # chills
            "s016": 0.8,  # dizziness
            "s005": 0.85, # shortness of breath
            "s055": 0.8,  # confusion
            "s028": 0.6   # swelling
        }
    },
    "d034": {
        "name": "chickenpox",
        "weight": 0.2,
        "symptoms": {
            "s027": 0.99, # rash
            "s026": 0.9,  # itching
            "s002": 0.7,  # fever
            "s004": 0.6,  # fatigue
            "s017": 0.5   # chills
        }
    },

    "d035": {
        "name": "depression",
        "weight": 0.6,
        "symptoms": {
            "s057": 0.99, # depression
            "s058": 0.8,  # insomnia
            "s004": 0.8,  # fatigue
            "s019": 0.7,  # loss of appetite
            "s003": 0.5,  # headache
            "s054": 0.5   # memory loss
        }
    },
    "d036": {
        "name": "anxiety disorder",
        "weight": 0.65,
        "symptoms": {
            "s056": 0.99, # anxiety
            "s058": 0.8,  # insomnia
            "s004": 0.7,  # fatigue
            "s003": 0.6,  # headache
            "s016": 0.5,  # dizziness
            "s011": 0.5   # chest pain
        }
    },
    "d037": {
        "name": "panic disorder",
        "weight": 0.35,
        "symptoms": {
            "s056": 0.9,  # anxiety
            "s011": 0.9,  # chest pain
            "s005": 0.85, # shortness of breath
            "s018": 0.7,  # sweating
            "s016": 0.7,  # dizziness
            "s051": 0.5   # tingling
        }
    },

    "d038": {
        "name": "type 2 diabetes",
        "weight": 0.45,
        "symptoms": {
            "s059": 0.9,  # frequent urination
            "s004": 0.7,  # fatigue
            "s020": 0.6,  # weight loss
            "s031": 0.6,  # blurred vision
            "s050": 0.7,  # numbness
            "s026": 0.5   # itching
        }
    },
    "d039": {
        "name": "hypothyroidism",
        "weight": 0.3,
        "symptoms": {
            "s021": 0.85, # weight gain
            "s004": 0.8,  # fatigue
            "s023": 0.6,  # constipation
            "s058": 0.7,  # insomnia
            "s016": 0.5,  # dizziness
            "s014": 0.5   # joint pain
        }
    },
    "d040": {
        "name": "hyperthyroidism",
        "weight": 0.2,
        "symptoms": {
            "s020": 0.85, # weight loss
            "s018": 0.8,  # sweating
            "s058": 0.7,  # insomnia
            "s056": 0.7,  # anxiety
            "s004": 0.5,  # fatigue
            "s052": 0.6   # tremors
        }
    },
    "d041": {
        "name": "anemia",
        "weight": 0.4,
        "symptoms": {
            "s004": 0.9,  # fatigue
            "s016": 0.8,  # dizziness
            "s005": 0.7,  # shortness of breath
            "s003": 0.5,  # headache
            "s050": 0.5,  # numbness
            "s015": 0.4   # muscle aches
        }
    },

    "d042": {
        "name": "sinusitis",
        "weight": 0.5,
        "symptoms": {
            "s037": 0.9,  # nasal congestion
            "s003": 0.85, # headache
            "s034": 0.7,  # ear pain
            "s042": 0.5,  # hoarseness
            "s019": 0.3   # loss of appetite
        }
    },
    "d043": {
        "name": "otitis media",
        "weight": 0.25,
        "symptoms": {
            "s034": 0.99, # ear pain
            "s002": 0.7,  # fever
            "s035": 0.6,  # hearing loss
            "s003": 0.5,  # headache
            "s004": 0.4   # fatigue
        }
    },
    "d044": {
        "name": "conjunctivitis",
        "weight": 0.3,
        "symptoms": {
            "s033": 0.95, # eye pain
            "s026": 0.8,  # itching
            "s028": 0.6,  # swelling
            "s031": 0.5   # blurred vision
        }
    },
    "d045": {
        "name": "tonsillitis",
        "weight": 0.45,
        "symptoms": {
            "s006": 0.9,  # sore throat
            "s041": 0.85, # difficulty swallowing
            "s002": 0.8,  # fever
            "s003": 0.5,  # headache
            "s042": 0.6   # hoarseness
        }
    },
        "d046": {
        "name": "kidney stones",
        "weight": 0.18,
        "symptoms": {
            "s012": 0.95,  # abdominal pain
            "s060": 0.85,  # painful urination
            "s008": 0.7,   # nausea
            "s009": 0.6,   # vomiting
            "s002": 0.5,   # fever
            "s059": 0.6    # frequent urination
        }
    },
    "d047": {
        "name": "chronic kidney disease",
        "weight": 0.1,
        "symptoms": {
            "s004": 0.85,  # fatigue
            "s028": 0.8,   # swelling
            "s005": 0.7,   # shortness of breath
            "s059": 0.75,  # frequent urination
            "s008": 0.6,   # nausea
            "s016": 0.5    # dizziness
        }
    },
    "d048": {
        "name": "glomerulonephritis",
        "weight": 0.05,
        "symptoms": {
            "s028": 0.9,   # swelling
            "s002": 0.7,   # fever
            "s004": 0.7,   # fatigue
            "s005": 0.6,   # shortness of breath
            "s003": 0.5    # headache
        }
    },    "d049": {
        "name": "hepatitis b",
        "weight": 0.03,
        "symptoms": {
            "s004": 0.85,  # fatigue
            "s008": 0.8,   # nausea
            "s012": 0.75,  # abdominal pain
            "s019": 0.7,   # loss of appetite
            "s002": 0.65,  # fever
            "s020": 0.5    # weight loss
        }
    },
    "d050": {
        "name": "hepatitis c",
        "weight": 0.03,
        "symptoms": {
            "s004": 0.9,   # fatigue
            "s014": 0.7,   # joint pain
            "s008": 0.7,   # nausea
            "s019": 0.65,  # loss of appetite
            "s020": 0.55,  # weight loss
            "s003": 0.5    # headache
        }
    },
    "d051": {
        "name": "cirrhosis",
        "weight": 0.05,
        "symptoms": {
            "s028": 0.9,   # swelling
            "s004": 0.85,  # fatigue
            "s019": 0.75,  # loss of appetite
            "s020": 0.7,   # weight loss
            "s008": 0.65,  # nausea
            "s016": 0.5    # dizziness
        }
    },
    "d052": {
        "name": "fatty liver disease",
        "weight": 0.25,
        "symptoms": {
            "s004": 0.8,   # fatigue
            "s012": 0.7,   # abdominal pain
            "s008": 0.55,  # nausea
            "s019": 0.5,   # loss of appetite
            "s021": 0.6    # weight gain
        }
    },    "d053": {
        "name": "psoriasis",
        "weight": 0.3,
        "symptoms": {
            "s027": 0.95,  # rash
            "s026": 0.9,   # itching
            "s014": 0.6,   # joint pain
            "s028": 0.5    # swelling
        }
    },
    "d054": {
        "name": "eczema",
        "weight": 0.4,
        "symptoms": {
            "s026": 0.95,  # itching
            "s027": 0.9,   # rash
            "s028": 0.6,   # swelling
            "s004": 0.4    # fatigue
        }
    },
    "d055": {
        "name": "shingles",
        "weight": 0.15,
        "symptoms": {
            "s027": 0.95,  # rash
            "s026": 0.9,   # itching
            "s015": 0.8,   # muscle aches
            "s002": 0.6,   # fever
            "s004": 0.6    # fatigue
        }
    },
    "d056": {
        "name": "cellulitis",
        "weight": 0.2,
        "symptoms": {
            "s028": 0.95,  # swelling
            "s002": 0.8,   # fever
            "s004": 0.6,   # fatigue
            "s026": 0.5    # itching
        }
    },
    "d057": {
        "name": "hives",
        "weight": 0.3,
        "symptoms": {
            "s026": 0.99,  # itching
            "s027": 0.95,  # rash
            "s028": 0.7,   # swelling
            "s005": 0.4    # shortness of breath
        }
    },    "d058": {
        "name": "glaucoma",
        "weight": 0.15,
        "symptoms": {
            "s033": 0.85,  # eye pain
            "s031": 0.9,   # blurred vision
            "s003": 0.6,   # headache
            "s008": 0.5    # nausea
        }
    },
    "d059": {
        "name": "cataracts",
        "weight": 0.35,
        "symptoms": {
            "s031": 0.95,  # blurred vision
            "s032": 0.8,   # double vision
            "s033": 0.5    # eye pain
        }
    },
    "d060": {
        "name": "macular degeneration",
        "weight": 0.2,
        "symptoms": {
            "s031": 0.95,  # blurred vision
            "s032": 0.7,   # double vision
            "s033": 0.4    # eye pain
        }
    },
    "d061": {
        "name": "labyrinthitis",
        "weight": 0.15,
        "symptoms": {
            "s016": 0.95,  # dizziness
            "s036": 0.85,  # ringing in ears
            "s035": 0.7,   # hearing loss
            "s008": 0.65,  # nausea
            "s034": 0.6    # ear pain
        }
    },
    "d062": {
        "name": "meniere's disease",
        "weight": 0.12,
        "symptoms": {
            "s016": 0.99,  # dizziness
            "s036": 0.9,   # ringing in ears
            "s035": 0.85,  # hearing loss
            "s008": 0.7,   # nausea
            "s034": 0.5    # ear pain
        }
    }
}


PRIORS = {
# very common
"d001": 1.03,  # cold
"d002": 1.02,  # flu
"d003": 1.01,  # COVID
"d005": 1.02,  # bronchitis
"d006": 1.01,  # asthma
"d007": 1.02,  # gastroenteritis
"d008": 1.02,  # food poisoning
"d010": 1.01,  # IBS
"d011": 1.01,  # GERD
"d014": 1.02,  # hypertension
"d019": 1.02,  # migraine
"d020": 1.03,  # tension headache
"d023": 1.01,  # vertigo
"d026": 1.02,  # osteoarthritis
"d032": 1.02,  # UTI
"d035": 1.02,  # depression
"d036": 1.02,  # anxiety
"d038": 1.02,  # type2 diabetes
"d041": 1.01,  # anemia
"d042": 1.02,  # sinusitis
"d045": 1.02,  # tonsillitis
"d054": 1.02,  # eczema
"d057": 1.02,  # hives

# common but not everyday
"d004": 0.99,  # pneumonia
"d012": 0.99,  # ulcer
"d013": 0.99,  # gallstones
"d016": 0.99,  # heart failure
"d017": 1.00,  # angina
"d025": 0.99,  # rheumatoid arthritis
"d027": 0.99,  # gout
"d028": 1.00,  # fibromyalgia
"d029": 1.00,  # sciatica
"d034": 1.00,  # chickenpox
"d039": 0.99,  # hypothyroid
"d040": 0.99,  # hyperthyroid
"d043": 0.99,  # otitis media
"d044": 1.00,  # conjunctivitis
"d046": 0.99,  # kidney stones
"d047": 0.98,  # chronic kidney disease
"d052": 1.01,  # fatty liver
"d053": 1.00,  # psoriasis
"d055": 0.99,  # shingles
"d056": 0.99,  # cellulitis
"d058": 0.98,  # glaucoma
"d059": 1.00,  # cataracts
"d060": 0.99,  # macular degeneration
"d061": 0.99,  # labyrinthitis
"d062": 0.99,  # meniere

# rare / emergency / dangerous
"d009": 0.98,  # appendicitis
"d015": 0.98,  # heart attack
"d018": 0.97,  # pulmonary embolism
"d021": 0.97,  # meningitis
"d022": 0.97,  # stroke
"d024": 0.98,  # epilepsy
"d030": 0.97,  # malaria
"d031": 0.97,  # dengue
"d033": 0.97,  # sepsis
"d037": 0.99,  # panic disorder
"d048": 0.98,  # glomerulonephritis
"d049": 0.98,  # hepatitis B
"d050": 0.98,  # hepatitis C
"d051": 0.98,  # cirrhosis
}

for disease_id, disease in diseases.items():
    disease["weight"] = PRIORS[disease_id]


symptoms = {
"s001": {"name": "cough"},
"s002": {"name": "fever"},
"s003": {"name": "headache"},
"s004": {"name": "fatigue"},
"s005": {"name": "shortness of breath"},
"s006": {"name": "sore throat"},
"s007": {"name": "runny nose"},
"s008": {"name": "nausea"},
"s009": {"name": "vomiting"},
"s010": {"name": "diarrhea"},
"s011": {"name": "chest pain"},
"s012": {"name": "abdominal pain"},
"s013": {"name": "back pain"},
"s014": {"name": "joint pain"},
"s015": {"name": "muscle aches"},
"s016": {"name": "dizziness"},
"s017": {"name": "chills"},
"s018": {"name": "sweating"},
"s019": {"name": "loss of appetite"},
"s020": {"name": "weight loss"},
"s021": {"name": "weight gain"},
"s022": {"name": "bloating"},
"s023": {"name": "constipation"},
"s024": {"name": "heartburn"},
"s025": {"name": "indigestion"},
"s026": {"name": "itching"},
"s027": {"name": "rash"},
"s028": {"name": "swelling"},
"s029": {"name": "bruising"},
"s030": {"name": "bleeding"},
"s031": {"name": "blurred vision"},
"s032": {"name": "double vision"},
"s033": {"name": "eye pain"},
"s034": {"name": "ear pain"},
"s035": {"name": "hearing loss"},
"s036": {"name": "ringing in ears"},
"s037": {"name": "nasal congestion"},
"s038": {"name": "sneezing"},
"s039": {"name": "loss of smell"},
"s040": {"name": "loss of taste"},
"s041": {"name": "difficulty swallowing"},
"s042": {"name": "hoarseness"},
"s043": {"name": "mouth sores"},
"s044": {"name": "toothache"},
"s045": {"name": "neck pain"},
"s046": {"name": "shoulder pain"},
"s047": {"name": "knee pain"},
"s048": {"name": "ankle pain"},
"s049": {"name": "foot pain"},
"s050": {"name": "numbness"},
"s051": {"name": "tingling"},
"s052": {"name": "tremors"},
"s053": {"name": "seizures"},
"s054": {"name": "memory loss"},
"s055": {"name": "confusion"},
"s056": {"name": "anxiety"},
"s057": {"name": "depression"},
"s058": {"name": "insomnia"},
"s059": {"name": "frequent urination"},
"s060": {"name": "painful urination"}
}


profile_adjustments = {
        "heart attack":        {"male": 1.5, "female": 0.7,
                            "very elderly": 1.8, "elderly": 1.6,
                            "late seniors": 1.4, "early seniors": 1.2,
                            "older adults": 1.1},

        "hypertension":        {"male": 1.2, "very elderly": 1.7,
                            "elderly": 1.5, "late seniors": 1.3,
                            "mid-seniors": 1.2},

        "heart failure":       {"very elderly": 1.8, "elderly": 1.6,
                            "late seniors": 1.3, "male": 1.2},

        "angina":              {"male": 1.4, "female": 0.8,
                            "elderly": 1.5, "late seniors": 1.3,
                            "older adults": 1.1},

        "stroke":              {"very elderly": 1.9, "elderly": 1.6,
                            "late seniors": 1.3, "male": 1.2},

        "asthma":              {"children": 1.6, "youth": 1.4, "female": 1.2},

        "pneumonia":           {"very elderly": 1.7, "elderly": 1.5,
                            "newborn": 1.6, "toddler": 1.4},

        "pulmonary embolism":  {"female": 1.3, "elderly": 1.4, "very elderly": 1.6},

        "migraine":            {"female": 1.7, "male": 0.6,
                            "young adults": 1.3, "mid-adults": 1.2},

        "epilepsy":            {"children": 1.5, "youth": 1.3, "very elderly": 1.4},

        "meningitis":          {"newborn": 1.9, "toddler": 1.6,
                            "children": 1.4, "youth": 1.3},

        "alzheimer's":         {"very elderly": 2.0, "elderly": 1.7, "female": 1.3},

        "osteoarthritis":      {"very elderly": 1.8, "elderly": 1.6,
                            "late seniors": 1.3, "female": 1.2},

        "rheumatoid arthritis":{"female": 1.8, "male": 0.5,
                            "mid-adults": 1.2, "older adults": 1.3},

        "gout":                {"male": 2.0, "female": 0.4,
                            "elderly": 1.4, "late seniors": 1.2},

        "osteoporosis":        {"female": 2.0, "male": 0.3,
                            "very elderly": 1.9, "elderly": 1.6},

        "type 2 diabetes":     {"very elderly": 1.5, "elderly": 1.4,
                                "mid-seniors": 1.3, "older adults": 1.2},

        "hypothyroidism":      {"female": 1.8, "male": 0.4, "elderly": 1.4},

        "hyperthyroidism":     {"female": 1.6, "male": 0.5, "young adults": 1.3},

        "depression":          {"female": 1.5, "male": 0.7,
                            "young adults": 1.3, "mid-adults": 1.2},

        "anxiety disorder":    {"female": 1.4, "young adults": 1.4, "youth": 1.5},

        "panic disorder":      {"female": 1.6, "young adults": 1.5, "mid-adults": 1.2},

        "malaria":             {"children": 1.8, "toddler": 1.9, "newborn": 2.0},

        "dengue fever":        {"children": 1.5, "youth": 1.3},

        "chickenpox":          {"children": 2.0, "toddler": 1.8,
                            "youth": 1.4, "very elderly": 1.5},

        "sepsis":              {"newborn": 1.9, "toddler": 1.6,
                            "very elderly": 1.8, "elderly": 1.5},

        "urinary tract infection": {"female": 1.9, "male": 0.4, "very elderly": 1.4},

        "kidney stones":           {"male": 1.5, "female": 0.7,
                                "older adults": 1.3, "mid-seniors": 1.2},

        }



def categorize_age(patient_age: int) -> str:
    if 90 <= patient_age<= 99:
        return "very elderly"
    elif 80 <= patient_age <= 89:
        return "elderly"
    elif 70 <= patient_age <= 79:
        return "late seniors"
    elif 60 <= patient_age <= 69:
        return "mid-seniors"
    elif 50 <= patient_age <= 59:
        return "early seniors"
    elif 40 <= patient_age <= 49:
        return "older adults"
    elif 30 <= patient_age <= 39:
        return "mid-adults"
    elif 20 <= patient_age <= 29:
        return "young adults"
    elif 15 <= patient_age <= 19:
        return "youth"
    elif 10 <= patient_age <= 14:
        return "children"
    elif 5 <= patient_age <= 9:
        return "toddler"
    else:
        return "newborn"
    


def run_diagnosis_engine(patient_age:int, patient_gender:str, patient_symptoms:list):

    if not patient_symptoms:
        return {"status": "error", "message": "No valid symptoms found", "ranking": None}

    if len(patient_symptoms) <= 2:
        return {"status": "error", "message": "please enter three or more symptoms for accurate diagnosis", "ranking": None}

    age_group = categorize_age(patient_age)

    result = {}

    for disease_id, disease_data in diseases.items():
        disease_name = disease_data["name"]
        prior = disease_data["weight"]

        # profile adjustments
        if disease_name in profile_adjustments:
            adjustments = profile_adjustments[disease_name]

            if patient_gender in adjustments:
                prior *= adjustments[patient_gender]

            if age_group in adjustments:
                prior *= adjustments[age_group]

        disease_symptoms = disease_data["symptoms"]

        likelihood = 0
        for symptom, probability in disease_symptoms.items():
            if symptom in patient_symptoms:
                likelihood += np.log(probability)
            else:
                likelihood += np.log(1 - probability)

        likelihood /= len(disease_symptoms)
        posterior = np.log(prior) + likelihood

        result[disease_name] = posterior

    scores = list(result.values()) 
    names = list(result.keys())
    scores = sorted(scores, key=lambda x: x, reverse=True)[:3]
    array = np.array(scores)
    probs = np.exp(array - np.max(scores))
    probs = probs / probs.sum()
    ranking = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)[:3]
    return {"status": "ok", "message": "success", "ranking": ranking}