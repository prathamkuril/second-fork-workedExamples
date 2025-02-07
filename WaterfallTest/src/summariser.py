# Copyright (c) 2024 Braid Technologies Ltd

# Standard Library Imports
import logging
import os
import requests

from summary_repository_facade import SummaryRespositoryFacade

# Set up logging to display information about the execution of the script
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.DEBUG)

SESSION_KEY = os.environ["SessionKey"]

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110',
   'Content-Type': 'application/json',   
   'Accept': 'application/json'
}  

class Summariser:

   def __init__(self, path : str, text: str, output_location: str):
      self.path = path
      self.text = text
      self.output_location = output_location       

   def summarise(self) -> str: 
      '''
      Summarises the text content by either loading an existing summary from the specified path or generating a new summary using an external API. 
      If an existing summary is found, it is returned; otherwise, a new summary is generated and saved at the specified path. 
      Returns the generated or loaded summary as a string.
      '''
      path = self.path
      repository = SummaryRespositoryFacade (self.output_location)      
      if repository.exists (path):          
         return repository.load (path)

      logger.debug("Summarising: %s", path)

      session = requests.Session()

      summaryUrl = f"https://braidapi.azurewebsites.net/api/Summarize?session={SESSION_KEY}"
      input = {
         'data': {
         'text': self.text
         }
      }

      response = session.post(summaryUrl, json=input, headers=headers)
      summary = response.text         

      repository.save (path, summary)

      return summary

