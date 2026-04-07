# ============================================================
# Application Configuration
# WARNING: This file should never be committed to version control
# (But let's pretend someone forgot that rule)
# ============================================================

# Cloud provider keys
AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Version control platform token
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"

# Payment processor
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

# Primary database
DATABASE_URL = "postgres://admin:SuperSecret123!@prod-db.internal.company.com:5432/myapp_prod"

# Notification service
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Safe to commit - marked explicitly
PLACEHOLDER = "this-is-not-a-real-key"  # betterleaks:allow