python3 -m virtualenv venv

python3 pip install prodigy -f {.....}

source venv/bin/activate

python3 pip install ngrok

ngrok config add-authoken {.....}

python3 -m prodigy metric.iaa.doc dataset:project3eval multiclass -l CapitalRequirements,ConsumerProtection,RiskManagement,ReportingAndCompliance,CorporateGovernance

PRODIGY_ALLOWED_SESSIONS=reviwer python3 -m prodigy review project3eval-review project3eval --auto-accept

prodigy db-out project3eval-review > goldenEval.jsonl

prodigy db-in prodigy3train train200.jsonl

iconv -f utf-16 -t utf-8 train200.jsonl > train200a.jsonl

prodigy db-in golden3 goldeneval.jsonl

python3 -m prodigy train --textcat-multilabel prodigy3train,eval:golden3 ./output/experiment1

python3 -m spacy download en_core_web_lg

python3 -m prodigy data-to-spacy --textcat-multilabel prodigy3train,eval:golden3 ./corpus --base-model en_core_web_lg

python -m spacy train corpus/config.cfg --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy

pip install jsonlines

python3 firstStep-format.py

python3 secondStep-score.py

python3 thirdStep-label.py

python3 finalStep-formatLabel.py

prodigy db-in prodigy3trainComplete project3_trainComplete.jsonl

python3 -m prodigy train --textcat-multilabel prodigy3trainComplete,eval:golden3 ./output/experiment3

python3 -m prodigy data-to-spacy --textcat-multilabel prodigy3trainComplete,eval:golden3 ./corpus --base-model en_core_web_lg

python -m spacy train corpus/config.cfg --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy
