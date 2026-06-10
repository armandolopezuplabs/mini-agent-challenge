"""
mini_agent.py
=============
A naive single-file agent loop written by a junior engineer.
It runs OFFLINE against a mock LLM (no API keys, no network).

CANDIDATE TASK (read the interviewer prompt aloud):
  "This agent is supposed to answer 'What is the weather in Madrid in
   Fahrenheit?' by calling tools. Run it. It does not work. In ~15 minutes,
   walk me through everything you'd change to make this production-ready,
   then implement the TWO changes you think matter most."

Do NOT modify the MockLLM class — treat it as an external provider.
Everything else is fair game.
"""

import json


# ----------------------------------------------------------------------
# Mock LLM provider (stands in for Anthropic/OpenAI/etc.). DO NOT MODIFY.
# Returns scripted assistant turns so the loop runs without API keys.
# ----------------------------------------------------------------------
class MockLLM:
    def __init__(self):
        self.turn = 0
        self.script = [
            # turn 0: valid tool call
            '{"thought": "I need the weather", "tool": "get_weather", "args": {"city": "Madrid"}}',
            # turn 1: tool call with a non-numeric arg
            '{"thought": "Now convert it", "tool": "celsius_to_f", "args": {"temp": "warm"}}',
            # turn 2+: model gets stuck repeating the same call forever
            '{"thought": "Let me check the weather again", "tool": "get_weather", "args": {"city": "Madrid"}}',
        ]

    def complete(self, messages):
        idx = min(self.turn, len(self.script) - 1)
        self.turn += 1
        return self.script[idx]


# ----------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------
def get_weather(city):
    data = {"Madrid": 30, "Lima": 18}
    return data[city]


def celsius_to_f(temp):
    return temp * 9 / 5 + 32


TOOLS = {
    "get_weather": get_weather,
    "celsius_to_f": celsius_to_f,
}


# ----------------------------------------------------------------------
# Agent loop
# ----------------------------------------------------------------------
def run_agent(goal):
    llm = MockLLM()
    messages = [{"role": "user", "content": goal}]

    while True:
        raw = llm.complete(messages)
        messages.append({"role": "assistant", "content": raw})

        action = json.loads(raw)
        tool = action["tool"]
        args = action["args"]

        result = TOOLS[tool](**args)
        print(f"[tool] {tool}({args}) -> {result}")
        messages.append({"role": "tool", "content": str(result)})

    return result


if __name__ == "__main__":
    answer = run_agent("What is the weather in Madrid in Fahrenheit?")
    print(f"\nFinal answer: {answer}")
