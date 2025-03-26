import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import base64
import io
from PIL import Image, ImageDraw, ImageFont

import torch
import torchvision.models as models
import torch.nn as nn
from torchvision import transforms

# Load the trained model
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(512, 2)  # Assuming 2 classes: Stop and Not Stop
model.load_state_dict(torch.load(r'C:\Users\hophu\OneDrive\Documents\GitHub\hophuoclanh_2102114\plotly\model.pt', map_location=torch.device('cpu')))
model.eval()

# Image transform (same as training)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Dash app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H2("Stop Sign Detector (AI-powered)", className="my-3 text-center"),

    dcc.Upload(
        id='upload-image',
        children=html.Div(['📤 Drag and Drop or ', html.A('Select an Image')]),
        style={
            'width': '100%',
            'height': '120px',
            'lineHeight': '120px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '10px',
            'textAlign': 'center',
            'margin': '20px'
        },
        multiple=False
    ),
    html.Div(id='output-image-container')
])

def detect_stop_sign(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_for_model = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(img_for_model)
        _, pred = torch.max(output.data, 1)

    label = "STOP" if pred.item() == 0 else "NOT STOP"

    # Draw label on image
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    draw.text((10, 10), f"Prediction: {label}", fill="red", font=font)

    # Convert image to base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    encoded = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{encoded}"

@app.callback(
    Output('output-image-container', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename')
)
def update_output(contents, filename):
    if contents is None:
        return []

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    img_result = detect_stop_sign(decoded)

    return html.Div([
        html.H5(f"Result for: {filename}"),
        html.Img(src=img_result, style={"width": "100%", "maxWidth": "600px"})
    ])

if __name__ == '__main__':
    app.run(debug=True)
