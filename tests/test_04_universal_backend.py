"""
Unit test runner for Lesson 04: Universal Python Backend Toolkit.
"""

import asyncio
import sys
import unittest
from pathlib import Path
import importlib.util

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

practice_file = PROJECT_ROOT / "practice" / "04_universal_backend_essentials.py"
if not practice_file.exists():
    raise FileNotFoundError(f"Cannot find {practice_file}")

spec = importlib.util.spec_from_file_location("user_universal", practice_file)
user_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_module)


class TestLesson04(unittest.TestCase):

    def test_enum_and_auth_success(self):
        self.assertTrue(hasattr(user_module, "UserRole"))
        self.assertEqual(user_module.UserRole.ADMIN.value, "admin")
        self.assertEqual(user_module.UserRole.EDITOR.value, "editor")
        self.assertEqual(user_module.UserRole.VIEWER.value, "viewer")

        # Allowed role check
        allowed = [user_module.UserRole.ADMIN, user_module.UserRole.EDITOR]
        self.assertTrue(user_module.authorize_user(user_module.UserRole.ADMIN, allowed))

    def test_enum_and_auth_failure(self):
        allowed = [user_module.UserRole.ADMIN]
        with self.assertRaises(user_module.AuthenticationError):
            user_module.authorize_user(user_module.UserRole.VIEWER, allowed)

    def test_filter_and_transform_orders(self):
        orders = [
            {"id": "o1", "amount": 100.0, "status": "COMPLETED"},
            {"id": "o2", "amount": 25.0,  "status": "CANCELLED"},
            {"id": "o3", "amount": 200.0, "status": "COMPLETED"},
            {"id": "o4", "amount": 80.0,  "status": "PENDING"}
        ]
        result = user_module.filter_and_transform_orders(orders)
        expected = {
            "o1": 118.0,
            "o3": 236.0
        }
        self.assertEqual(result, expected)

    def test_safe_api_endpoint_decorator(self):
        @user_module.safe_api_endpoint
        def good_endpoint():
            return {"data": "ok"}

        @user_module.safe_api_endpoint
        def bad_endpoint():
            raise ValueError("Database connection failed")

        self.assertEqual(good_endpoint(), {"data": "ok"})
        error_resp = bad_endpoint()
        self.assertEqual(error_resp.get("status"), "error")
        self.assertIn("Database connection failed", error_resp.get("message", ""))

    def test_async_fetch_user_profile(self):
        # Run async function in event loop
        result = asyncio.run(user_module.fetch_user_profile_async("usr_42"))
        self.assertEqual(result, {"id": "usr_42", "active": True})


if __name__ == "__main__":
    unittest.main()
