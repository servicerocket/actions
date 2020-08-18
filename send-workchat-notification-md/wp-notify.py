import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Send a message to Workchat using Workplace Publisher.')
    parser.add_argument('url', help="Workplace Publisher endpoint")
    parser.add_argument('token', help="Workplace Publisher API token")
    parser.add_argument('text', help="Body of the message")
    parser.add_argument('button_url', help="URL of the action button")
    parser.add_argument('button_text', help="Text of the action button")
    parser.add_argument('recipients', nargs='+', help="Workplace users IDs to send the message to")
    args = parser.parse_args()

    for recipient in args.recipients:
        body = {
                "recipient": {
                "id": recipient
                },
                "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                    "template_type": "button",
                    "text": args.text,
                    "buttons": [
                            {
                                "type": "web_url",
                                "url": args.button_url,
                                "title": args.button_text
                            }
                        ]
                    }
                }
                }
            }

        ret = requests.post(
            url=args.url,
            headers={'Content-type': 'application/json', 'x-api-key': args.token},
            json=body
        )

        print(ret.text)

if __name__ == '__main__':
    main()
