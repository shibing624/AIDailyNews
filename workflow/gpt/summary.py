import json
import os

from openai import OpenAI
from loguru import logger

from workflow.gpt.prompt import multi_content_prompt


def evaluate_article_with_gpt(articles):
    article_links = [article.link for article in articles]
    logger.info(f"start summary: {article_links}")

    prompt = multi_content_prompt

    gpt_input = ""
    max_input_tokens = int(os.getenv("GPT_MAX_INPUT_TOKENS", 8000))
    for idx, item in enumerate(articles):
        content = item.summary[:max_input_tokens]
        gpt_input += f"```link: {item.link}, content:{content}```.\n"

    ai_provider = os.environ.get("AI_PROVIDER")
    if ai_provider == "openai":
        response = request_openai(prompt=prompt, content=gpt_input)
    else:
        response = request_gemini(prompt=prompt, content=gpt_input)
    response_list = transform2json(response)
    # check format
    if not response_list:
        return []
    if not isinstance(response_list, list):
        # 有时单个内容未按数组格式输出
        response_list = [response_list]

    evaluate_list = [item for item in response_list if item.get("title") and item.get("link")]
    return evaluate_list


def request_gemini(prompt, content):
    import google.generativeai as genai
    input_text = f"{prompt}: {content}"

    api_key = os.environ.get("GPT_API_KEY")
    if not api_key:
        raise ValueError("gemini key is empty")

    genai.configure(api_key=api_key)
    # Set up the model
    generation_config = genai.GenerationConfig(temperature=0.2)

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    model = genai.GenerativeModel(model_name='gemini-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    try:
        response = model.generate_content([input_text])
        logger.info(response.text)
        return response.text
    except Exception as e:
        logger.error(f"request gemini failed: {e}, skip")
        return None


def request_openai(prompt, content):
    try:
        api_key = os.getenv("GPT_API_KEY")
        base_url = os.getenv("GPT_BASE_URL")
        model = os.getenv("GPT_MODEL_NAME", "gpt-4o-mini")
        # logger.debug(f"request openai: {api_key}, {base_url}")
        client = OpenAI(api_key=api_key, base_url=base_url)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            model=model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logger.error(f"request openai failed: {e}")
        return ""


def transform2json(result):
    if not result:
        return None
    format_json = None
    # 去掉首尾两行就是完整json内容
    text = result.removeprefix("```json")
    text = text.removesuffix("```")
    # 有时输出格式可能不完全符合json
    try:
        json_obj = json.loads(text)
        # 关键信息校验
        format_json = json_obj
    except Exception as e:
        logger.exception(f"{e}")
    finally:
        return format_json


if __name__ == '__main__':
    from workflow.article.rss import gen_article_from
    from dotenv import load_dotenv

    pwd_path = os.path.abspath(os.path.dirname(__file__))

    load_dotenv(dotenv_path=os.path.join(pwd_path, '../../.env'), override=True)
    g = os.getenv("GPT_BASE_URL")
    a = os.getenv("GPT_API_KEY")
    c = os.getenv("GPT_MODEL_NAME")
    logger.info(f"envs: {g}, {a}, {c}")

    rss_item = {
        "link": "https://github.com/groue/GRDB.swift",
        "title": "grdb.swift"
    }

    article = gen_article_from(rss_item=rss_item, rss_type="code")
    logger.info(f"article: {article.summary}, {article.title}")
    res = evaluate_article_with_gpt([article])
    print(res)
