import argparse



'''

Implements a chat agent which chats with the website.

'''

import weave
import weave.builtins.knits.chat as chat
import weave.configure.quick as wc

wc.set_relative_weave_data_root("../weave_data")


class Chatter:
    
    def __init__(self, website_desc, plan_directions):
        self.website_desc = website_desc
        self.plan_directions = plan_directions
        self.system_prompt = weave.Weave('{P.chatter.system_prompt}').format(website_desc=website_desc, plan_directions=plan_directions)
        self.chat = chat.Chat(system_prompt=self.system_prompt)

    def next_message(self, last_message):
        return self.chat.infer(last_message).unweave()


def example_loop(website_desc, plan_directions):
    print('Website: ', website_desc)
    print('Instructions: ', plan_directions)
    chatter = Chatter(website_desc, plan_directions)
    first_message = chatter.next_message('How can I help you?')
    print(f'Chatter: {first_message}')
    while True:
        last_message = input("You: ")
        next_message = chatter.next_message(last_message)
        print(f"Chatter: {next_message}")


def main():
    parser = argparse.ArgumentParser(description='Chat Agent')
    parser.add_argument('website_desc', type=str, help='Website description')
    parser.add_argument('plan_directions', type=str, help='Plan directions')
    
    args = parser.parse_args()
    
    website_desc = args.website_desc
    plan_directions = args.plan_directions
    
    try:
        example_loop(website_desc, plan_directions)
    except KeyboardInterrupt:
        print('\nGoodbye!')

if __name__ == '__main__':
    main()

