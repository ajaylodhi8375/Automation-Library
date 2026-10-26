import openpyxl, json, datetime, sys
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src, data_only=True)
sheets = []
for ws in wb.worksheets:
    if ws.sheet_state != 'visible': continue
    rows = []
    for r in ws.iter_rows(values_only=True):
        cells = []
        for c in r:
            if isinstance(c, (datetime.datetime, datetime.date)): c = c.strftime('%Y-%m-%d')
            elif isinstance(c, float) and c.is_integer(): c = int(c)
            elif isinstance(c, str): c = c.replace('\r', '').replace('’', "'")
            if isinstance(c, str) and not c.strip(): c = None
            cells.append(c)
        while cells and cells[-1] is None: cells.pop()
        if cells: rows.append(cells)
    sheets.append({'name': ws.title.strip(), 'rows': rows})
json.dump({'file': src.split('_',1)[-1] if '_' in src.split('/')[-1] else src.split('/')[-1], 'sheets': sheets}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print([(s['name'], len(s['rows'])) for s in sheets])
