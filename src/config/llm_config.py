"""
Centralized LLM configuration for the ANeuk AI project.

This module loads LLM configurations from llm_config.yaml and provides
factory functions to create LLM instances for different purposes.

All model configurations are defined in llm_config.yaml.
No environment variables are used for model selection.
"""

from pathlib import Path
from typing import List, Dict, Any
from omegaconf import OmegaConf, DictConfig
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


# Load configuration from YAML
CONFIG_PATH = Path(__file__).parent / "llm_config.yaml"
_config = OmegaConf.load(CONFIG_PATH)


def _get_single_llm_model(model_cfg: DictConfig):
    """
    Creates a single LLM instance from a model configuration.

    Args:
        model_cfg: Configuration dict containing model_name, temperature, etc.

    Returns:
        LLM instance (ChatOpenAI or ChatGoogleGenerativeAI)
    """
    model_name = model_cfg.model_name

    # OpenAI models (GPT family)
    if "gpt" in model_name.lower():
        kwargs = {
            "model": model_name,
            "temperature": model_cfg.get("temperature", 0.7),
        }
        if hasattr(model_cfg, "max_tokens"):
            kwargs["max_tokens"] = model_cfg.max_tokens
        if hasattr(model_cfg, "reasoning_effort"):
            kwargs["reasoning_effort"] = model_cfg.reasoning_effort
        return ChatOpenAI(**kwargs)

    # OpenAI reasoning models (o3-mini, o4-mini)
    elif "o3-mini" in model_name or "o4-mini" in model_name:
        kwargs = {"model": model_name}
        if hasattr(model_cfg, "max_tokens"):
            kwargs["max_tokens"] = model_cfg.max_tokens
        return ChatOpenAI(**kwargs)

    # Google Gemini models
    elif "gemini" in model_name.lower():
        kwargs = {
            "model": model_name,
            "temperature": model_cfg.get("temperature", 0.7),
        }
        if hasattr(model_cfg, "max_tokens"):
            kwargs["max_tokens"] = model_cfg.max_tokens
        if hasattr(model_cfg, "thinking_mode"):
            kwargs["include_thoughts"] = model_cfg.thinking_mode
        if hasattr(model_cfg, "thinking_budget"):
            kwargs["thinking_budget"] = model_cfg.thinking_budget
        return ChatGoogleGenerativeAI(**kwargs)

    # Add other providers as needed
    # elif "claude" in model_name.lower():
    #     from langchain_anthropic import ChatAnthropic
    #     return ChatAnthropic(...)

    else:
        raise NotImplementedError(f"LLM {model_name} not supported")


def get_llm_models(cfg_section: DictConfig) -> Dict[str, Any]:
    """
    Creates a dictionary of LLM instances from a configuration section.

    Args:
        cfg_section: OmegaConf DictConfig where each key is an LLM name
                    and value contains its configuration.

    Returns:
        Dictionary mapping LLM names to initialized LLM objects.
    """
    llms = {}
    for llm_name, model_cfg in cfg_section.items():
        if isinstance(model_cfg, DictConfig) and "model_name" in model_cfg:
            llms[llm_name] = _get_single_llm_model(model_cfg)
    return llms


# Factory functions for specific tasks
def get_chat_llm():
    """
    Get LLM for chat generation.

    Configuration: llm_config.yaml -> models.chat
    """
    return _get_single_llm_model(_config.models.chat)


def get_chat_fallback_llm():
    """
    Get fallback LLM for chat generation when primary model fails.

    Configuration: llm_config.yaml -> models.chat_fallback
    """
    return _get_single_llm_model(_config.models.chat_fallback)


def get_diary_llm():
    """
    Get LLM for diary generation.

    Configuration: llm_config.yaml -> models.diary
    """
    return _get_single_llm_model(_config.models.diary)


def get_diary_split_llm():
    """
    Get LLM for diary paragraph splitting.

    Configuration: llm_config.yaml -> models.diary_split
    """
    return _get_single_llm_model(_config.models.diary_split)


def get_emotion_finding_llms() -> List:
    """
    Get LLMs for emotion finding with varying temperatures.

    Returns a list of 4 LLM instances with different temperatures
    for diverse emotion extraction.

    Configuration: llm_config.yaml -> models.emotion_finding
    """
    emotion_cfg = _config.models.emotion_finding
    return [
        _get_single_llm_model(emotion_cfg.primary),
        _get_single_llm_model(emotion_cfg.low),
        _get_single_llm_model(emotion_cfg.medium),
        _get_single_llm_model(emotion_cfg.high),
    ]


def get_remake_llm():
    """
    Get LLM for sentence remaking.

    Configuration: llm_config.yaml -> models.remake
    """
    return _get_single_llm_model(_config.models.remake)


# Logging configuration on module load
print("=" * 60)
print("LLM Configuration Loaded from: llm_config.yaml")
print("=" * 60)
print(f"Chat          : {_config.models.chat.model_name} (temp={_config.models.chat.temperature})")
print(f"Chat Fallback : {_config.models.chat_fallback.model_name} (temp={_config.models.chat_fallback.temperature})")
print(f"Diary         : {_config.models.diary.model_name} (temp={_config.models.diary.temperature})")
print(f"Diary Split   : {_config.models.diary_split.model_name} (temp={_config.models.diary_split.temperature})")
print(f"Emotion (x4)  : {_config.models.emotion_finding.primary.model_name} (temps: 0.0, 0.25, 0.5, 0.75)")
print(f"Remake        : {_config.models.remake.model_name} (temp={_config.models.remake.temperature})")
print("=" * 60)
