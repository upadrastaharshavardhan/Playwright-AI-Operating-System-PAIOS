from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_plugins():
    return [
        {"name": "Jira Connector", "version": "1.0.0", "status": "active"},
        {"name": "Slack Notifier", "version": "1.0.0", "status": "active"},
        {"name": "Azure DevOps", "version": "0.9.0", "status": "beta"},
    ]
