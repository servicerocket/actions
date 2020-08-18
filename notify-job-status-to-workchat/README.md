# GitHub Action to send Job Status notifications via Workchat

This GitHub action send a chat messages containing status details of the job being run using ServiceRocket's Workplace Publisher.

## Usage

```yaml
- name: Notify Job Status
  # Always include commit hash to make sure new versions of the action does not break your workflow.
  uses: servicerocket/actions/notify-job-status-to-workchat@{ref}
  with:
    # Workplace Publisher API endpoint for chat
    api-endpoint: 
    # Workplace Publisher API Key
    api-key: 
    # Workplace ID of the message recipients separated by spaces (add "t_" for chat groups and make sure bot is a member of the group)
    recipients-id: 
```

### Example

```yaml
- name: Notify Job Status to 12345678 and t_45678901
  uses: servicerocket/actions/notify-job-status-to-workchat@1234567
  with:
    api-endpoint: ${{ secrets.WORKPLACE_PUBLISHER_API_ENDPOINT }}
    api-key: ${{ secrets.WORKPLACE_PUBLISHER_API_GATEWAY_KEY }}
    recipients-id: "12345678 t_45678901"
```
