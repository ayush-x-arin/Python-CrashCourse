"""
Lesson 04: Universal Python Backend Toolkit
==========================================
Complete Solution: Bridges Java / Spring Boot to Python Backend
"""

import asyncio
from enum import Enum
from functools import wraps
from typing import List, Dict, Any, Callable


# ---------------------------------------------------------------------------
# Task 1: Enums & Custom Exceptions
# Java equivalent: public enum UserRole { ADMIN("admin"), ... }
# ---------------------------------------------------------------------------

class UserRole(str, Enum):
    """
    User roles enum.
    Inheriting from (str, Enum) allows seamless JSON serialization in FastAPI.
    """
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class AuthenticationError(Exception):
    """Custom exception, equivalent to Java's AuthenticationException."""
    pass


def authorize_user(user_role: UserRole, allowed_roles: List[UserRole]) -> bool:
    """
    Checks if user_role is in allowed_roles.
    Throws AuthenticationError if not authorized (like Java throw new AuthenticationError(...)).
    """
    if user_role in allowed_roles:
        return True
    raise AuthenticationError(f"Role '{user_role.value}' is not authorized")


# ---------------------------------------------------------------------------
# Task 2: Stream API Equivalent (Dict Comprehension)
# Java equivalent: orders.stream().filter(...).collect(Collectors.toMap(...))
# ---------------------------------------------------------------------------

def filter_and_transform_orders(orders: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Filters COMPLETED orders and calculates amount with 18% tax.
    Uses a concise Python dict comprehension.
    """
    return {
        order["id"]: round(order["amount"] * 1.18, 2)
        for order in orders
        if order.get("status") == "COMPLETED"
    }


# ---------------------------------------------------------------------------
# Task 3: Python Decorator (@safe_api_endpoint)
# Java equivalent: Spring AOP @Around advice / @ControllerAdvice Exception Handler
# ---------------------------------------------------------------------------

def safe_api_endpoint(func: Callable) -> Callable:
    """
    Decorator that wraps an endpoint:
    Catches any unhandled Exception and returns a clean error dictionary.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            return {"status": "error", "message": str(err)}
    return wrapper


# ---------------------------------------------------------------------------
# Task 4: Async / Await Handler
# Java equivalent: CompletableFuture.supplyAsync(...) / Spring WebFlux Mono
# ---------------------------------------------------------------------------

async def fetch_user_profile_async(user_id: str) -> Dict[str, Any]:
    """
    Simulates non-blocking async I/O (database query or external API call).
    In FastAPI, async def allows the server to handle 10,000+ concurrent requests.
    """
    await asyncio.sleep(0.01)  # Non-blocking pause
    return {"id": user_id, "active": True}


if __name__ == "__main__":
    print("UserRole ADMIN:", UserRole.ADMIN, "Value:", UserRole.ADMIN.value)

    orders = [
        {"id": "o1", "amount": 100.0, "status": "COMPLETED"},
        {"id": "o2", "amount": 50.0,  "status": "CANCELLED"},
        {"id": "o3", "amount": 200.0, "status": "COMPLETED"},
    ]
    print("Transformed Orders:", filter_and_transform_orders(orders))

    # Test decorator
    @safe_api_endpoint
    def risky_endpoint():
        raise ConnectionError("Database timed out!")

    print("Decorator Caught Error:", risky_endpoint())

    # Test async
    profile = asyncio.run(fetch_user_profile_async("usr_42"))
    print("Async Profile Fetched:", profile)
