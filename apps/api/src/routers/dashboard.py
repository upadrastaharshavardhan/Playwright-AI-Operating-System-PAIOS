from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
async def get_dashboard_metrics():
    return {
        "overview": {
            "total_tests": 4782,
            "total_executions": 18934,
            "total_failures": 1256,
            "active_agents": 6,
            "releases_assessed": 42
        },
        "quality_score": 87,
        "failure_breakdown": {
            "locator_drift": 482,
            "environment_issue": 312,
            "regression": 198,
            "flaky_test": 264
        },
        "recent_activity": [
            {"time": "2 min ago", "agent": "Self-Healing", "action": "Healed #loginBtn locator", "status": "success"},
            {"time": "5 min ago", "agent": "Release Risk", "action": "Scored PR #1287: 78/100", "status": "warning"},
            {"time": "12 min ago", "agent": "Test Designer", "action": "Generated 24 tests for checkout", "status": "success"},
        ],
        "module_health": [
            {"module": "auth-service", "health": 92, "trend": "up"},
            {"module": "payment-service", "health": 78, "trend": "down"},
            {"module": "notification-service", "health": 85, "trend": "stable"},
        ]
    }
