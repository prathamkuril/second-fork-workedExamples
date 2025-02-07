# Copyright (c) 2024 Braid Technologies Ltd

from abc import ABC, abstractmethod
from typing import List
import logging
from openai import AzureOpenAI
import os
import sys

# Add the project root and scripts directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from common.ApiConfiguration import ApiConfiguration
from common.common_functions import get_embedding
from openai import AzureOpenAI, OpenAIError, BadRequestError, APIConnectionError
from BoxerDataTest_v1 import call_openai_chat


# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for Persona Prompts
DEVELOPER_PROMPT = "You are a programmer interested in the details of writing applications that use an LLM in Python."
TESTER_PROMPT = "You are a tester who wants to know how to assess and ensure quality in an application that uses LLM technology."
BUSINESS_ANALYST_PROMPT = "You are a business analyst interested in how people can apply LLM technology to solve business problems."

class PersonaStrategy(ABC):
    @abstractmethod
    def generate_questions(self, client: AzureOpenAI, config: ApiConfiguration, num_questions: int, logger: logging.Logger) -> List[str]:
    """
    Generates a list of questions based on a persona.

    Args:
        client (AzureOpenAI): An instance of the AzureOpenAI class.
        config (ApiConfiguration): An instance of the ApiConfiguration class.
        num_questions (int): The number of questions to generate.
        logger (logging.Logger): An instance of the logging.Logger class.

    Returns:
        List[str]: A list of questions generated based on the persona.
    """
        pass  # This is an abstract method to be implemented by subclasses

    def _generate_questions(self, client: AzureOpenAI, config: ApiConfiguration, prompt: str, num_questions: int, logger: logging.Logger) -> List[str]:
    """
    Generates a list of questions based on a prompt.

    Args:
        client (AzureOpenAI): An instance of the AzureOpenAI class.
        config (ApiConfiguration): An instance of the ApiConfiguration class.
        prompt (str): The prompt to use when generating the questions.
        num_questions (int): The number of questions to generate.
        logger (logging.Logger): An instance of the logging.Logger class.

    Returns:
        List[str]: A list of questions generated based on the prompt.
    """

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Generate {num_questions} questions about this topic."},
        ]
        logger.info("Generating questions with the following prompt: %s", prompt)
        response = call_openai_chat(client, messages, config, logger)
        questions = response.split('\n')
        return [q for q in questions if q.strip()]

class DeveloperPersonaStrategy(PersonaStrategy):
    def generate_questions(self, client: AzureOpenAI, config: ApiConfiguration, num_questions: int, logger: logging.Logger) -> List[str]:
    """
    Generates a list of questions based on the developer persona.

    Args:
        client (AzureOpenAI): An instance of the AzureOpenAI class.
        config (ApiConfiguration): An instance of the ApiConfiguration class.
        num_questions (int): The number of questions to generate.
        logger (logging.Logger): An instance of the logging.Logger class.

    Returns:
        List[str]: A list of questions generated based on the developer persona.
    """
        return self._generate_questions(client, config, DEVELOPER_PROMPT, num_questions, logger)

class TesterPersonaStrategy(PersonaStrategy):
    def generate_questions(self, client: AzureOpenAI, config: ApiConfiguration, num_questions: int, logger: logging.Logger) -> List[str]:
    """
    Generates a list of questions based on the tester persona.

    Args:
        client (AzureOpenAI): An instance of the AzureOpenAI class.
        config (ApiConfiguration): An instance of the ApiConfiguration class.
        num_questions (int): The number of questions to generate.
        logger (logging.Logger): An instance of the logging.Logger class.

    Returns:
        List[str]: A list of questions generated based on the tester persona.
    """
        return self._generate_questions(client, config, TESTER_PROMPT, num_questions, logger)

class BusinessAnalystPersonaStrategy(PersonaStrategy):
    def generate_questions(self, client: AzureOpenAI, config: ApiConfiguration, num_questions: int, logger: logging.Logger) -> List[str]:
    """
    Generates a list of questions based on the business analyst persona.

    Args:
        client (AzureOpenAI): An instance of the AzureOpenAI class.
        config (ApiConfiguration): An instance of the ApiConfiguration class.
        num_questions (int): The number of questions to generate.
        logger (logging.Logger): An instance of the logging.Logger class.

    Returns:
        List[str]: A list of questions generated based on the business analyst persona.
    """
    
        return self._generate_questions(client, config, BUSINESS_ANALYST_PROMPT, num_questions, logger)