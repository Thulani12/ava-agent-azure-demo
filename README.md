
# AVA Agent Demo for Standard Bank

This demo deploys a LangGraph-based AVA Agent on Azure using AI Foundry.

## Components

- Azure App Service (LangGraph + FastAPI)
- Azure OpenAI GPT-4 via Foundry
- Azure AI Search and Blob for Knowledge Store
- Streamlit UI for interaction

## Deploy Steps

1. Use Terraform to deploy the infrastructure.
2. Build and deploy the backend (FastAPI) and Streamlit frontend.
3. Load knowledge docs into Azure Blob, vectorize via Foundry.

See `terraform/` folder for IaC and `app/` for app logic.
