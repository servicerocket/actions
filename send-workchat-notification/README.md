# GitHub Action to send notifications via Workchat

This GitHub action allow sending chat messages using ServiceRocket's Workplace Publisher. 

Messages sent use Facebook Messenger [Generic Template](https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic) with a single button and an optional image.

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
    # Message title
    title: 
    # Message subtitle
    subtitle: # optional
    # Button Text
    button-text: #optional, default is 'View'
    # Button URL
    button-url: 
    # Image URL
    image-url: #optional
    # Image Aspect Ratio
    image-aspect-ratio: #optional, either 'square' or 'horizontal', default is 'horizontal'
    
```

### Example

```yaml
- name: Send Workchat notification to 12345678
  uses: servicerocket/actions/send-workchat-notification@12209e7
  with:
    api-endpoint: ${{ secrets.WORKPLACE_PUBLISHER_API_ENDPOINT }}
    api-key: ${{ secrets.WORKPLACE_PUBLISHER_API_GATEWAY_KEY }}
    recipient-id: 12345678
    title: "Some important title"
    subtitle: "A nice subtitle"
    button-url: "https://link.example.com"
```
