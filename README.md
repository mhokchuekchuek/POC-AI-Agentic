# POC-AI-Agentic
this section for poc AI Agentic in 2 parts
- [Text to SQL](#text-to-sql)
- OCR Task

## Prerequisite
You need to install dependencies first

```
pip install -r req.txt
```

## Run Locally

### Text to SQL

if you need to use self-hosted, U can run this CMD.

```
vllm serve "deepseek-ai/deepseek-coder-1.3b-base" \
    --max-model-len 1024 \
    --chat-template chat_template\template_deepseek_vl2.jinja
```

> 📝 **Noted:** \
This config is for Mac M2. You can see more config params via [this link](https://docs.vllm.ai/en/latest/serving/engine_args.html).

#### Run Demo:

```
python generate_sql.py
```

### OCR

if you need to use self-hosted, U can run this CMD.

```
vllm serve "deepseek-ai/deepseek-coder-1.3b-base" \
    --max-model-len 1024 \
    --chat-template chat_template\template_deepseek_vl2.jinja
```

> 📝 **Noted:** \
This config is for Mac M2. You can see more config params via [this link](https://docs.vllm.ai/en/latest/serving/engine_args.html).

#### Run Demo:

```
python ocr.py
```
