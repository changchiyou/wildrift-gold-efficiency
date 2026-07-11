# translate-patch

Update i18n translation files with new item name and passive translations based on patch notes.

## Usage

```
/translate-patch [target languages]

[EN patch notes]
---
[Patch notes in each target language, separated by ---]
```

- **Base language**: `en-US` (always the reference)
- **Default target**: `zh-TW` (if no languages specified)
- **Multiple targets**: `/translate-patch zh-TW ja-JP pt-BR`

Patch notes sections must be provided in the same order as the target languages listed.

### Examples

```
/translate-patch

[EN patch notes]
---
[ZH-TW patch notes]
```

```
/translate-patch zh-TW ja-JP

[EN patch notes]
---
[ZH-TW patch notes]
---
[JA-JP patch notes]
```

## Instructions

### Step 1 — Parse arguments

Read the arguments after `/translate-patch`:
- If no arguments: target = `[zh-TW]`
- If arguments provided: target = each space-separated language code (e.g., `zh-TW ja-JP`)

Map each target language to its file: `_data/i18n/{language}.yml`

Split the user-provided text by `---` to get one patch notes block per language:
- Block 0 = EN patch notes (base)
- Block 1 = first target language patch notes
- Block 2 = second target language patch notes
- etc.

### Step 2 — Identify missing keys

Read `_data/i18n/en-US.yml` to get all keys under `item.name` and `item.passive`.

For **each target language**:
- Read `_data/i18n/{language}.yml`
- Find all keys present in `en-US` but absent in the target file — these need translation

### Step 3 — Derive translations

For each target language, use its corresponding patch notes block as the primary source:
- Extract item names exactly as written in the localized patch notes (official names)
- Extract passive names if mentioned
- For passives not mentioned in patch notes, infer from context or follow the existing translation style in that language's yml file

Key naming rules (keys are always identical to en-US.yml):
- Item names: lowercase kebab-case (e.g., `bloodthirster`, `guardian-angel`)
- Passive variants: `{item-key}-{passive-key}` (e.g., `bloodthirster-bloody[crit]`)
- Passive keys: kebab-case (e.g., `bloody`, `last-whisper`, `bloody[crit]`)

### Step 4 — Update each target file

For each target language, append missing translations to `_data/i18n/{language}.yml`:
- New item names → under `item.name:`
- New passive names → under `item.passive:`
- Maintain alphabetical order within each section
- Do NOT modify any existing translations
- Do NOT add entries for keys that already exist in the target file

### Step 5 — Upload to Crowdin

After all target files are updated, run:

```bash
crowdin upload translations
```

This requires `crowdin.yml` in the project root and the following env vars set locally:
- `CROWDIN_PROJECT_ID`
- `CROWDIN_PERSONAL_TOKEN`

If the upload fails due to missing env vars, report the error and remind the user to set them.

### Step 6 — Report

For each target language, list:
- Each new `item.name` key added and its translation
- Each new `item.passive` key added and its translation
- Any keys still missing (patch notes didn't mention them — flag for manual review)
- Crowdin upload result (success / error)
