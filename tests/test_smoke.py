import pytest

@pytest.mark.smoke
def test_homepage_title(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    # Adjust expected title for your app
    assert page.title() != "", "Page title should not be empty"

@pytest.mark.smoke
def test_core_nav_links_render(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    # Replace with real selectors for your app, e.g.:
    # page.get_by_role("link", name="Search").is_visible()
    assert page.locator("body").is_visible()

# Example placeholder for a login flow (commented until customized)
# import os
# @pytest.mark.smoke
# def test_login_flow(page, base_url):
#     page.goto(f"{base_url}/login", wait_until="domcontentloaded")
#     page.get_by_label("Email").fill(os.environ["TEST_USER_EMAIL"])
#     page.get_by_label("Password").fill(os.environ["TEST_USER_PASSWORD"])
#     page.get_by_role("button", name="Sign in").click()
#     page.get_by_text("Welcome").wait_for()
#     assert page.url.startswith(f"{base_url}/dashboard")