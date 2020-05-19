# aws-enable-guardduty-allregions

Enables GuardDuty Delegated Administrator Account in all regions

## Steps

1. Clean up your existing GuardDuty implementation, if you have one
2. Run ```enable_guardduty.py``` in the Organization Master Billing Account
3. Run ```update_guardduty_config.py``` in the GuardDuty delegated admin account
4. Deploy GuardDuty stack as stackset to all accounts in Org
