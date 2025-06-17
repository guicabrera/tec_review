#-----------------------------------------------------------------------------
#Open AI Azure Client Conection Setup 
#This code sets up a connection to the Azure OpenAI service using the AzureOpenAI
from openai import AzureOpenAI
import openai
import httpx

#Define properties
#-----------------------------------------------------------------------------
openai.api_type = "azure"
openai.api_base = "https://your-azure-openai-endpoint.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "your-azure-openai-key"
#-----------------------------------------------------------------------------

httpx_client = httpx.Client(verify="cacert.pm",timeout=60.0)

client = AzureOpenAI(
    azure_endpoint=openai.api_base,
    api_key=openai.api_key,
    api_version=openai.api_version,
    httpx_client=httpx_client
)

#-----------------------------------------------------------------------------
