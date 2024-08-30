import json

if __name__ == "__main__":

    with open('results/None_ProntoQA_dev_gpt-3.5-turbo.json', 'r') as file:
        response = json.load(file)
        response = response[0]
    print(response.keys())
    print(f"""
Question:{response['question']} \n
Context:{response['original_context']} \n
Translation:
{response['context']} \n
Plan:{response['plan']} \n
Predicted answer: {response['predicted_choice']}   Actual answer: {response['answer']}
          """)