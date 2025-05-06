import gradio as gr

def predict_churn(CreditScore, Gender, Age, Tenure, Balance, NumOfProducts,
                  HasCrCard, IsActiveMember, EstimatedSalary, Geography):
    
    # Encode and scale input
    gender = 1 if Gender == 'Male' else 0
    geo_Germany = 1 if Geography == 'Germany' else 0
    geo_Spain = 1 if Geography == 'Spain' else 0
    
    input_data = np.array([[CreditScore, gender, Age, Tenure, Balance, NumOfProducts,
                            HasCrCard, IsActiveMember, EstimatedSalary,
                            geo_Germany, geo_Spain]])
    
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]
    
    return "Customer will churn." if prediction > 0.5 else "Customer will not churn."

# UI fields
interface = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Slider(300, 900, step=1, label="Credit Score"),
        gr.Radio(["Male", "Female"], label="Gender"),
        gr.Slider(18, 92, step=1, label="Age"),
        gr.Slider(0, 10, step=1, label="Tenure"),
        gr.Number(label="Balance"),
        gr.Slider(1, 4, step=1, label="Number of Products"),
        gr.Radio([0, 1], label="Has Credit Card (0 = No, 1 = Yes)"),
        gr.Radio([0, 1], label="Is Active Member (0 = No, 1 = Yes)"),
        gr.Number(label="Estimated Salary"),
        gr.Radio(["France", "Germany", "Spain"], label="Geography"),
    ],
    outputs="text",
    title="Customer Churn Prediction",
    description="Enter customer details to predict whether they will churn or not."
)

interface.launch()
