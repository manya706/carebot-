# import os
# import openai
# import gradio as gr
# openai.api_key = "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"
# start_sequence="\nAI:"
# restart_sequence="\nHuman: "
# prompt="The following conversation is with an ai assistant and patient who wants to check if the medicines given to him is suitable for him or not \nPatient: Hi i am the patient \nAI: Hi how are you",
# def openai_create(prompt):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=["Patient:","AI:"]
#     )
#     return response.choices[0].text 

# def conversation_history(input,history):
#     history=history or []
#     s=list(sum(history,()))
#     s.append(input)
#     inp=' '.join(s)
#     output=openai_create(inp)
#     history.append(input,output)
#     return history,history
    
# blocks=gr.Blocks() 
# with blocks:
#     chatbot=gr.Chatbot()
#     message=gr.Textbox(placeholder=prompt)
#     state=gr.State()
#     submit=gr.Button("Click")
#     submit.click(conversation_history,inputs=[message,state],outputs=[chatbot,state])
    
# blocks.launch(debug=True)
# import os
# import openai
# import gradio as gr

# openai.api_key = "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"
# start_sequence="\nAI:"
# restart_sequence="\nHuman: "
# prompt="The following conversation is with an ai assistant and patient who wants to check if the medicines given to him is suitable for him or not \nPatient: Hi i am the patient \nAI: Hi how are you"

# def openai_create(prompt):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=["Patient:","AI:"]
#     )
#     return response.choices[0].text 

# def conversation_history(input,history):
#     history=history or []
#     s=list(sum(history,()))
#     s.append(input)
#     inp=' '.join(s)
#     output=openai_create(inp)
#     history.append((input,output))
#     return history,history


# blocks=gr.Interface(fn=conversation_history, 
#                      inputs=[gr.inputs.Textbox(placeholder=prompt)], 
#                      outputs=[gr.outputs.Textbox(label="AI Response"), gr.outputs.Textbox(label="Conversation History")], 
#                      title="Conversation with AI", 
#                      description="Enter your message and see how the AI responds!", 
#                      theme="compact")
# blocks.launch()
#import os
import openai
import gradio as gr

openai.api_key = "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"
start_sequence="\nAI:"
restart_sequence="\nHuman: "
prompt="The following conversation is with an ai assistant and patient who wants to check if the medicines given to him is suitable for him or not \nPatient: Hi i am the patient \nAI: Hi how are you"

class GPT:
    def __init__(self):
        self.gpt = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["Patient:","AI:"]
        )

    def answer(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["Patient:","AI:"]
        )
        return response.choices[0].text

gpt = GPT()

def conversation_history(input_text):
    global history
    input_text = input_text.strip()
    prompt = "Patient: " + input_text + restart_sequence
    response = gpt.answer(prompt)
    history.append(("Patient: " + input_text, response.strip()))
    return response.strip(), "\n\n".join([f"{t[0]}\nAI: {t[1]}" for t in history])

history = [("Patient:", "Hi i am the patient"), ("AI:", "Hi how are you")]
inputs = gr.inputs.Textbox(lines=2, placeholder="Start conversation here...")
outputs = [gr.outputs.Textbox(label="AI Response"), gr.outputs.Textbox(label="Conversation History")]

interface = gr.Interface(fn=conversation_history, inputs=inputs, outputs=outputs, title="Validate Prescription with AI", 
                         description="The following conversation is with an ai assistant and patient who wants to check if the medicines given to him is suitable for him or not ", theme="compact",css="""
                            body{
                              background-image: url('https://blog.academyoflearning.com/wp-content/uploads/2017/04/bigstock-Home-health-care-worker-and-an-13926641.jpg');  
                            }
                            """)
# interface = gr.Interface(fn=conversation_history, inputs=inputs, outputs=outputs, title="Conversation with AI", 
#                          description="Enter your message and see how the AI responds!", theme="compact",
#                          live_css=True, css_style="body { background-image: url('https://blog.academyoflearning.com/wp-content/uploads/2017/04/bigstock-Home-health-care-worker-and-an-13926641.jpg'); }")
interface.launch()