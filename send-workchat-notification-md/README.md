# GitHub Action to send notifications via Workchat (Button Template)

This GitHub action allow sending chat messages using ServiceRocket's Workplace Publisher. 

Messages sent use Facebook Messenger [Button Template](https://developers.facebook.com/docs/messenger-platform/reference/templates/button) with a single button.

## Usage

```yaml
- name: Send Workchat notification
  # Always include commit hash to make sure new versions of the action does not break your workflow.
  uses: servicerocket/actions/send-workchat-notification@{ref}
  with:
    # Workplace Publisher API endpoint for chat
    api-endpoint: 
    # Workplace Publisher API Key
    api-key: 
    # Workplace ID of the message recipient
    recipient-id: 
    # Message text (supports [Facebook Messenger formatting](https://www.facebook.com/help/147348452522644))
    text: 
    # Button Text
    button-text: #optional, default is 'View'
    # Button URL
    button-url: 
    
```

### Example

```yaml
- name: Send Workchat notification to 12345678
  uses: servicerocket/actions/send-workchat-notification-md@12209e7
  with:
    api-endpoint: ${{ secrets.WORKPLACE_PUBLISHER_API_ENDPOINT }}
    api-key: ${{ secrets.WORKPLACE_PUBLISHER_API_GATEWAY_KEY }}
    recipient-id: 12345678
    text: "Here is my message!"
    button-url: "https://link.example.com"
```
