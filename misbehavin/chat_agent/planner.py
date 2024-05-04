import weave
import weave.configure.quick as wc
import pydantic

import misbehavin.chat_agent.planner_data as planner_data
import dataclasses
import argparse

import weave.builtins.uagents.pydantic_pattern as pydantic_pattern

wc.set_relative_weave_data_root("../weave_data")


PLANNER = pydantic_pattern.PydanticPattern(planner_data.EXAMPLE_PLANS, '{P.planner.plan_directions}')


def make_plan_for_website(website_desc):
    return PLANNER.infer(website_desc)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("website_desc", help="Description of the website")
    args = parser.parse_args()

    result = make_plan_for_website(args.website_desc)
    for i, attempt in enumerate(result.list_of_attempts):
        print(i, attempt.plan_type, attempt.description)

if __name__ == "__main__":
    main()

