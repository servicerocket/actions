# GitHub Action to send notifications via Workchat

This GitHub action allow sending chat messages using ServiceRocket's Workplace Publisher. 

## Usage

```yaml
- name: Send Workchat notification to 12345678
  # Include commit hash to make sure new versions of the action does not break your workflow
  uses: servicerocket/actions/send-workchat-notification@12209e7
  with:
    api-endpoint: ${{ secrets.WORKPLACE_PUBLISHER_API_ENDPOINT }}
    api-key: ${{ secrets.WORKPLACE_PUBLISHER_API_GATEWAY_KEY }}
    recipient-id: 12345678
    title: "Some important title"
    subtitle: "A nice subtitle"
    button-url: "https://link.example.com"
```
