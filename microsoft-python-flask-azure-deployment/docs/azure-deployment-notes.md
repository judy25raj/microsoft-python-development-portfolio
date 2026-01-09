# Azure Deployment Notes

- Subscription: Azure subscription 1 (Free Trial)
- Resource group: judyalexisdc_rg_6257
- App Service plan: judyalexisdc_asp_4265 (F1, Linux)
- Web App: lemon-grass-47001bae3ae04a418083cf45f32c19a5
- Runtime stack: Python 3.11, Linux

Key commands:

```bash
az login
az provider register --namespace Microsoft.Web
az webapp up --runtime "PYTHON:3.11" --sku F1 --logs
```
