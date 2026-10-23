# SIS 2 — Test Automation with Playwright

**Site under test:** https://practicesoftwaretesting.com/ (Toolshop demo)
**Stack:** Python + Playwright + pytest (`pytest-playwright`)

## What I want to do
Automate core user flows of the web shop in 5 test suites (18 test cases), using stable `data-test` locators and Playwright auto-waiting / `expect_response` instead of fixed sleeps.

## List of TCs to be automated
| Suite | File | Test cases |
|---|---|---|
| 1. Login | `test_01_login.py` | valid login; wrong password; empty fields validation; logout |
| 2. Registration | `test_02_registration.py` | empty form errors; weak password rejected; successful registration (unique email) |
| 3. Search | `test_03_search.py` | existing product; no results; reset search |
| 4. Catalog sort/pagination | `test_04_catalog_sort.py` | products shown; price asc; name A-Z; next page |
| 5. Product & Cart | `test_05_product_and_cart.py` | product details; add to cart; change quantity -> total; remove from cart |

## How to run
```
pip install -r requirements.txt
playwright install chromium
pytest
```
Failure screenshots are saved to `screenshots/`.
