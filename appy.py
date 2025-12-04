import gradio as gr
import pandas as pd
import joblib

# Load model
model = joblib.load("land_conflict_model.pkl")

# Prediction function
def predict_conflict(location, population_density, ownership_type, property_value, conflict_history):
    data = pd.DataFrame([[location, population_density, ownership_type, property_value, conflict_history]])
    prediction = model.predict(data)[0]
    return "HIGH risk of land conflict ⚠️" if prediction == 1 else "LOW risk of land conflict ✅"

# Conflict resolution suggestions
def resolve_type(conflict_type):
    if conflict_type == "Boundary":
        return "Suggestion: Do GPS re-survey and mediation with local leadership."
    elif conflict_type == "Inheritance":
        return "Suggestion: Legal consultation + family meeting mediation."
    elif conflict_type == "Sale Fraud":
        return "Suggestion: Police + legal investigation recommended."
    else:
        return "Further investigation is needed."

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# 🏡 Land Conflict Prediction & Resolution System")

    with gr.Tab("Conflict Prediction"):
        location = gr.Number(label="Location code (1, 2, or 3)")
        population = gr.Number(label="Population density")
        ownership = gr.Number(label="Ownership type (1=title, 2=customary)")
        value = gr.Number(label="Property value")
        history = gr.Number(label="Past conflict cases")

        output = gr.Textbox(label="Prediction Result")
        btn = gr.Button("Predict Conflict")

        btn.click(predict_conflict, [location, population, ownership, value, history], output)

    with gr.Tab("Conflict Resolution Guide"):
        conflict_type = gr.Dropdown(["Boundary", "Inheritance", "Sale Fraud", "Other"], label="Conflict Type")
        result = gr.Textbox(label="Recommended Solution")
        btn2 = gr.Button("Get Solution")

        btn2.click(resolve_type, [conflict_type], result)

app.launch()
