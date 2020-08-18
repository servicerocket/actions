import requests
import argparse
import os
import textwrap

def main():
    parser = argparse.ArgumentParser(description='Send a message to Workchat using Workplace Publisher.')
    parser.add_argument('url', help="Workplace Publisher endpoint")
    parser.add_argument('token', help="Workplace Publisher API token")
    parser.add_argument('job_status', help="Job status")
    parser.add_argument('--commit_message', help="Commit message")
    parser.add_argument('recipients', nargs='+', help="Workplace users IDs to send the message to")
    args = parser.parse_args()

    text = textwrap.dedent(f'''
        *{os.environ['GITHUB_REPOSITORY']}*
        _{os.environ['GITHUB_WORKFLOW']} #{os.environ['GITHUB_RUN_NUMBER']}_
        
        {'💚' if args.job_status == 'success' else '🐞'} {args.job_status.upper()}
        {'😎' if args.job_status == 'success' else '😨'} {os.environ['GITHUB_ACTOR']}
    ''')

    if (args.commit_message):
        text = text + f'```\n{args.commit_message}\n```'

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
                    "text": text,
                    "buttons": [
                            {
                                "type": "web_url",
                                "url": f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}",
                                "title": "View details"
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
