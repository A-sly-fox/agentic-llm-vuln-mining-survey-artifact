#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'

def read_csv(name):
    path = DATA / name
    if not path.exists():
        print(f'ERROR: missing {name}')
        return []
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def expand_a_level(value):
    if not value or value == 'NA':
        return []
    value = value.replace(' ', '')
    if '--' in value:
        left, right = value.split('--', 1)
        try:
            start = int(left[1:]); end = int(right[1:])
            return [f'A{i}' for i in range(start, end + 1)]
        except Exception:
            return [value]
    if '-' in value and value.count('A') >= 2:
        left, right = value.split('-', 1)
        try:
            start = int(left[1:]); end = int(right[1:])
            return [f'A{i}' for i in range(start, end + 1)]
        except Exception:
            return [value]
    return [value]

def status(kind, ok, msg):
    print(f'{kind if not ok else "PASS"}: {msg}')

corpus = read_csv('corpus.csv')
core = read_csv('core_coding.csv')
summary = read_csv('screening_summary.csv')
ref = read_csv('reference_audit.csv')
record_classification = read_csv('record_classification_audit.csv')

expected_layers = {'Core': 31, 'Supporting': 66, 'Background': 95, 'Excluded': 20}
if corpus:
    status('ERROR', len(corpus) == 212, f'candidate records = {len(corpus)}; expected 212')
    layer_counts = Counter(r.get('corpus_layer', 'NA') for r in corpus)
    for layer, expected in expected_layers.items():
        status('ERROR', layer_counts.get(layer, 0) == expected, f'{layer} = {layer_counts.get(layer, 0)}; expected {expected}')

if core:
    status('ERROR', len(core) == 31, f'Core rows = {len(core)}; expected 31')
    core_ids = [r.get('core_id', '') for r in core]
    record_ids = [r.get('record_id', '') for r in core]
    status('ERROR', len(core_ids) == len(set(core_ids)), 'core_id values are unique')
    status('ERROR', len(record_ids) == len(set(record_ids)), 'record_id values are unique in core_coding.csv')
    for required_core in ['C28', 'C29', 'C30', 'C31']:
        status('ERROR', required_core in core_ids, f'{required_core} exists in core_coding.csv')
    missing_reason = [r.get('core_id','?') for r in core if r.get('a_level_reason','NA') in ('', 'NA') or r.get('e_level_reason','NA') in ('', 'NA')]
    if missing_reason:
        print('WARNING: missing A/E reason fields for:', ', '.join(missing_reason))
    else:
        print('PASS: all Core rows include A/E reason fields')

    a_counts = Counter()
    for r in core:
        for a in expand_a_level(r.get('a_level','')):
            a_counts[a] += 1
    print('A-level occurrence counts:', dict(sorted(a_counts.items())))

    e_counts = Counter(r.get('e_level','NA') for r in core)
    expected_e = {'E0':3, 'E1':5, 'E2':8, 'E3':14, 'N/A':1}
    for e, expected in expected_e.items():
        status('ERROR', e_counts.get(e, 0) == expected, f'{e} = {e_counts.get(e, 0)}; expected {expected}')
    e4c_count = sum(1 for r in core if 'E4c' in (r.get('external_evidence_profile', '') or ''))
    status('ERROR', e4c_count == 0, f'E4c external profile = {e4c_count}; expected 0')

if summary:
    stage_counts = {r.get('stage'): r.get('count') for r in summary}
    print('screening_summary.csv stages:', stage_counts)

if ref:
    missing_url = sum(1 for r in ref if r.get('official_url','NA') in ('', 'NA'))
    missing_doi = sum(1 for r in ref if r.get('doi','NA') in ('', 'NA'))
    missing_verified = sum(1 for r in ref if r.get('last_verified_date','NA') in ('', 'NA'))
    print(f'WARNING: reference_audit missing official_url in {missing_url} rows')
    print(f'WARNING: reference_audit missing doi in {missing_doi} rows')
    print(f'WARNING: reference_audit missing last_verified_date in {missing_verified} rows')

if record_classification:
    expected_records = {
        'FuzzingBrain V2': 'Core',
        'DrillAgent': 'Core',
        'AIxCC SoK': 'Background',
        'OSS-CRS': 'Core',
        'GONDAR': 'Core',
        'COTTONTAIL': 'Supporting',
        'Wan et al.': 'Background',
    }
    status('ERROR', len(record_classification) == 7, f'record_classification_audit rows = {len(record_classification)}; expected 7')
    actual = {r.get('record', ''): r.get('classification', '') for r in record_classification}
    for record, expected in expected_records.items():
        status('ERROR', actual.get(record) == expected, f'{record} classification = {actual.get(record, "MISSING")}; expected {expected}')

print('DONE')
